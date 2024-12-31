import PyPDF2

def extract_text_from_pdf(file_path):
    """
    Extrae el texto de un archivo PDF.
    """
    text = ""
    with open(file_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()
    return text
