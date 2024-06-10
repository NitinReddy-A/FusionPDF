# Import required dependencies
import fitz

# Define the path to the original PDF file and the path to the new PDF file
original_pdf_path = r"try\demo.pdf"
new_pdf_path = r"try\new_demo.pdf"

# Create a document object for the original PDF
original_doc = fitz.open(original_pdf_path)

# Create a new PDF document
new_doc = fitz.open()

# Define default font style for the new PDF
default_font = "helv"  # Helvetica font family

# Iterate through all pages of the original PDF
for i in range(original_doc.page_count):
    # Get the original page
    original_page = original_doc.load_page(i)
    
    # Create a new page with the same size as the original page
    new_page = new_doc.new_page(width=original_page.rect.width, height=original_page.rect.height)
    
    # Extract text blocks from the original page
    blocks = original_page.get_text_blocks()
    
    # Add text with coordinates to the new page
    for b in blocks:
        try:
            # Extract text and coordinates
            text = b[4]
            x0, y0, x1, y1 = b[:4]
            print(text)
            # Draw text on the new page with default font style
            new_page.insert_text((x0, y0), text, fontname=default_font, fontsize=12, color=(0, 0, 0))
        except Exception as e:
            print(f"Error processing text block: {e}")
    
# Save the new PDF document
new_doc.save(new_pdf_path)

# Close all documents
original_doc.close()
new_doc.close()

print("New PDF with extracted content created successfully.")