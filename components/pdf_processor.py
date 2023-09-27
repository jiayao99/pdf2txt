import os
import PyPDF2

def pdf_to_str(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    total_pages = len(pdf_reader.pages)
    extracted_text = ""
    for page_num in range(total_pages):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()
        page_text = f"\n--- Page {page_num + 1} ---\n{page_text}\n\n"
        extracted_text += page_text
    pdf_file.close()
    print(f"Text has been extracted.")
    return extracted_text
