"""
Input:pdf
Output: text
Assumption: the pdf is not scanned, it is a text-based pdf
"""

#libraries
import fitz

def open_pdf(pdf_path):

    return(fitz.open(pdf_path))

def extract_text_from_pdf(pdf_path):

    pdf=open_pdf(pdf_path)
    text=[]
    for page in pdf:
        text.append(page.get_text())

    return text


