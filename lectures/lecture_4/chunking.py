"""
Модуль стратегий чанкинга для RAG-пайплайна.

Каждая стратегия принимает текст (и метаданные документа)
и возвращает список чанков — словарей с ключами:
  - text: str          — текст фрагмента
  - metadata: dict     — метаданные (chunk_id, strategy, ...)

Тут описаны методы чанкинга которые разбирали на практике. Но в их существует огромное кол-во, 
можете даже свой изобрести. Можете использовать готовые методики, можете сделать новый.

"""

from __future__ import annotations

import re

from langchain_core.documents import Document
from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    TextSplitter,
)

# ────────────────────────────────────────────────────────────
# 1. Fixed-Size Chunking
# ────────────────────────────────────────────────────────────


def fixed_size_chunking(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
    metadata: dict | None = None,
) -> list[Document]:
    """
    Разбивает текст на фрагменты фиксированного размера.

    Простейшая стратегия: нарезаем текст на куски по ``chunk_size``
    символов с перекрытием ``chunk_overlap``.  Разделитель — двойной
    перенос строки (абзац), но если абзац длиннее chunk_size,
    текст режется принудительно.

    Args:
        text: исходный текст документа.
        chunk_size: целевой размер чанка (в символах).
        chunk_overlap: перекрытие между соседними чанками.
        metadata: метаданные документа-источника (будут скопированы
                  в каждый чанк).

    Returns:
        Список ``Document`` с полями ``page_content`` и ``metadata``.
    """
    metadata = metadata or {}

    splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    chunks = splitter.split_text(text)

    documents: list[Document] = []
    for i, chunk in enumerate(chunks):
        doc = Document(
            page_content=chunk,
            metadata={
                **metadata,
                "chunk_id": i,
                "total_chunks": len(chunks),
                "chunk_size": len(chunk),
                "strategy": "fixed-size",
            },
        )
        documents.append(doc)

    return documents


# ────────────────────────────────────────────────────────────
# 2. Semantic Chunking (Recursive)
# ────────────────────────────────────────────────────────────

# Паттерны для определения секции документа
_SECTION_PATTERNS = [
    re.compile(r"^#{1,4}\s+(.+)$", re.MULTILINE),  # Markdown-заголовки
    re.compile(r"^\*\*(.{5,80})\*\*", re.MULTILINE),  # **Жирный текст** как заголовок
    re.compile(r"^[А-ЯЁA-Z\s]{10,80}$", re.MULTILINE),  # ЗАГЛАВНЫЕ БУКВЫ
]


def _detect_section(text: str, fallback: str = "Введение") -> str:
    """Пытается определить название секции из текста чанка."""
    for pattern in _SECTION_PATTERNS:
        m = pattern.search(text)
        if m:
            return m.group(1) if m.lastindex else m.group(0)
    return fallback


def semantic_chunking(
    text: str,
    chunk_size: int = 500,
    chunk_overlap: int = 100,
    metadata: dict | None = None,
) -> list[Document]:
    """
    Рекурсивный чанкинг с учётом структуры текста.

    В отличие от fixed-size, ``RecursiveCharacterTextSplitter``
    пробует разделители **по приоритету**:

    1. ``\\n\\n`` — граница абзаца (лучший вариант)
    2. ``\\n``   — перенос строки
    3. ``". "``  — конец предложения (с учётом русской точки)
    4. ``" "``   — пробел
    5. ``""``    — посимвольно (крайний случай)

    Если текст удаётся разбить по более «семантичному» разделителю —
    он используется;  иначе алгоритм спускается к менее осмысленному.

    Дополнительно: для каждого чанка определяется **секция** документа
    (по заголовкам), что позволяет фильтровать при поиске.

    Args:
        text: исходный текст документа.
        chunk_size: целевой размер чанка (в символах).
        chunk_overlap: перекрытие между соседними чанками.
        metadata: метаданные документа-источника.

    Returns:
        Список ``Document`` с расширенными метаданными
        (``section``, ``strategy``).
    """
    metadata = metadata or {}

    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    chunks = splitter.split_text(text)

    documents: list[Document] = []
    current_section = "Введение"

    for i, chunk in enumerate(chunks):
        # Обновляем секцию, если в чанке есть заголовок
        detected = _detect_section(chunk, fallback=current_section)
        current_section = detected

        doc = Document(
            page_content=chunk,
            metadata={
                **metadata,
                "chunk_id": i,
                "total_chunks": len(chunks),
                "chunk_size": len(chunk),
                "strategy": "semantic-recursive",
                "section": current_section,
            },
        )
        documents.append(doc)

    return documents


# ────────────────────────────────────────────────────────────
# 3. Adaptive Chunking
# ────────────────────────────────────────────────────────────

# Простой regex для разбиения на предложения (без nltk)
_SENTENCE_RE = re.compile(
    r"(?<=[.!?…])"  # после знака конца предложения
    r"(?:\s+)"  # один или более пробелов/переносов
    r"(?=[A-ZА-ЯЁ«\"])",  # перед заглавной буквой или открывающей кавычкой
)


def _split_sentences(text: str) -> list[str]:
    """Разбивает текст на предложения с помощью regex."""
    parts = _SENTENCE_RE.split(text.strip())
    return [s.strip() for s in parts if s.strip()]


class _AdaptiveTextSplitter(TextSplitter):
    """Сплиттер, адаптирующий размер чанка под сложность текста.

    Более «сложные» фрагменты (высокая лексическая плотность,
    длинные предложения) получают **меньший** chunk_size,
    а простые — **больший**.
    """

    def __init__(
        self,
        min_chunk_size: int = 300,
        max_chunk_size: int = 1000,
        min_chunk_overlap: int = 30,
        max_chunk_overlap: int = 150,
        complexity_measure: str = "combined",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.min_chunk_size = min_chunk_size
        self.max_chunk_size = max_chunk_size
        self.min_chunk_overlap = min_chunk_overlap
        self.max_chunk_overlap = max_chunk_overlap
        self.complexity_measure = complexity_measure

    # ── метрики сложности ──────────────────────────────────

    @staticmethod
    def _lexical_density(text: str) -> float:
        """Доля уникальных слов (0..1). Выше → богаче лексика."""
        words = re.findall(r"\b\w+\b", text.lower())
        if not words:
            return 0.0
        return min(1.0, len(set(words)) / len(words) / 0.8)

    @staticmethod
    def _sentence_complexity(text: str) -> float:
        """Средняя длина предложения, нормированная к 200 символам."""
        sentences = _split_sentences(text)
        if not sentences:
            return 0.0
        avg = sum(len(s) for s in sentences) / len(sentences)
        return min(1.0, avg / 200)

    def analyze_complexity(self, text: str) -> float:
        """Возвращает оценку сложности текста от 0 (простой) до 1."""
        if not text.strip():
            return 0.0
        ld = self._lexical_density(text)
        sc = self._sentence_complexity(text)
        if self.complexity_measure == "lexical_density":
            return ld
        if self.complexity_measure == "sentence_length":
            return sc
        return (ld + sc) / 2  # combined

    # ── основной метод ─────────────────────────────────────

    def split_text(self, text: str) -> list[str]:
        """Разбивает текст на чанки с адаптивным размером."""
        if not text:
            return []

        sentences = _split_sentences(text)
        chunks: list[str] = []
        current: list[str] = []
        current_size = 0
        running_complexity = 0.5

        for sentence in sentences:
            slen = len(sentence)
            if slen == 0:
                continue

            sc = self.analyze_complexity(sentence)
            running_complexity = (running_complexity + sc) / 2 if current else sc

            # Целевой размер: чем сложнее — тем меньше чанк
            target = self.max_chunk_size - running_complexity * (self.max_chunk_size - self.min_chunk_size)
            target_overlap = self.min_chunk_overlap + running_complexity * (
                self.max_chunk_overlap - self.min_chunk_overlap
            )

            if current_size + slen > target and current:
                chunks.append(" ".join(current))

                # Overlap: берём последние предложения предыдущего чанка
                overlap: list[str] = []
                overlap_size = 0
                for prev in reversed(current):
                    if overlap_size + len(prev) <= target_overlap:
                        overlap.insert(0, prev)
                        overlap_size += len(prev)
                    else:
                        break

                current = overlap + [sentence]
                current_size = sum(len(s) for s in current)
            else:
                current.append(sentence)
                current_size += slen

        if current:
            chunks.append(" ".join(current))

        return chunks


def adaptive_chunking(
    text: str,
    min_chunk_size: int = 300,
    max_chunk_size: int = 1000,
    min_chunk_overlap: int = 30,
    max_chunk_overlap: int = 150,
    complexity_measure: str = "combined",
    metadata: dict | None = None,
) -> list[Document]:
    """
    Адаптивный чанкинг: размер чанка зависит от сложности текста.

    Простые участки (перечисления, короткие факты) получают
    более крупные чанки, а плотные аналитические фрагменты —
    мелкие, чтобы повысить точность поиска.

    Сложность оценивается по двум метрикам:

    * **lexical_density** — доля уникальных слов,
    * **sentence_length** — средняя длина предложения,
    * **combined** (по умолчанию) — среднее обеих.

    Args:
        text: исходный текст документа.
        min_chunk_size: минимальный размер (для самых сложных участков).
        max_chunk_size: максимальный размер (для простых участков).
        min_chunk_overlap: минимальное перекрытие.
        max_chunk_overlap: максимальное перекрытие (для сложных участков).
        complexity_measure: ``"lexical_density"`` | ``"sentence_length"``
                           | ``"combined"``.
        metadata: метаданные документа-источника.

    Returns:
        Список ``Document`` с метаданными ``text_complexity``,
        ``target_chunk_size``, ``strategy``.
    """
    metadata = metadata or {}

    splitter = _AdaptiveTextSplitter(
        min_chunk_size=min_chunk_size,
        max_chunk_size=max_chunk_size,
        min_chunk_overlap=min_chunk_overlap,
        max_chunk_overlap=max_chunk_overlap,
        complexity_measure=complexity_measure,
    )

    chunks = splitter.split_text(text)

    documents: list[Document] = []
    for i, chunk in enumerate(chunks):
        complexity = splitter.analyze_complexity(chunk)
        target = max_chunk_size - complexity * (max_chunk_size - min_chunk_size)

        doc = Document(
            page_content=chunk,
            metadata={
                **metadata,
                "chunk_id": i,
                "total_chunks": len(chunks),
                "chunk_size": len(chunk),
                "strategy": "adaptive",
                "text_complexity": round(complexity, 3),
                "target_chunk_size": round(target),
            },
        )
        documents.append(doc)

    return documents


# ────────────────────────────────────────────────────────────
# 4. Context-Enriched Chunking
# ────────────────────────────────────────────────────────────


def _summarize_text(text: str, client, model: str) -> str:
    """Генерирует краткое саммари текста через LLM."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты — ассистент для суммаризации. Дай краткое резюме текста в 1–2 предложениях на русском."
                ),
            },
            {"role": "user", "content": text},
        ],
        temperature=0.1,
        max_tokens=150,
    )
    return response.choices[0].message.content.strip()


def context_enriched_chunking(
    text: str,
    chunk_size: int = 500,
    chunk_overlap: int = 50,
    window_size: int = 1,
    metadata: dict | None = None,
    client=None,
    model: str | None = None,
) -> list[Document]:
    """
    Чанкинг с обогащением контекстом соседних чанков.

    Каждый чанк получает **контекст** — краткое саммари соседних
    фрагментов (``window_size`` чанков слева и справа).  Это помогает
    модели при генерации понимать, *в каком контексте* находится
    данный фрагмент.

    Если передан ``client`` (OpenAI-совместимый) и ``model`` —
    контекст формируется через LLM-суммаризацию.  Иначе используется
    простая эвристика: первое предложение каждого соседнего чанка.

    Args:
        text: исходный текст документа.
        chunk_size: целевой размер базового чанка.
        chunk_overlap: перекрытие между базовыми чанками.
        window_size: сколько соседних чанков брать для контекста
                     (по каждую сторону).
        metadata: метаданные документа-источника.
        client: OpenAI-совместимый клиент (опционально).
        model: имя модели для суммаризации (опционально).

    Returns:
        Список ``Document``.  Поле ``page_content`` содержит
        обогащённый текст вида ``"Context: …\\n\\nContent: …"``,
        а в ``metadata`` — информация об окне и типе контекста.
    """
    metadata = metadata or {}
    use_llm = client is not None and model is not None

    # Базовое разбиение — рекурсивный сплиттер
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    base_chunks = splitter.split_text(text)

    # Простая fallback-суммаризация (без LLM)
    def _fallback_summary(t: str) -> str:
        first = t.split(".")[0]
        return first[:120].strip() + ("…" if len(first) > 120 else ".")

    documents: list[Document] = []

    for i, chunk in enumerate(base_chunks):
        win_start = max(0, i - window_size)
        win_end = min(len(base_chunks), i + window_size + 1)

        # Собираем тексты соседних чанков (без текущего)
        neighbors = [base_chunks[j] for j in range(win_start, win_end) if j != i]
        neighbor_text = " ".join(neighbors)

        # Формируем контекст
        if neighbors:
            if use_llm:
                try:
                    context = _summarize_text(neighbor_text, client, model)
                    ctx_type = "llm_summary"
                except Exception:
                    context = _fallback_summary(neighbor_text)
                    ctx_type = "fallback"
            else:
                context = _fallback_summary(neighbor_text)
                ctx_type = "heuristic"
            enriched = f"Context: {context}\n\nContent: {chunk}"
        else:
            context = ""
            ctx_type = "none"
            enriched = chunk

        doc = Document(
            page_content=enriched,
            metadata={
                **metadata,
                "chunk_id": i,
                "total_chunks": len(base_chunks),
                "chunk_size": len(chunk),
                "enriched_size": len(enriched),
                "strategy": "context-enriched",
                "context_type": ctx_type,
                "window_start": win_start,
                "window_end": win_end - 1,
            },
        )
        documents.append(doc)

    return documents
