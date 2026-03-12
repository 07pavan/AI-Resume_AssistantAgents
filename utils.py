from pypdf import PdfReader
import docx

MAX_CHARS = 3000   # prevents huge prompts

def read_resume(file_path):

    text = ""

    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"

    # limit text size
    return text[:MAX_CHARS]