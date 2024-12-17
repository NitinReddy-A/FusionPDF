import fitz
import json

# Define the path to the PDF file
pdf_path = r"TranslatedOutput.pdf"

# Define the path to the output JSON file
json_path = r"extracted_text_with_coordinates.json"

# Load the JSON data
with open(json_path, "r", encoding="utf-8") as json_file:
    extracted_data = json.load(json_file)

# Create a document object
doc = fitz.open(pdf_path)

# Iterate through the extracted data and translate the text
for page_num, page_data in extracted_data.items():
    
    # Get the page
    page = doc.load_page(int(page_num) - 1)  # or page = doc[i]
    blocks = page.get_text("blocks")
    for b,block in zip(blocks,page_data):
        text = b[4]
        block["text"] = text
        block["Character_count"] = len(text)


# Save the extracted data to a JSON file
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)

# Close the document
doc.close()

