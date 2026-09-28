# Future responsibility:
# Coordinate the complete indexing flow:
# ZIP -> extract -> scan -> chunk -> embed -> vector store -> report.
from rag.zip_loader import load_project_zip
from rag.scanner import scan_project, create_scan_report
from rag.chunker import chunk_project
from rag.embeddings import load_embedding_model, create_embeddings
from rag.store import create_chromadb_client, get_collection, store_chunks

def build_rag_index() -> None:
    project_path = load_project_zip()
    useful_files = scan_project(project_path)
    create_scan_report(project_path, useful_files)
    chunks = chunk_project(useful_files)
    model = load_embedding_model()
    embeddings = create_embeddings(model, chunks)
    client = create_chromadb_client()
    collection = get_collection(client, reset=True)
    store_chunks(collection, chunks, embeddings)