import fitz
from googletrans import Translator

# Define the path to the original PDF file and the path to the new PDF file
original_pdf_path = r"documents/demo1.pdf"
new_pdf_path = r"documents/new_demo.pdf"

# Define the path to the Noto Sans Kannada TTF file
noto_sans_kannada_path = r"fonts/NotoSansKannada-VariableFont_wdth,wght.ttf"  # Update this with the correct path

# Create a document object for the original PDF
original_doc = fitz.open(original_pdf_path)

# Create a new PDF document
new_doc = fitz.open()

# Initialize the translator
translator = Translator()

# Function to translate text
def translate_text(text, dest_language='kn'):  # Change 'kn' to your desired language code
    try:
        translated = translator.translate(text, dest=dest_language)
        print("trans", translated.text)
        return translated.text
    except Exception as e:
        print(f"Error in translation: {e}")
        return text

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

            # Translate the text to Kannada
            translated_text = translate_text(text)

            # Draw translated text on the new page with the specified font
            new_page.insert_text(
                (x0, y0),
                translated_text,
                fontname='noto_sans_kannada',
                fontfile=noto_sans_kannada_path,
                fontsize=12,
                color=(0, 0, 0)
            )
        except Exception as e:
            print(f"Error processing text block: {e}")

# Save the new PDF document
new_doc.save(new_pdf_path)

# Close all documents
original_doc.close()
new_doc.close()

print("New PDF with translated content created successfully.")
