# Import required dependencies
import fitz
import os
from PIL import Image

# Define the path to the PDF file
pdf_path = r"documents/demo1.pdf"
new_pdf_path = r"documents/translateddemo1.pdf"

# Define default font style for the new PDF
default_font = "helv"  # Helvetica font family

# Create a document object
doc = fitz.open(pdf_path)

# Create a new PDF document
new_doc = fitz.open(new_pdf_path)

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
        new_page = new_doc.load_page(i)
        
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
            new_page.insert_text((x0, y0), text, fontname=default_font, fontsize=12, color=(0, 0, 0))
        # Write text with coordinates to the file
        output_file.write(f"Text with coordinates on page {i + 1}:\n{text_with_coordinates}\n")
        output_file.write("\n")
    # Save the new PDF document
    new_doc.saveIncr()

    # Close all documents
    doc.close()
    new_doc.close()
print(f"Text with coordinates has been saved to {output_file_path}")
