import fitz
import json

# Define the path to the PDF file
pdf_path = r"documents\knpdf.pdf"

# Define the path to the output JSON file
output_json_path = r"extracted_text_with_coordinates.json"

# Dictionary to store text with coordinates and character count
extracted_data = {}

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
    #blocks = page.get_text("dict", flags=11)["blocks"]

    blocks = page.get_text("blocks")
    
    
    # List to store text and coordinates for the current page
    page_data = []



    for b in blocks:
        print(b)
        bbox = b[:4]
        text = b[4]
        # for l in b["lines"]:  # iterate through the text lines
        #     #print(l)
        #     for s in l["spans"]:  # iterate through the text spans
        #         text = s["text"]
        #         print(text)
        #         #origin = s["origin"]
        #         font_size = s["size"]
        #         #character_count = len(text)
        #         color = s["color"]

        # Append to the result
        page_data.append({
            "coordinates": bbox,
            "text": text,
            #"IniCharacter_count": character_count,
            #"IniFontsize": font_size,
            #"Color": color,
        })

    # Add the page data to the extracted data dictionary
    extracted_data[i+1] = page_data

# Save the extracted data to a JSON file
with open(output_json_path, "w", encoding="utf-8") as json_file:
    json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)

# Close the document
doc.close()