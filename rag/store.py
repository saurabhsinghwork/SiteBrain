# Future responsibility:
# Create, replace, and access the local vector store generated from the latest ZIP.
import chromadb

def create_chromadb_client() -> chromadb.PersistentClient :
    client = chromadb.PersistentClient(path="rag/vector_store")
    return client

def get_collection(client: chromadb.PersistentClient, reset: bool = False) :
    if reset:
        try:
            client.delete_collection(name = "sitebrain")
        except ValueError:
            pass 
    collection = client.get_or_create_collection(name= "sitebrain")
    return collection

def store_chunks(collection,chunks: list[dict], embeddings:list[list[float]]) -> None:
    ids = []
    documents = []
    metadatas = []
    for index, chunk in enumerate(chunks):
        ids.append(f"chunk-{index}")
        documents.append(chunk["text"])
        metadatas.append(
            {
                "source" : chunk["source"],
                "chunk_index" : chunk["chunk_index"]
            }
        )
    collection.add(
        id = ids,
        documents = documents,
        metadatas = metadatas,
        embeddings = embeddings,
    )    