from pypdf import PdfReader

MAX_CHARS = 3500

def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text.strip()[:MAX_CHARS]
