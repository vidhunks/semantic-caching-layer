from fastapi import FastAPI

from app.services.embedding_service import EmbeddingService
from app.utils.similarity import cosine_similarity


app = FastAPI(
    title="Semantic Cache API",
    version="1.0.0"
)

embedding_service = EmbeddingService()


@app.get("/")
def root():
    return {
        "message": "Semantic Cache API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/test-similarity")
def test_similarity():

    text_1 = "What is machine learning?"

    text_2 = "Explain artificial intelligence."

    embedding_1 = embedding_service.generate_embedding(text_1)

    embedding_2 = embedding_service.generate_embedding(text_2)

    similarity = cosine_similarity(
        embedding_1,
        embedding_2
    )

    return {
        "text_1": text_1,
        "text_2": text_2,
        "similarity": similarity
    }