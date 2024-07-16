import fitz
import json

# Define the path to the PDF file
pdf_path = r"documents\demo1.pdf"

# Dictionary to store text with coordinates and character count
extracted_data = {}

# Function to count total characters in extracted data
#def count_total_characters(extracted_data):
#    for page_num, page_data in extracted_data.items():
#        print(f"Page {page_num}:")
#        for block_num, block in enumerate(page_data, 1):
#            text = block["text"]
#            character_count = block["IniCharacter_count"]
#            print(f"Block {block_num}: has {character_count} characters.")

# Create a document object
doc = fitz.open(pdf_path)

# Extract the number of pages
#print(f"Number of pages: {doc.page_count}")

# Extract metadata
#print("Metadata:", doc.metadata)

# Iterate through all pages
#for i in range(doc.page_count):
# Get the page
page = doc.load_page(0)  # or page = doc[i]

# Extract text blocks from the page
blocks = page.get_text("dict", flags=11)["blocks"]

for b in blocks:
    for l in b["lines"]:  # iterate through the text lines
        for s in l["spans"]:  # iterate through the text spans
            #text = s["text"]
            #bbox = s["bbox"]
            #origin = s["origin"]
            font_size = s["size"]
            #character_count = len(text)
    print(b , "\n")
bl = page.get_text("blocks")
print(bl)
#Remove /n from all the text.
                # Append to the result
                #page_data.append({
                #    "coordinates": bbox,
                #    "origin": origin,
                #    "text": text,
                #    "IniCharacter_count": character_count,
                #    "IniFontsize": font_size,
                #})


# Close the document
doc.close()
