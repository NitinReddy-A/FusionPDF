# Import required dependencies
import fitz
import os
from PIL import Image

# Define the path to the PDF file
pdf_path = r"translated_document.pdf"
new_pdf_path = r"d.pdf"

# Define default font style for the new PDF
default_font = "NotoSansKannada"  

# Define the path to the Noto Sans Kannada TTF file
noto_sans_kannada_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"

# Load the font into a buffer
with open(noto_sans_kannada_path, "rb") as font_file:
    font_buffer = font_file.read()

# Create a document object
doc = fitz.open(pdf_path)

# Create a new PDF document
new_doc = fitz.open()

# Extract the number of pages
print(f"Number of pages: {doc.page_count}")

# Extract metadata
print("Metadata:", doc.metadata)

# Define the path to the output text file
output_file_path = r"extracted_text_with_coordinates.txt"

# Open the output text file in write mode
with open(output_file_path, "w", encoding="utf-8") as output_file:
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
        
        # Extract text with coordinates
        text_with_coordinates = ""
        for b in blocks:
            # Extract text and coordinates
            text = b[4]
            x0, y0, x1, y1 = b[:4]
            # Append to the result
            text_with_coordinates += f"Text: {text}, Coordinates: ({x0}, {y0}) - ({x1}, {y1})\n"

            # Draw text on the new page with default font style
            new_page.insert_text((x0, y0), text, fontname=default_font,fontfile=noto_sans_kannada_path, fontsize=9, color=(0, 0, 0))
        # Write text with coordinates to the file
        output_file.write(f"Text with coordinates on page {i + 1}:\n{text_with_coordinates}\n")
        output_file.write("\n")
    # Save the new PDF document
    new_doc.save(new_pdf_path)

    # Close all documents
    doc.close()
    new_doc.close()
print(f"Text with coordinates has been saved to {output_file_path}")
