from pypdf import PdfReader
import docx

def read_resume(file_path):

    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text

    elif file_path.endswith(".docx"):

        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])

        return text