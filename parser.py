from pathlib import Path

def extract_text(path, suffix):
    suffix = suffix.lower()
    if suffix == ".txt":
        return Path(path).read_text(encoding="utf-8", errors="ignore")
    if suffix == ".docx":
        try:
            from docx import Document
        except ImportError:
            raise ValueError("DOCX support is unavailable. Install python-docx.")
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs)
    if suffix == ".pdf":
        try:
            import fitz
        except ImportError:
            raise ValueError("PDF support is unavailable. Install PyMuPDF.")
        text_parts = []
        with fitz.open(path) as pdf:
            for page in pdf:
                text_parts.append(page.get_text("text"))
        return "\n".join(text_parts)
    raise ValueError("Unsupported file type.")
