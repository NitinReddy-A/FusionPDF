import fitz
import pymupdf
import os

# Open the PDF document
doc = fitz.open(r"C:\Users\Lenovo\Downloads\scan1.pdf") #---------> Specify the input file
new_pdf_path = r"documents/scan.pdf" #-----------> Specify the output file

# Create a new PDF document
new_doc = fitz.open()

# FOR TEXT ------------------------------------------>
for i in range(doc.page_count):
    # Get the original page
    original_page = doc.load_page(i)

    # Create a new page with the same size as the original page
    new_page = new_doc.load_page(i)

    # Extract text blocks from the original page
    blocks = original_page.get_text("blocks")

    # Add text with coordinates to the new page
    for b in blocks:
        try:
            # Extract text and coordinates
            text = b[4]
            x0, y0, x1, y1 = b[:4]

            rect = fitz.Rect(x0, y0, x1, y1)

            # Draw translated text on the new page with the font buffer
            new_page.insert_textbox(
                rect,
                text,
                color=(0, 0, 0)
            )
        except Exception as e:
            print(f"Error processing text block: {e}")

# Save the new PDF document
new_doc.save(new_pdf_path)

# Close all documents
doc.close()
new_doc.close()
