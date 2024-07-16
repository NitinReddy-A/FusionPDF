import fitz
import json
import os

# Path to the JSON file
json_path = r"extracted_text_with_coordinates.json"

# Path to the output translated PDF file
output_pdf_path = r"translated_demo1_new.pdf"

# Define the path to the Noto Sans Kannada TTF file
noto_sans_kannada_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"

# Check if the font file exists
if not os.path.isfile(noto_sans_kannada_path):
    raise FileNotFoundError(f"The font file was not found: {noto_sans_kannada_path}")

# Load the JSON data
with open(json_path, "r", encoding="utf-8") as json_file:
    extracted_data = json.load(json_file)

# Create a new PDF document
new_doc = fitz.open()

# Iterate through the pages in the JSON data
for page_num, page_data in extracted_data.items():
    # Create a new page
    new_page = new_doc.new_page()

    # Iterate through the text blocks on the current page
    for block in page_data:
        translated_text = block.get("translated_text", "")
        coordinates = block["coordinates"]
        #origin = block["origin"]
        x0, y0, x1, y1 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]

        # Set the font size based on the height of the bounding box
        font_size = block["IniFontsize"]

        # Draw translated text on the new page with the font file using insert_textbox
        new_page.insert_text(
            (x0,y0),
            text=translated_text,
            fontsize=font_size*0.8,
            fontname='NotoSansKannada',
            fontfile=noto_sans_kannada_path
        )

# Save the new PDF
new_doc.save(output_pdf_path)

# Close the document
new_doc.close()
ಹಿಂಡೋಸ್ 