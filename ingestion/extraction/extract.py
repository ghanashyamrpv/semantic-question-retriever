"""
Input:pdf
Output: json
Assumption: orchastrate the extraction process by determining whether to use OCR or text-based parsing based on the type of PDF, and then applying regex to extract structured information and store it in a json format
"""
#libraries
from pathlib import Path
from extraction_package import parser

path=Path(__file__).parent.parent.parent/"data"/"raw"/"isi_a_2026.pdf"

lst=parser.extract_text_from_pdf(path)
print(lst[0])

