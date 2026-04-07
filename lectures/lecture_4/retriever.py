from __future__ import annotations

from typing import Any


class Retriever:
    """
    Простой semantic retriever поверх LanceDB.
    """

    def __init__(
        self,
        table,
        embedder,
        top_k: int = 10,
        max_context_chars: int = 6000,
    ) -> None:
        self.table = table
        self.embedder = embedder
        self.top_k = top_k
        self.max_context_chars = max_context_chars

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

    def retrieve(
        self,
        question: str,
        top_k: int | None = None,
        max_context_chars: int | None = None,
    ) -> list[dict[str, Any]]:
        limit = top_k if top_k is not None else self.top_k
        char_limit = max_context_chars if max_context_chars is not None else self.max_context_chars

        query_vector = self.embedder.embed_query(question)
        raw_rows = self.table.search(query_vector).limit(limit).to_list()

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

            next_total = total_chars + len(text)
            if next_total > char_limit:
                break

            seen_texts.add(text)
            total_chars = next_total
            results.append(row)

        return results

    @staticmethod
    def build_context(chunks: list[dict[str, Any]]) -> str:
        parts: list[str] = []

        for idx, chunk in enumerate(chunks, start=1):
            parts.append(
                f"[Фрагмент {idx} | year={chunk['year']} | chunk_id={chunk['chunk_id']}]\n{chunk['text']}"
            )

        return "\n\n".join(parts)