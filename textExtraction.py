import fitz  # PyMuPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Map fonts that might not be found to built-in fonts
font_fallback_map = {
    'Calibri-Bold': 'Helvetica-Bold',
    'Calibri': 'Helvetica',
    'Aptos': 'Helvetica',
    'Aptos,Bold': 'Helvetica-Bold',
    # Add more mappings if necessary
}

builtin_fonts = {
    'Helvetica', 'Helvetica-Bold', 'Helvetica-Oblique', 'Helvetica-BoldOblique',
    'Times-Roman', 'Times-Bold', 'Times-Italic', 'Times-BoldItalic',
    'Courier', 'Courier-Bold', 'Courier-Oblique', 'Courier-BoldOblique'
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

def register_fonts(content_list):
    registered_fonts = set()
    
    for content in content_list:
        text = content["text"]
        for block in text["blocks"]:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        font_name = span["font"]
                        if font_name not in registered_fonts:
                            if font_name in builtin_fonts:
                                registered_fonts.add(font_name)
                            elif font_name in font_fallback_map:
                                registered_fonts.add(font_fallback_map[font_name])
                            else:
                                try:
                                    font_path = f"{font_name}.ttf"  # Path to the TTF file
                                    pdfmetrics.registerFont(TTFont(font_name, font_path))
                                    registered_fonts.add(font_name)
                                except Exception as e:
                                    print(f"Error registering font {font_name}: {e}")
                                    # Use a fallback font
                                    fallback_font = font_fallback_map.get(font_name, 'Helvetica')
                                    if fallback_font not in registered_fonts:
                                        registered_fonts.add(fallback_font)

def get_registered_font(font_name):
    if font_name in pdfmetrics.getRegisteredFontNames():
        return font_name
    return font_fallback_map.get(font_name, 'Helvetica')

def create_new_pdf(new_pdf_path, content_list, original_pdf_path):
    doc = fitz.open(original_pdf_path)
    c = canvas.Canvas(new_pdf_path, pagesize=letter)
    
    for page_num, content in enumerate(content_list):
        if page_num > 0:
            c.showPage()
        
        text = content["text"]
        
        for block in text["blocks"]:
            if "lines" in block:
                for line in block["lines"]:
                    combined_text = ""
                    combined_x = line["spans"][0]["bbox"][0]
                    y0, y1 = line["spans"][0]["bbox"][1], line["spans"][0]["bbox"][3]
                    font_name = get_registered_font(line["spans"][0]["font"])
                    font_size = line["spans"][0]["size"]
                    
                    for span in line["spans"]:
                        current_font_name = get_registered_font(span["font"])
                        current_font_size = span["size"]
                        
                        if current_font_name != font_name or current_font_size != font_size:
                            c.setFont(font_name, font_size)
                            y = letter[1] - y1
                            c.drawString(combined_x, y, combined_text)
                            combined_text = ""
                            combined_x = span["bbox"][0]
                            y0, y1 = span["bbox"][1], span["bbox"][3]
                            font_name = current_font_name
                            font_size = current_font_size
                        
                        combined_text += span["text"]
                    
                    if combined_text:
                        c.setFont(font_name, font_size)
                        y = letter[1] - y1
                        c.drawString(combined_x, y, combined_text)

    c.save()

pdf_path = r"C:\Users\len\OneDrive\Desktop\Repo\FusionPDF\try\demo.pdf"
new_pdf_path = r"pdf_file.pdf"
content_list = extract_content(pdf_path)
register_fonts(content_list)
create_new_pdf(new_pdf_path, content_list, pdf_path)
