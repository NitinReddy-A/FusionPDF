# Import required dependencies
import fitz
import os
import json
from PIL import Image

# Define the path to the PDF file
pdf_path = r"documents\translatedDemo1.pdf"

# Define default font style for the new PDF
default_font = "NotoSansKannada"

# Define the path to the Noto Sans Kannada TTF file
noto_sans_kannada_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"

# Load the font into a buffer
with open(noto_sans_kannada_path, "rb") as font_file:
    font_buffer = font_file.read()

# Create a document object
doc = fitz.open(pdf_path)

# Extract the number of pages
print(f"Number of pages: {doc.page_count}")

# Extract metadata
print("Metadata:", doc.metadata)

# Define the path to the output JSON file
output_json_path = r"extracted_text_with_coordinates1.json"

# Dictionary to store text with coordinates and character count
extracted_data = {}

# Function to count total characters in extracted data
def count_total_characters(extracted_data):
    for page_num, page_data in extracted_data.items():
        print(f"Page {page_num}:")
        for block_num, block in enumerate(page_data, 1):
            text = block["text"]
            character_count = block["character_count"]
            print(f"Block {block_num}: has {character_count} characters.")

# Iterate through all pages
for i in range(doc.page_count):
    # Get the page
    page = doc.load_page(i)  # or page = doc[i]
    
    # Extract text blocks from the page
    blocks = page.get_text_blocks()
    
    # List to store text and coordinates for the current page
    page_data = []

    for b in blocks:
        # Extract text and coordinates
        text = b[4]
        x0, y0, x1, y1 = b[:4]
        character_count = len(text)

        # Append to the result
        page_data.append({
            "text": text,
            "character_count": character_count,
            "coordinates": {
                "x0": x0,
                "y0": y0,
                "x1": x1,
                "y1": y1
            }
        })

    # Add the page data to the extracted data dictionary
    extracted_data[f"page_{i + 1}"] = page_data

# Save the extracted data to a JSON file
with open(output_json_path, "w", encoding="utf-8") as json_file:
    json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)

# Close all documents
doc.close()

# Print the total number of characters for each text block
count_total_characters(extracted_data)
