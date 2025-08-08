import fitz  # PyMuPDF
import unicodedata
import re

def parse_resume(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def clean_text(text):
    replacements = {
        'Ɵ': 't',
        'Ō': 'O',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)
    lines = [line.strip() for line in text.splitlines()]
    cleaned_text = "\n".join(lines)

    return cleaned_text
