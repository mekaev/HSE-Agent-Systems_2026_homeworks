"""
Тут описываете своего RAG агента или RAG пайплайн (как хотите, без разницы)
Главное чтобы на каждый запрос Ваш RAG агент \ пайплайн возвращал объект
RAGAgentAnswer 
Это контракт который ожидает модуль evaluation для оценки 
"""

from pydantic import BaseModel

class Chunk(BaseModel):
    """Один найденный фрагмент из векторного хранилища."""

    text: str
    chunk_id: int
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