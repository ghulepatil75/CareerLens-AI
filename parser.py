import os
import re
import zipfile
import xml.etree.ElementTree as ET

def extract_docx(path):
    with zipfile.ZipFile(path, "r") as z:
        xml = z.read("word/document.xml")

    root = ET.fromstring(xml)

    texts = []
    for element in root.iter():
        if element.tag.endswith("}t") and element.text:
            texts.append(element.text)

    return "\n".join(texts)

def extract_text(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".docx":
        return extract_docx(file_path)

    if extension == ".txt":
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    if extension == ".pdf":
        raise ValueError(
            "PDF analysis is disabled in the lightweight Termux version. "
            "Please upload a DOCX resume."
        )

    raise ValueError("Unsupported file format. Please upload DOCX.")
