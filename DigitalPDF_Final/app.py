from docx import Document
import requests
import os
import time
import fitz
import pymupdf
from PIL import Image
import json
from fpdf import FPDF
import convertapi
from googletrans import Translator

def extract_text_with_coordinates(pdf_path, output_json_path):
    """
    Extract text from a PDF file along with coordinates, font size, and color,
    and save the data to a JSON file.

    :param pdf_path: Path to the input PDF file.
    :param output_json_path: Path to the output JSON file.
    """
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
        blocks = page.get_text("dict", flags=11)["blocks"]
    
        #blocks1 = page.get_text("blocks")
        
        # List to store text and coordinates for the current page
        page_data = []
    
    
    
        for b in blocks:
            bbox = b["bbox"]
            for l in b["lines"]:  # iterate through the text lines
                for s in l["spans"]:  # iterate through the text spans
                    text = s["text"]
                    #origin = s["origin"]
                    font_size = s["size"]
                    #character_count = len(text)
                    color = s["color"]
    
            # Append to the result
            page_data.append({
                "coordinates": bbox,
                "text": text,
                #"IniCharacter_count": character_count,
                "IniFontsize": font_size,
                "Color": color,
            })
    
        # Add the page data to the extracted data dictionary
        extracted_data[i+1] = page_data
    
    # Save the extracted data to a JSON file
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)
    
    # Close the document
    doc.close()
    print(f"Extraction complete. Data saved to {output_json_path}.")


def add_text_and_character_count(pdf_path, json_path):
    """
    This function loads the extracted data from a JSON file, updates the text and character count
    for each block in the PDF, and saves the updated data back to the JSON file.

    :param pdf_path: Path to the input PDF file.
    :param json_path: Path to the JSON file with extracted data.
    """
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

    print(f"Text and character count added. Data saved to {json_path}.")

def create_pdf_with_images(input_pdf_path, output_pdf_path, image_dir='images/'):
    """Extract images from a PDF and create a new PDF with those images."""
    # Create the images directory
    if not os.path.exists(image_dir):
        os.mkdir(image_dir)

    # Open the PDF document
    doc = fitz.open(input_pdf_path)

    # Create a new PDF document
    new_doc = fitz.open()

    # Process each page
    for page_index in range(doc.page_count):
        original_page = doc.load_page(page_index)

        # Create a new page with the same size as the original
        new_page = new_doc.new_page(width=original_page.rect.width, height=original_page.rect.height)

        # Extract images from the page
        page = doc.load_page(page_index)
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            try:
                if img[1] == 0:
                    bbox = page.get_image_bbox(img)
                    xref = img[0]  # Get the XREF of the image
                    pix = pymupdf.Pixmap(doc, xref)  # Create a Pixmap
                    if pix.n - pix.alpha > 3:  # CMYK: convert to RGB
                        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

                    image_path = os.path.join(image_dir, f"page{page_index}-image{img_index}.png")
                    pix.save(image_path)  # Save the image as PNG
                    pix = None

                    with open(image_path, "rb") as image_file:
                        new_page.insert_image(bbox, stream=image_file.read())

                    print(f"Image {img_index} on page {page_index} extracted and inserted: {bbox}")
            except Exception as e:
                print(f"An error occurred while extracting image: {e}")

    # Save the new PDF document
    new_doc.save(output_pdf_path)
    new_doc.close()
    doc.close()


def translate_and_insert_newlinesk(pdf_path, json_path, dest_language='kn'):
    """
    This function loads extracted text from a JSON file, translates the text,
    inserts newlines at appropriate positions, and updates the JSON file with the translated text
    and character counts.

    :param pdf_path: Path to the input PDF file (unused here, kept for context).
    :param json_path: Path to the input/output JSON file.
    :param dest_language: The language code to translate to (default is Kannada 'kn').
    """
    # Initialize the translator
    translator = Translator()

    # Function to translate text
    def translate_text(text, dest_language='kn'):  # Change 'kn' to your desired language code
        try:
            translated = translator.translate(text, dest=dest_language)
            print("Translated:", translated.text)
            return (translated.text)
        except Exception as e:
            print(f"Error in translation: {e}")
            return text

    def insert_newlines(text, translated_text):
        # Find positions of '\n' in the original text
        newline_positions = [pos for pos, char in enumerate(text) if char == '\n']

        # Adjust positions for translated text
        adjusted_positions = []
        offset = 0
        for pos in newline_positions:
            while pos + offset < len(translated_text) and translated_text[pos + offset] != ' ':
                offset += 1
            adjusted_positions.append(pos + offset)

        # Insert '\n' at the adjusted positions
        for pos in reversed(adjusted_positions):  # reversed to avoid messing up positions
            translated_text = translated_text[:pos] + '\n' + translated_text[pos:]

        return translated_text


    # Load the JSON data
    with open(json_path, "r", encoding="utf-8") as json_file:
        extracted_data = json.load(json_file)

    # Iterate through the extracted data and translate the text
    for page_num, page_data in extracted_data.items():
        for block in page_data:
            original_text = block.get("text", "")
            c1 = block.get("Character_count", len(original_text)) 
            f = block.get("IniFontsize", 12)
            translated_text = translate_text(original_text, dest_language='kn')  # Change 'kn' to your desired language code
            block["translated_text"] = translated_text
            block["translated_character_count"] = len(translated_text)
            #block["Translated_text"] = insert_newlines(block["text"], translated_text)
            if c1 < len(translated_text):
                block["Font_Size"] = len(translated_text) * f / c1
            else:
                block["Font_Size"] = f

    # Save the translated data back to the same JSON file
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)
    
    print(f"Translation and updates complete. Data saved to {json_path}.")

def translate_and_insert_newlinesh(pdf_path, json_path, dest_language='hi'):
    """
    This function loads extracted text from a JSON file, translates the text,
    inserts newlines at appropriate positions, and updates the JSON file with the translated text
    and character counts.

    :param pdf_path: Path to the input PDF file (unused here, kept for context).
    :param json_path: Path to the input/output JSON file.
    :param dest_language: The language code to translate to (default is Kannada 'kn').
    """
    # Initialize the translator
    translator = Translator()

    # Function to translate text
    def translate_text(text, dest_language='hi'):  # Change 'kn' to your desired language code
        try:
            translated = translator.translate(text, dest=dest_language)
            print("Translated:", translated.text)
            return (translated.text)
        except Exception as e:
            print(f"Error in translation: {e}")
            return text

    def insert_newlines(text, translated_text):
        # Find positions of '\n' in the original text
        newline_positions = [pos for pos, char in enumerate(text) if char == '\n']

        # Adjust positions for translated text
        adjusted_positions = []
        offset = 0
        for pos in newline_positions:
            while pos + offset < len(translated_text) and translated_text[pos + offset] != ' ':
                offset += 1
            adjusted_positions.append(pos + offset)

        # Insert '\n' at the adjusted positions
        for pos in reversed(adjusted_positions):  # reversed to avoid messing up positions
            translated_text = translated_text[:pos] + '\n' + translated_text[pos:]

        return translated_text


    # Load the JSON data
    with open(json_path, "r", encoding="utf-8") as json_file:
        extracted_data = json.load(json_file)

    # Iterate through the extracted data and translate the text
    for page_num, page_data in extracted_data.items():
        for block in page_data:
            original_text = block.get("text", "")
            c1 = block.get("Character_count", len(original_text)) 
            f = block.get("IniFontsize", 12)
            translated_text = translate_text(original_text, dest_language='hi')  # Change 'kn' to your desired language code
            block["translated_text"] = translated_text
            block["translated_character_count"] = len(translated_text)
            #block["Translated_text"] = insert_newlines(block["text"], translated_text)
            if c1 < len(translated_text):
                block["Font_Size"] = len(translated_text) * f / c1
            else:
                block["Font_Size"] = f

    # Save the translated data back to the same JSON file
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)
    
    print(f"Translation and updates complete. Data saved to {json_path}.")


def translate_and_insert_newlinesr(pdf_path, json_path, dest_language='ru'):
    """
    This function loads extracted text from a JSON file, translates the text,
    inserts newlines at appropriate positions, and updates the JSON file with the translated text
    and character counts.

    :param pdf_path: Path to the input PDF file (unused here, kept for context).
    :param json_path: Path to the input/output JSON file.
    :param dest_language: The language code to translate to (default is Kannada 'kn').
    """
    # Initialize the translator
    translator = Translator()

    # Function to translate text
    def translate_text(text, dest_language='ru'):  # Change 'kn' to your desired language code
        try:
            translated = translator.translate(text, dest=dest_language)
            print("Translated:", translated.text)
            return (translated.text)
        except Exception as e:
            print(f"Error in translation: {e}")
            return text

    def insert_newlines(text, translated_text):
        # Find positions of '\n' in the original text
        newline_positions = [pos for pos, char in enumerate(text) if char == '\n']

        # Adjust positions for translated text
        adjusted_positions = []
        offset = 0
        for pos in newline_positions:
            while pos + offset < len(translated_text) and translated_text[pos + offset] != ' ':
                offset += 1
            adjusted_positions.append(pos + offset)

        # Insert '\n' at the adjusted positions
        for pos in reversed(adjusted_positions):  # reversed to avoid messing up positions
            translated_text = translated_text[:pos] + '\n' + translated_text[pos:]

        return translated_text


    # Load the JSON data
    with open(json_path, "r", encoding="utf-8") as json_file:
        extracted_data = json.load(json_file)

    # Iterate through the extracted data and translate the text
    for page_num, page_data in extracted_data.items():
        for block in page_data:
            original_text = block.get("text", "")
            c1 = block.get("Character_count", len(original_text)) 
            f = block.get("IniFontsize", 12)
            translated_text = translate_text(original_text, dest_language='ru')  # Change 'kn' to your desired language code
            block["translated_text"] = translated_text
            block["translated_character_count"] = len(translated_text)
            #block["Translated_text"] = insert_newlines(block["text"], translated_text)
            if c1 < len(translated_text):
                block["Font_Size"] = len(translated_text) * f / c1
            else:
                block["Font_Size"] = f

    # Save the translated data back to the same JSON file
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)
    
    print(f"Translation and updates complete. Data saved to {json_path}.")


def create_translated_pdf(json_path, output_pdf_path, font_path):
    """
    This function reads translated text from a JSON file and adds it to a PDF document
    with the specified font, saving the result as an incremental update.

    :param json_path: Path to the JSON file containing extracted text with coordinates.
    :param output_pdf_path: Path to the existing PDF file where text will be added.
    :param font_path: Path to the TTF font file (e.g., Noto Sans Kannada).
    """
    # Check if the font file exists
    if not os.path.isfile(font_path):
        raise FileNotFoundError(f"The font file was not found: {font_path}")

    # Load the JSON data
    with open(json_path, "r", encoding="utf-8") as json_file:
        extracted_data = json.load(json_file)

    # Create a new PDF document
    new_doc = fitz.open(output_pdf_path)

    # Iterate through the pages in the JSON data
    for page_num, page_data in extracted_data.items():
        # Load a page
        new_page = new_doc.load_page(int(page_num)-1)

        # Iterate through the text blocks on the current page
        for block in page_data:
            translated_text = block["translated_text"]
            coordinates = block["coordinates"]
            #origin = block["origin"]
            x0, y0, x1, y1 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]

            # Set the font size based on the height of the bounding box
            font_size = block["IniFontsize"]

            rect = fitz.Rect(x0, y0, x1, y1)

            print(translated_text)

            # Draw translated text on the new page with the font file using insert_textbox
            new_page.insert_htmlbox(
                coordinates,
                translated_text,
                #align=0,
                #fontsize=font_size,
                #fontname='NotoSansKannada',
                #fontfile=noto_sans_kannada_path,
                #color=(0, 0, 0),
                #oc=0
            )#

    # Save the new PDF
    new_doc.saveIncr()

    # Close the document
    new_doc.close()

    print(f"Translated PDF saved to {output_pdf_path}.")


# pdf_path = r"ScannedPDF_Final/TextOp.pdf"
# output_json_path = r"extracted_text_with_coordinates.json"
# extract_text_with_coordinates(pdf_path, output_json_path)
# add_text_and_character_count(pdf_path, output_json_path)
# translate_and_insert_newlines(pdf_path, output_json_path, dest_language='kn')
# font_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"
# create_translated_pdf(output_json_path, output_pdf_path, font_path)