from __future__ import annotations

import re
from typing import Any


YEAR_PATTERN = re.compile(r"\b(2019|2025)\b")


class Retriever:
    """
    Простой semantic retriever поверх LanceDB.

    Эксперимент A:
    - если в вопросе явно найден год 2019 или 2025,
      сначала ищем только по этому году
    - если по фильтру ничего не найдено, делаем fallback
      на обычный поиск без year-filter

    Эксперимент B:
    - запрашиваем из БД больше кандидатов
    - exact dedup по тексту
    - собираем один финальный список чанков
    - жестко ограничиваем финальный список по max_returned_chunks
    - бюджет считаем по реальному контексту с оберткой
    - если текущий чанк не влезает, пробуем следующий
    """

    def __init__(
        self,
        table,
        embedder,
        top_k: int = 20,
        max_context_chars: int = 6000,
        max_returned_chunks: int = 5,
    ) -> None:
        self.table = table
        self.embedder = embedder
        self.top_k = top_k
        self.max_context_chars = max_context_chars
        self.max_returned_chunks = max_returned_chunks

    @staticmethod
    def _normalize_row(row: dict[str, Any]) -> dict[str, Any]:
        distance = row.get("_distance", row.get("distance", 0.0))

        return {
            "text": str(row.get("text", "")).strip(),
            "chunk_id": row.get("chunk_id"),
            "year": int(row.get("year", 0)),
            "distance": float(distance),
            "document_name": str(row.get("document_name", "")),
            "source": str(row.get("source", "")),
            "chunk_index": int(row.get("chunk_index", 0)),
        }

    @staticmethod
    def extract_year_from_question(question: str) -> int | None:
        match = YEAR_PATTERN.search(question)
        if match is None:
            return None
        return int(match.group(1))

    def _search_without_filter(
        self,
        query_vector: list[float],
        limit: int,
    ) -> list[dict[str, Any]]:
        return self.table.search(query_vector).limit(limit).to_list()

    def _search_with_year_filter(
        self,
        query_vector: list[float],
        year: int,
        limit: int,
    ) -> list[dict[str, Any]]:
        return self.table.search(query_vector).where(f"year = {year}").limit(limit).to_list()

    def _search_rows(
        self,
        query_vector: list[float],
        question: str,
        limit: int,
    ) -> list[dict[str, Any]]:
        expected_year = self.extract_year_from_question(question)

        if expected_year is None:
            return self._search_without_filter(query_vector, limit)

        try:
            filtered_rows = self._search_with_year_filter(query_vector, expected_year, limit)
        except Exception:
            filtered_rows = []

        if filtered_rows:
            return filtered_rows

        return self._search_without_filter(query_vector, limit)

    @staticmethod
    def format_chunk_for_context(chunk: dict[str, Any], idx: int) -> str:
        return f"[Фрагмент {idx} | год {chunk['year']} | chunk_id={chunk['chunk_id']}]\n{chunk['text']}"

    @classmethod
    def build_context(cls, chunks: list[dict[str, Any]]) -> str:
        parts = [
            cls.format_chunk_for_context(chunk, idx)
            for idx, chunk in enumerate(chunks, start=1)
        ]
        return "\n\n".join(parts)

    def retrieve(
        self,
        question: str,
        top_k: int | None = None,
        max_context_chars: int | None = None,
    ) -> list[dict[str, Any]]:
        limit = top_k if top_k is not None else self.top_k
        char_limit = max_context_chars if max_context_chars is not None else self.max_context_chars

        query_vector = self.embedder.embed_query(question)
        raw_rows = self._search_rows(
            query_vector=query_vector,
            question=question,
            limit=limit,
        )

        results: list[dict[str, Any]] = []
        seen_texts: set[str] = set()
        total_chars = 0

        for raw_row in raw_rows:
            row = self._normalize_row(raw_row)
            text = row["text"]

            if not text:
                continue
            if text in seen_texts:
                continue

            next_idx = len(results) + 1
            rendered_chunk = self.format_chunk_for_context(row, next_idx)
            separator_len = 2 if results else 0
            next_total = total_chars + separator_len + len(rendered_chunk)

            if next_total > char_limit:
                continue

            seen_texts.add(text)
            results.append(row)
            total_chars = next_total

            if len(results) >= self.max_returned_chunks:
                break

        return results