from __future__ import annotations

from typing import Any

import lancedb
import pandas as pd
from langchain_core.documents import Document


VECTORSTORE_DIR = "lance_db/vectorstore"
TABLE_NAME = "chunks"


def documents_to_records(documents: list[Document], embeddings: list[list[float]]) -> list[dict[str, Any]]:
    """
    Превращает langchain Document + embeddings в записи для LanceDB.
    """
    if len(documents) != len(embeddings):
        raise ValueError("Количество чанков и количество эмбеддингов должно совпадать")

    records: list[dict[str, Any]] = []

    for doc, vector in zip(documents, embeddings, strict=True):
        metadata = dict(doc.metadata or {})

        document_name = str(metadata.get("document_name", "unknown"))
        chunk_index = int(metadata.get("chunk_id", 0))
        year = int(metadata.get("year", 0))

        records.append(
            {
                "chunk_id": f"{document_name}:{chunk_index}",
                "text": doc.page_content,
                "vector": [float(x) for x in vector],
                "year": year,
                "document_name": document_name,
                "source": str(metadata.get("source", "")),
                "chunk_index": chunk_index,
                "total_chunks": int(metadata.get("total_chunks", 0)),
                "strategy": str(metadata.get("strategy", "")),
                "section": str(metadata.get("section", "")),
            }
        )

    return records


class LanceDBManager:
    """
    Минимальный адаптер для работы с LanceDB.
    """

    def __init__(
        self,
        uri: str = VECTORSTORE_DIR,
        table_name: str = TABLE_NAME,
    ) -> None:
        self.uri = uri
        self.table_name = table_name
        self.db = lancedb.connect(self.uri)
        self.table = None

    def open_table(self):
        if self.table is None:
            self.table = self.db.open_table(self.table_name)
        return self.table

    def create_or_overwrite_table(self, records: list[dict[str, Any]]):
        if not records:
            raise ValueError("Нельзя создать таблицу из пустого списка records")

        self.table = self.db.create_table(
            self.table_name,
            data=records,
            mode="overwrite",
        )
        return self.table

    def insert_records(self, records: list[dict[str, Any]]):
        if not records:
            return self.open_table()

        table = self.open_table()
        table.add(records)
        return table

    def search(
        self,
        query_vector: list[float],
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        table = self.open_table()
        return table.search(query_vector).limit(limit).to_list()

    def read_all(self) -> pd.DataFrame:
        table = self.open_table()
        return table.to_pandas()