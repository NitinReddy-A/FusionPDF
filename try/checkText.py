# Import required dependencies
import fitz
import os
from PIL import Image

# Define the path to the PDF file
pdf_path = r"documents/demo1KannadaCorr.pdf"
new_pdf_path = r"documents/output.pdf"

# Define default font style for the new PDF
default_font = "helv"  # Helvetica font family

# Create a document object
doc = fitz.open(pdf_path)

# Create a new PDF document
new_doc = fitz.open()  # Create an empty new PDF

# Define the path to the Noto Sans Kannada TTF file
noto_sans_kannada_path = r"Nirmala.ttf"  # Update this with the correct path

# Extract the number of pages
print(f"Number of pages: {doc.page_count}")

# Extract metadata
#print("Metadata:", doc.metadata)

# Iterate through all pages
for i in range(doc.page_count):
    # Get the page
    page = doc.load_page(i)  # or page = doc[i]
    # Get the original page
    original_page = doc.load_page(i)

    # Create a new page with the same size as the original page
    new_page = new_doc.new_page(width=original_page.rect.width, height=original_page.rect.height)
    
    # Extract text blocks from the page
    blocks = page.get_text_blocks()
    font = doc.get_page_fonts(page, full=False)
    print(font)
    
    # Extract text with coordinates
    text_with_coordinates = ""
    for b in blocks:
        # Extract text and coordinates
        text = b[4]
        x0, y0, x1, y1 = b[:4]
        # Append to the result
        text_with_coordinates += f"Text: {text}, Coordinates: ({x0}, {y0}) - ({x1}, {y1})\n"
        # Draw text on the new page with default font style
        new_page.insert_text((x0, y0), text,fontname='Nirmala',
                fontfile=noto_sans_kannada_path, fontsize=9, color=(0, 0, 0),encoding='Identity-H')

# Save the new PDF document
new_doc.save(new_pdf_path)

# Close all documents
doc.close()
new_doc.close()