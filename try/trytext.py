# Import required dependencies
import fitz
import os
from PIL import Image

# Define the path to the PDF file
pdf_path = r"try\demo.pdf"

# Create a document object
doc = fitz.open(pdf_path)

# Extract the number of pages
print(f"Number of pages: {doc.page_count}")

# Extract metadata
print("Metadata:", doc.metadata)

# Iterate through all pages
for i in range(doc.page_count):
    # Get the page
    page = doc.load_page(i)  # or page = doc[i]
    
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
    
    # Print text with coordinates
    print(f"Text with coordinates on page {i + 1}:\n{text_with_coordinates}\n")
    
    # Extract text from the page
    text = page.get_text()
    print(f"Text on page {i + 1}:\n{text}\n")
    
    # Render and save the page as an image
    pix = page.get_pixmap()
    image_filename = f"page-{i + 1}.png"
    pix.save(image_filename)
    print(f"Saved image: {image_filename}")
    
    # Get all links on the page
    links = page.get_links()
    print(f"Links on page {i + 1}: {links}\n")
