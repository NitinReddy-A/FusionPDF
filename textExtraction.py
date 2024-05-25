import fitz  # PyMuPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import io
import os

# Map extracted font names to ReportLab standard fonts
font_map = {
    'Georgia-Bold': 'Helvetica-Bold',
    'Georgia': 'Helvetica',
    # You can map more fonts as needed or use a default font
}

def extract_content(pdf_path):
    doc = fitz.open(pdf_path)
    content_list = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("dict")
        images = page.get_images(full=True)
        
        content_list.append({"page_num": page_num, "text": text, "images": images})
    
    return content_list

def create_new_pdf(new_pdf_path, content_list, original_pdf_path):
    doc = fitz.open(original_pdf_path)
    c = canvas.Canvas(new_pdf_path, pagesize=letter)
    
    for page_num, content in enumerate(content_list):
        # Start a new page in the new PDF for each page in the original PDF
        if page_num > 0:
            c.showPage()
        
        text = content["text"]
        
        for block in text["blocks"]:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        x, y = span["bbox"][0], span["bbox"][1]
                        font_size = span["size"]
                        font_name = span["font"]
                        font_name = font_map.get(font_name, 'Helvetica')
                        
                        c.setFont(font_name, font_size)
                        c.drawString(x, letter[1] - y, span["text"])

    c.save()



pdf_path = r"Path.pdf"
new_pdf_path = r"pdf_file.pdf"
content_list = extract_content(pdf_path)
create_new_pdf(new_pdf_path, content_list,pdf_path)
