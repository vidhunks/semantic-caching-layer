from fastapi import FastAPI

app = FastAPI(
    title="Semantic Cache API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Semantic Cache API is running"
        
    }

@app.get("/health")
def health():
    return{
        "status":"healthy"
    }