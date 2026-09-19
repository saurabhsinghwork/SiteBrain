# Future responsibility:
# Break useful website project content into small meaningful chunks
# that can later be embedded and searched.
from pathlib import Path

def read_file_text(file_path:Path) -> str:
    return file_path.read_text(
        encoding="utf-8",
        errors="ignore",
    ).strip()

def split_text(text: str, chunk_size: int= 1000, overlap: int= 200) -> list[str]:
    chunks= []
    start= 0
    while start < len(text):
        end= start + chunk_size
        chunk= text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start= end - overlap
    return chunks

def chunk_file(file_path: Path) -> list[dict]:
    text = read_file_text(file_path)
    if not text:
        return []

    text_chunks= split_text(text)
    chunks= []

    for index, text_chunk in enumerate(text_chunks):
        chunks.append(
            {
                "text": text_chunk,
                "source": str(file_path),
                "chunk_index": index,
            }
        )        
    return chunks

def chunk_project(file_paths: list[Path]) -> list[dict]:
    all_chunks= []

    for file_path in file_paths:
        file_chunks= chunk_file(file_path)
        all_chunks.extend(file_chunks)
    return all_chunks    