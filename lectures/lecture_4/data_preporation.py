"""
Тут описываете флоу подготовки данных перед заливкой в БД (очистка + чанкикнг).
Так же сюда можете закинуть код по извлечению текста из pdf (docling и тп)
"""

from __future__ import annotations

import re
from pathlib import Path

from langchain_core.documents import Document

from chunking import semantic_chunking
from embedder import DEFAULT_EMBEDDING_MODEL, SimpleEmbedder
from lance_db import LanceDBManager, documents_to_records


try:
    from pypdf import PdfReader
except ImportError as exc:
    raise ImportError(
        "Для чтения PDF нужен пакет pypdf. Добавь его в зависимости: pypdf>=5.0.0"
    ) from exc


DATASET_DIR = Path("dataset")


def extract_year_from_filename(filename: str) -> int:
    match = re.search(r"(?<!\d)(?:19|20)\d{2}(?!\d)", filename)
    if not match:
        raise ValueError(f"Не удалось извлечь год из имени файла: {filename}")
    return int(match.group(0))


def clean_text(text: str) -> str:
    """
    Базовая очистка текста без агрессивной нормализации.
    """
    text = text.replace("\xa0", " ").replace("\u200b", " ").replace("\r", "\n")
    text = re.sub(r"-\n(?=\w)", "", text)

    placeholder = "<<<PARA>>>"
    text = re.sub(r"\n{2,}", placeholder, text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = text.replace(placeholder, "\n\n")

    return text.strip()


def extract_text_from_pdf(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    pages: list[str] = []

    for page in reader.pages:
        page_text = page.extract_text() or ""
        page_text = page_text.strip()
        if page_text:
            pages.append(page_text)

    return clean_text("\n\n".join(pages))


def load_pdf_documents(data_dir: Path | str = DATASET_DIR) -> list[dict]:
    data_dir = Path(data_dir)

    documents: list[dict] = []
    for pdf_path in sorted(data_dir.glob("*.pdf")):
        text = extract_text_from_pdf(pdf_path)
        year = extract_year_from_filename(pdf_path.name)

        documents.append(
            {
                "text": text,
                "document_name": pdf_path.stem,
                "source": str(pdf_path),
                "year": year,
            }
        )

    if not documents:
        raise ValueError(f"В папке {data_dir} не найдено PDF-документов")

    return documents


def prepare_chunks(
    data_dir: Path | str = DATASET_DIR,
    chunk_size: int = 900,
    chunk_overlap: int = 150,
) -> list[Document]:
    documents = load_pdf_documents(data_dir)

    chunks: list[Document] = []
    for doc in documents:
        doc_chunks = semantic_chunking(
            text=doc["text"],
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            metadata={
                "document_name": doc["document_name"],
                "source": doc["source"],
                "year": doc["year"],
            },
        )
        chunks.extend(doc_chunks)

    return chunks


def build_vectorstore(
    client,
    data_dir: Path | str = DATASET_DIR,
    embedding_model: str = DEFAULT_EMBEDDING_MODEL,
    vectorstore_dir: str = "lance_db/vectorstore",
    table_name: str = "chunks",
    chunk_size: int = 900,
    chunk_overlap: int = 150,
):
    """
    Полный offline ingest:
    PDF -> clean -> chunk -> embed -> LanceDB
    """
    chunks = prepare_chunks(
        data_dir=data_dir,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    embedder = SimpleEmbedder(
        client=client,
        model=embedding_model,
    )
    embeddings = embedder.embed_documents([chunk.page_content for chunk in chunks])

    records = documents_to_records(chunks, embeddings)

    db = LanceDBManager(
        uri=vectorstore_dir,
        table_name=table_name,
    )
    table = db.create_or_overwrite_table(records)

    return table