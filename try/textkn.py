import pymupdf

def extract_pdf_text_font_adjust(pdf_path):
    doc = pymupdf.open(pdf_path)
    full_text = ""

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        full_text += text + "\n\n"
    
    return full_text

pdf_path = r"TranslatedOutput.pdf"
full_text = extract_pdf_text_font_adjust(pdf_path)
print(full_text)
