import fitz
import pymupdf
from googletrans import Translator
import os
import convertapi

# Open the PDF document
doc = fitz.open(r"documents/demo.pdf") #---------> Specify the input file
new_pdf_path = r"documents/TranslatedDemo.pdf" #-----------> Specify the output file

# Create a new PDF document
new_doc = fitz.open()

# Create the images directory if it doesn't exist
if not os.path.exists('images/'):
    os.mkdir('images/')

# Define the path to the Noto Sans Kannada TTF file
noto_sans_kannada_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"

# Check if the font file exists
if not os.path.isfile(noto_sans_kannada_path):
    raise FileNotFoundError(f"The font file was not found: {noto_sans_kannada_path}")

# FOR IMAGES ------------------------------------------>
for page_index in range(doc.page_count):
    page = doc.load_page(page_index)
    # Get the original page
    original_page = doc.load_page(page_index)

    # Create a new page with the same size as the original page
    new_page = new_doc.new_page(width=original_page.rect.width, height=original_page.rect.height)

    # Get the list of images on the page
    image_list = page.get_images(full=True)

    # Iterate through each image and save it in the images folder
    for img_index, img in enumerate(image_list):
        try:
            if img[1] == 0:
                print(img)
                bbox = page.get_image_bbox(img)
                xref = img[0] # get the XREF of the image
                pix = pymupdf.Pixmap(doc, xref) # create a Pixmap
                if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
                    pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
                pix.save(f"images/page{page_index}-image{img_index}.png") # save the image as png
                pix = None
                new_page.insert_image(bbox, stream=open(f"images/page{page_index}-image{img_index}.png", "rb").read())
                print(f"Image {img_index} on page {page_index}: {bbox}")
        except Exception as e:
            print(f"An error occurred while extracting image: {e}")

# Save the new PDF document
new_doc.save(new_pdf_path)
new_doc.close()

# Create a new PDF document
new_doc = fitz.open(new_pdf_path)

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

            # Translate the text to Kannada
            translated_text = translate_text(text)

            # Ensure UTF-8 encoding
            translated_text = translated_text.encode('utf-8').decode('utf-8')

            rect = fitz.Rect(x0, y0, x1, y1)

            # Draw translated text on the new page with the font buffer
            new_page.insert_textbox(
                rect,
                translated_text,
                fontname='NotoSansKannada',
                fontfile=noto_sans_kannada_path,
                fontsize=10,
                color=(0, 0, 0)
            )
        except Exception as e:
            print(f"Error processing text block: {e}")

# Save the new PDF document
new_doc.saveIncr()

# Close all documents
doc.close()
new_doc.close()

# API Key 
convertapi.api_secret = '4OYbALQ2RREClhvm'

# Specify the file path here

docf = 'documents/TranslatedDemo1' #-----------------> new_pdf_path ***but without extension***

# For docx generation

convertapi.convert('docx', {
    'File': f'{docf}.pdf' 
}, from_format = 'pdf').save_files('documents')

# For pdf generation

convertapi.convert('pdf', {
    'File': f'{docf}.docx' 
}, from_format = 'docx').save_files('documents')

print("New PDF and Docx with translated content generated successfully.")