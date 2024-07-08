import fitz
from googletrans import Translator
import os

# Define the path to the original PDF file
original_pdf_path = r"demo1.pdf"

# Define the path to the Noto Sans Kannada TTF file
noto_sans_kannada_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"

# Check if the font file exists
if not os.path.isfile(noto_sans_kannada_path):
    raise FileNotFoundError(f"The font file was not found: {noto_sans_kannada_path}")

# Create a document object for the original PDF
original_doc = fitz.open(original_pdf_path)

# Load the font into a buffer
with open(noto_sans_kannada_path, "rb") as font_file:
    font_buffer = font_file.read()

# Initialize the translator
translator = Translator()

# Function to translate text
def translate_text(text, dest_language='kn'):  # Change 'kn' to your desired language code
    try:
        translated = translator.translate(text, dest=dest_language)
        print("Translated:", translated.text)
        return translated.text
    except Exception as e:
        print(f"Error in translation: {e}")
        return text

# Iterate through all pages of the original PDF
for i in range(original_doc.page_count):
    # Get the original page
    original_page = original_doc.load_page(i)

    # Extract text blocks from the original page
    blocks = original_page.get_text("blocks")

    # Add text with coordinates to the same page
    for b in blocks:
        try:
            # Extract text and coordinates
            text = b[4]
            x0, y0, x1, y1 = b[:4]

            # Translate the text to Kannada
            #translated_text = translate_text(text).encode('utf-8').decode('utf-8')

            # Redact the original text area
            original_page.add_redact_annot(fitz.Rect(x0, y0, x1, y1), text=text)

            # Apply the redactions (removes the original text)
            original_page.apply_redactions(images=0, graphics=0,text=0)

            # Draw translated text on the original page with the font buffer
            #original_page.insert_textbox(
            #    fitz.Rect(x0, y0, x1, y1),
            #    translated_text,
            #    fontfile=noto_sans_kannada_path,
            #    fontname='NotoSansKannada',
            #    fontsize=10,
            #    
            #)

        except Exception as e:
            print(f"Error processing text block: {e}")

# Save the modified PDF document
original_doc.saveIncr()

# Close the document
original_doc.close()

print("PDF content translated and replaced in the same PDF successfully.")
