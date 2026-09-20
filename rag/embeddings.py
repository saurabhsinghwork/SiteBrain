# Future responsibility:
# Create vector embeddings for project chunks using a free/local embedding model.
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def load_embedding_model() -> SentenceTransformer:
    model = SentenceTransformer(MODEL_NAME)
    return model

def create_embeddings(model:SentenceTransformer, chunks: list[dict],) -> list[list[float]] :
    text = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts)
    return embeddings.tolist()
