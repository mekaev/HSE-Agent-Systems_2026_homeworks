"""
Тут описываете своего RAG агента или RAG пайплайн (как хотите, без разницы)
Главное чтобы на каждый запрос Ваш RAG агент \ пайплайн возвращал объект
RAGAgentAnswer 
Это контракт который ожидает модуль evaluation для оценки 
"""

from __future__ import annotations

from typing import Any, Callable

from pydantic import BaseModel, Field

from embedder import DEFAULT_EMBEDDING_MODEL, SimpleEmbedder
from retriever import Retriever


class Chunk(BaseModel):
    """Один найденный фрагмент из векторного хранилища."""

    text: str
    chunk_id: str | int
    year: int
    distance: float


class RAGAgentAnswer(BaseModel):
    """
    Контракт ответа RAG-агента для системы оценки.

    Это единый формат, который позволяет считать все метрики:
    - Retrieval-метрики (Precision@K, Recall@K, MRR, MAP, NDCG) — по retrieved_chunks
    - Generation-метрики (Faithfulness) — по answer + retrieved_chunks
    """

    dataset_row_id: str | None = None
    answer: str
    retrieved_chunks: list[Chunk] | None = None


TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "retrieve_context",
            "description": "Ищет релевантные фрагменты в векторной базе по вопросу пользователя.",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "Вопрос пользователя",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Сколько top-k результатов запросить из базы",
                        "default": 10,
                    },
                    "max_context_chars": {
                        "type": "integer",
                        "description": "Максимальный суммарный размер контекста в символах",
                        "default": 6000,
                    },
                },
                "required": ["question"],
            },
        },
    }
]


def get_tool_functions(table, client) -> dict[str, Callable[..., list[dict[str, Any]]]]:
    """
    Ноутбук ожидает эту функцию.
    Возвращаем не сложный tools-agent, а один retrieval tool.
    """
    embedder = SimpleEmbedder(
        client=client,
        model=DEFAULT_EMBEDDING_MODEL,
    )
    retriever = Retriever(
        table=table,
        embedder=embedder,
        top_k=20,
        max_context_chars=6000,
        max_returned_chunks=5,
    )

    return {
        "retrieve_context": retriever.retrieve,
    }


class RAGAgent:
    """
    Внешне совместим с notebook, внутри - обычный baseline RAG.
    """

    def __init__(
        self,
        client,
        model: str,
        tools_schema: list[dict[str, Any]] | None = None,
        tool_functions: dict[str, Callable[..., Any]] | None = None,
    ) -> None:
        self.client = client
        self.model = model
        self.tools_schema = tools_schema or []
        self.tool_functions = tool_functions or {}

    def _retrieve(self, question: str) -> list[dict[str, Any]]:
        retrieve_fn = self.tool_functions.get("retrieve_context")
        if retrieve_fn is None:
            raise ValueError("В tool_functions не найдена функция 'retrieve_context'")
        return retrieve_fn(question=question, top_k=20, max_context_chars=6000)

    @staticmethod
    def _build_context(chunks: list[dict[str, Any]]) -> str:
        return Retriever.build_context(chunks)

    def _generate_answer(self, question: str, context: str) -> str:
        system_prompt = (
            "Ты отвечаешь только по предоставленному контексту из документов.\n"
            "Правила:\n"
            "1. Не добавляй факты от себя.\n"
            "2. Если в контексте недостаточно данных, честно скажи об этом.\n"
            "3. Отвечай кратко, по-русски, по существу.\n"
            "4. Не упоминай, что ты модель или ассистент.\n"
        )

        user_prompt = (
            f"Вопрос:\n{question}\n\n"
            f"Контекст:\n{context}\n\n"
            "Сформулируй ответ только на основе контекста."
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0,
        )

        return (response.choices[0].message.content or "").strip()

    @staticmethod
    def _to_chunks(items: list[dict[str, Any]]) -> list[Chunk]:
        return [
            Chunk(
                text=item["text"],
                chunk_id=item["chunk_id"],
                year=int(item["year"]),
                distance=float(item["distance"]),
            )
            for item in items
        ]

    def run(
        self,
        question: str,
        verbose: bool = False,
        dataset_row_id: str | None = None,
    ) -> RAGAgentAnswer:
        retrieved_items = self._retrieve(question)

        if verbose:
            print(f"[RAG] Найдено чанков: {len(retrieved_items)}")

        if not retrieved_items:
            return RAGAgentAnswer(
                dataset_row_id=str(dataset_row_id) if dataset_row_id is not None else None,
                answer="В документах не найдено достаточно данных для ответа на вопрос.",
                retrieved_chunks=[],
            )

        context = self._build_context(retrieved_items)
        answer = self._generate_answer(question, context)
        chunks = self._to_chunks(retrieved_items)

        return RAGAgentAnswer(
            dataset_row_id=str(dataset_row_id) if dataset_row_id is not None else None,
            answer=answer,
            retrieved_chunks=chunks,
        )