from __future__ import annotations

import re
from typing import Any

from rank_bm25 import BM25Okapi


# Хардкод под текущий датасет (отчёты только 2019 и 2025).
# Если корпус расширится — заменить на \b(?:19|20)\d{2}\b и валидировать
# найденный год по списку доступных в БД.
YEAR_PATTERN = re.compile(r"(?<!\d)(2019|2025)(?!\d)")
TOKEN_PATTERN = re.compile(r"[\w]+")


class Retriever:
    """
    Semantic retriever поверх LanceDB с soft BM25 reranking.

    Эксперимент A:
    - year-aware фильтрация по годам 2019/2025

    Эксперимент B:
    - один финальный список для LLM и retrieved_chunks
    - бюджет 6000 символов с обёрткой
    - continue вместо break при упаковке

    Эксперимент D:
    - большие чанки (1500/400), max_returned_chunks=3

    Эксперимент E.3 (dense-anchored BM25 rerank):
    - dense top-N остаётся основой ранжирования
    - BM25 строится только по этим N кандидатам, не по всей базе
    - финальный score = 0.85 * dense_score + 0.15 * bm25_score
    - BM25 работает только как мягкий tie-breaker внутри dense top-N
    """

    DENSE_WEIGHT = 0.85
    BM25_WEIGHT = 0.15

    def __init__(
        self,
        table,
        embedder,
        top_k: int = 20,
        max_context_chars: int = 6000,
        max_returned_chunks: int = 4,
        llm_client: Any = None,
        llm_model: str | None = None,
        llm_filter_candidates: int = 8,
    ) -> None:
        self.table = table
        self.embedder = embedder
        self.top_k = top_k
        self.max_context_chars = max_context_chars
        self.max_returned_chunks = max_returned_chunks
        self.llm_client = llm_client
        self.llm_model = llm_model
        self.llm_filter_candidates = llm_filter_candidates

    @staticmethod
    def _tokenize(text: str) -> list[str]:
        """Та же токенизация, что в evaluation.py — для согласованности."""
        return TOKEN_PATTERN.findall(text.lower())

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
    def _min_max_normalize(values: list[float]) -> list[float]:
        """
        Нормализация в [0, 1]. Если все значения одинаковые — возвращаем нули.
        """
        if not values:
            return []
        lo = min(values)
        hi = max(values)
        if hi - lo < 1e-12:
            return [0.0] * len(values)
        return [(v - lo) / (hi - lo) for v in values]

    def _rerank_with_bm25_bonus(
        self,
        rows: list[dict[str, Any]],
        question: str,
    ) -> list[dict[str, Any]]:
        """
        Dense-anchored rerank с мягким BM25 бонусом.

        Алгоритм:
        1. dense_score = 1 - normalized(distance), то есть чем меньше distance, тем больше score
        2. bm25_score = normalized(BM25 score по этому вопросу среди этих же N кандидатов)
        3. final = 0.85 * dense_score + 0.15 * bm25_score

        Важно: BM25 строится только по тем N чанкам, которые dense уже отдал.
        Никакие новые чанки в финальный список попасть не могут.
        Это ключевое свойство dense-anchored подхода.
        """
        if not rows:
            return rows

        # Если кандидат один — никакого rerank-а не нужно
        if len(rows) == 1:
            return rows

        # 1. Dense score: чем меньше distance, тем больше score
        distances = [row["distance"] for row in rows]
        normalized_distances = self._min_max_normalize(distances)
        dense_scores = [1.0 - d for d in normalized_distances]

        # 2. BM25 score только по этим кандидатам
        tokenized_corpus = [self._tokenize(row["text"]) for row in rows]
        bm25 = BM25Okapi(tokenized_corpus)
        tokenized_query = self._tokenize(question)
        raw_bm25_scores = bm25.get_scores(tokenized_query).tolist()
        bm25_scores = self._min_max_normalize(raw_bm25_scores)

        # 3. Финальный комбинированный score
        for row, ds, bs in zip(rows, dense_scores, bm25_scores):
            row["_dense_score"] = ds
            row["_bm25_score"] = bs
            row["_final_score"] = self.DENSE_WEIGHT * ds + self.BM25_WEIGHT * bs

        # Сортируем по убыванию финального score
        rows_sorted = sorted(rows, key=lambda r: r["_final_score"], reverse=True)
        return rows_sorted


    _LLM_FILTER_PROMPT = """Ты — эксперт по отбору документов для RAG-системы.

    Тебе дан вопрос пользователя и {n} фрагментов документов с индексами.
    Твоя задача — выбрать фрагменты, которые содержат фактические формулировки,
    пригодные для ответа на вопрос.

    Правила отбора:
    1. Выбирай фрагмент, если он содержит конкретные данные, цитаты или утверждения,
    которые прямо отвечают на вопрос (даже частично).
    2. НЕ выбирай фрагменты, которые просто упоминают тему вопроса без конкретики.
    3. НЕ выбирай дубликаты: если два фрагмента говорят одно и то же — оставь один.
    4. Если полезных фрагментов меньше {max_keep} — верни только их.
    5. Если полезных фрагментов больше {max_keep} — верни {max_keep} самых информативных.
    6. Если ни один фрагмент не подходит — верни первые {max_keep} по порядку.

    Верни ТОЛЬКО JSON в формате:
    {{"selected": [индексы через запятую]}}

    Никакого текста до или после JSON.

    ВОПРОС:
    {question}

    ФРАГМЕНТЫ:
    {fragments}"""


    def _llm_filter(
        self,
        question: str,
        candidates: list[dict[str, Any]],
        max_keep: int,
        client: Any,
        model: str,
    ) -> list[dict[str, Any]]:
        """
        LLM-фильтрация кандидатов. Один вызов на все кандидаты.

        Возвращает подмножество candidates в порядке, выданном LLM.
        Fallback: при любой ошибке возвращает первые max_keep кандидатов.
        """
        import json

        if not candidates:
            return []
        if len(candidates) <= max_keep:
            return candidates

        # Формируем нумерованный список фрагментов
        fragments_text = "\n\n".join(
            f"[{idx}] {cand['text'][:800]}"  # обрезаем длинные чанки в промпте
            for idx, cand in enumerate(candidates)
        )

        prompt = self._LLM_FILTER_PROMPT.format(
            n=len(candidates),
            max_keep=max_keep,
            question=question,
            fragments=fragments_text,
        )

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                response_format={"type": "json_object"},
            )
            raw = response.choices[0].message.content or "{}"
            data = json.loads(raw)
            selected_indices = data.get("selected", [])

            # Валидация: индексы должны быть int и в диапазоне
            valid_indices = [
                int(i) for i in selected_indices
                if isinstance(i, (int, str)) and str(i).isdigit() and 0 <= int(i) < len(candidates)
            ]

            if not valid_indices:
                return candidates[:max_keep]

            # Убираем дубликаты, сохраняя порядок LLM
            seen: set[int] = set()
            unique_indices = []
            for i in valid_indices:
                if i not in seen:
                    seen.add(i)
                    unique_indices.append(i)

            result = [candidates[i] for i in unique_indices[:max_keep]]
            return result if result else candidates[:max_keep]

        except Exception:
            # Fallback: берём первые max_keep кандидатов (как без фильтра)
            return candidates[:max_keep]



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

        # 1. Dense retrieval (с year-фильтром и fallback)
        query_vector = self.embedder.embed_query(question)
        raw_rows = self._search_rows(
            query_vector=query_vector,
            question=question,
            limit=limit,
        )

        # 2. Нормализация
        normalized_rows = [self._normalize_row(raw_row) for raw_row in raw_rows]
        normalized_rows = [row for row in normalized_rows if row["text"]]

        # 3. Dense-anchored BM25 rerank внутри top-N
        reranked_rows = self._rerank_with_bm25_bonus(normalized_rows, question)

        # 3.5 LLM-фильтрация (если включена)
        if self.llm_client is not None and self.llm_model is not None and reranked_rows:
            # Берём top-N из BM25-реранка для LLM на вход
            top_candidates = reranked_rows[:self.llm_filter_candidates]
            filtered = self._llm_filter(
                question=question,
                candidates=top_candidates,
                max_keep=self.max_returned_chunks,
                client=self.llm_client,
                model=self.llm_model,
            )
            # LLM уже отдала нужное количество, но для совместимости с упаковщиком
            # кладём их в начало, оставшиеся как backup (на случай если упаковщик
            # выбросит кого-то по бюджету)
            filtered_ids = {id(r) for r in filtered}
            backup = [r for r in reranked_rows if id(r) not in filtered_ids]
            reranked_rows = filtered + backup

        # 4. Упаковка с дедупом и бюджетом (как в эксперименте B)
        results: list[dict[str, Any]] = []
        seen_texts: set[str] = set()
        total_chars = 0

        for row in reranked_rows:
            text = row["text"]
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