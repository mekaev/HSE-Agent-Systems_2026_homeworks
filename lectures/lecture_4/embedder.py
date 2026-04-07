from __future__ import annotations

from typing import Sequence


DEFAULT_EMBEDDING_MODEL = "openai/text-embedding-3-small"


class SimpleEmbedder:
    """
    Минимальная обертка над OpenAI-compatible embeddings API.
    Один и тот же embedder используется и для документов, и для query.
    """

    def __init__(
        self,
        client,
        model: str = DEFAULT_EMBEDDING_MODEL,
        batch_size: int = 32,
    ) -> None:
        self.client = client
        self.model = model
        self.batch_size = batch_size

    @staticmethod
    def _normalize_text(text: str) -> str:
        text = (text or "").replace("\x00", " ").strip()
        return text if text else " "

    def _embed_batch(self, texts: list[str]) -> list[list[float]]:
        normalized = [self._normalize_text(text) for text in texts]
        response = self.client.embeddings.create(
            model=self.model,
            input=normalized,
        )
        return [list(item.embedding) for item in response.data]

    def embed_documents(self, texts: Sequence[str]) -> list[list[float]]:
        texts = list(texts)
        if not texts:
            return []

        embeddings: list[list[float]] = []
        for start in range(0, len(texts), self.batch_size):
            batch = texts[start : start + self.batch_size]
            embeddings.extend(self._embed_batch(batch))
        return embeddings

    def embed_query(self, text: str) -> list[float]:
        return self._embed_batch([text])[0]