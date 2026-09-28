# Future responsibility:
# Search the vector store for chunks that are most relevant to a visitor's query.
import chromadb
from sentence_transformers import SentenceTransformer

def retrieve_chunks(collection, model:SentenceTransformer, query:str, top_k:int = 5) -> list[dict]:
    query_embedding = model.encode(query).tolist()
    results = collection.query(
        query_embeddings = [query_embedding],
        n_results = top_k,
    )
    retrieved_chunks = []
    for index in range(len(results["documents"][0])):
        retrieved_chunks.append(
            {
            "text" : results["documents"][0][index],
            "source" : results["metadatas"][0][index]["source"],
            "chunk_index" : results["metadatas"][0][index]["chunk_index"],
            }
        )    
    return retrieved_chunks