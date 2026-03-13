import pypdf
import docx


def parse_pdf(file):

    try:
        reader = pypdf.PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text

    except Exception as e:
        return f"PDF parsing error: {e}"


def parse_docx(file):

    try:
        doc = docx.Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])
        return text

    except Exception as e:
        return f"DOCX parsing error: {e}"


def extract_resume_text(uploaded_file):

    filename = uploaded_file.name

    if filename.endswith(".pdf"):
        return parse_pdf(uploaded_file)

    elif filename.endswith(".docx"):
        return parse_docx(uploaded_file)

    else:
        return "Unsupported file format"