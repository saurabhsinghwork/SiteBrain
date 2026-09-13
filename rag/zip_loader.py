# Future responsibility:
# Find the uploaded latest website repository ZIP and safely extract it
# into rag/extracted/ before indexing begins.
from pathlib import Path
import shutil
import zipfile

UPLOAD_DIR = Path("rag/uploads")
EXTRACT_DIR= Path("rag/extracted")

def load_project_zip() -> Path:
    zip_files= list(UPLOAD_DIR.glob("*.zip"))
    if not zip_files:
        raise FileNotFoundError(
            "No ZIP File found inside rag/uploads."
        )
    if len(zip_files)>1:
        raise ValueError(
            "Please keep only one website project ZIP inside rag/uploads."
        )
    zip_path= zip_files[0]

    if EXTRACT_DIR.exists():
        shutil.rmtree(EXTRACT_DIR)
    EXTRACT_DIR.mkdir(parents=True,exist_ok=True)

    with zipfile.ZipFile(zip_path,"r") as zip_file:
        zip_file.extractall(EXTRACT_DIR)
    return EXTRACT_DIR        