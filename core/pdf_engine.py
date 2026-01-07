from pypdf import PdfReader

MAX_CHARS = 3500

def extract_text(file):
    reader = PdfReader(file)
    text = []

    for page in reader.pages:
        try:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
        except:
            continue

    final_text = "\n".join(text)
    final_text = " ".join(final_text.split())

    if not final_text.strip():
        return "No readable text found. The resume may be scanned."

    return final_text[:MAX_CHARS]
