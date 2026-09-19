# Future responsibility:
# Inspect extracted project files and keep useful source/config/docs while
# skipping only clearly generated, binary, duplicate, cache, or irrelevant files.
# It will also record what was included and skipped.
from pathlib import Path

REPORT_DIR= Path("rag/reports")

IGNORED_DIRECTORIES= {
    ".git",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".next",
    "dist",
    "build",
}

IGNORED_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".ico",
    ".webp",
    ".svg",
    ".mp3",
    ".mp4",
    ".wav",
    ".avi",
    ".mov",
    ".pdf",
    ".zip",
    ".tar",
    ".gz",
    ".woff",
    ".woff2",
    ".ttf",
    ".eot",
    ".exe",
    ".dll",
}

def is_ignored_path(file_path:Path) -> bool:
    return any(
        part in IGNORED_DIRECTORIES
        for part in file_path.parts
    )

def scan_project(project_path:Path)-> list[Path]:
    useful_files= []
    for file_path in project_path.rglob("*"):
        if not file_path.is_file():
            continue
        if is_ignored_path(file_path):
            continue
        useful_files.append(file_path)
        if has_ignored_extension(file_path):
            continue
    return useful_files    

def has_ignored_extension(file_path:Path) -> bool:
    return file_path.suffix.lower() in IGNORED_EXTENSIONS

def create_scan_report(project_path:Path, useful_files: list[Path]) -> None:
    REPORT_DIR.mkdir(parents=True,exist_ok=True)
    report_path= REPORT_DIR/"scan_report.txt"

    all_files= [
        file_path
        for file_path in project_path.rglob("*")
        if file_path.is_file()
    ]

    with report_path.open("w", encoding="utf-8") as report:
        report.write("INCLUDED FILES\n")
        report.write("====================\n")

        for file_path in useful_files:
            report.write(f"{file_path}\n")

        report.write("\nSKIPPED FILES\n")
        report.write("====================\n")

        for file_path in all_files:
            if file_path not in useful_files:
                report.write(f"{file_path}\n")
                         