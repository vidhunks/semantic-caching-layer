from fastapi import FastAPI

from app.services.embedding_service import EmbeddingService


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


@app.get("/test-embedding")
def test_embedding():

    embedding = embedding_service.generate_embedding(
        "How can I get my money back?"
    )

    return {
        "dimensions": len(embedding),
        "first_5_values": embedding[:5].tolist()
    }