import fitz

def convert_pdf_to_jpg(pdf_path, output_folder, zoom=2):
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
        
    # Set a matrix to scale the page by the zoom factor (2 = 200% size)
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    
    pix.save(f"{output_folder}/page_{1}.jpg")

    doc.close()

convert_pdf_to_jpg(r"TranslatedOutput.pdf", "ScannedPDF_Final",zoom=3)