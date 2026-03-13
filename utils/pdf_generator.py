from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io


def create_resume_pdf(text):

    buffer = io.BytesIO()

    pdf = canvas.Canvas(buffer, pagesize=letter)

    y = 750

    for line in text.split("\n"):

        pdf.drawString(50, y, line)

        y -= 20

        if y < 50:
            pdf.showPage()
            y = 750

    pdf.save()

    buffer.seek(0)

    return buffer