import streamlit as st
from PIL import Image
import fitz  # PyMuPDF
import pytesseract
from googletrans import Translator
import tempfile
from pdf2image import convert_from_path
from streamlit_drawable_canvas import st_canvas
import re
import os
import json
from fpdf import FPDF
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"C:/Program Files/Tesseract-OCR/tessdata" 

# Function to convert PDF pages to images
def pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path,dpi=300, poppler_path=r'C:\Users\Lenovo\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin')
    return images

# Function to save translations to JSON file
def save_translation_to_json(kannada_sentence, translated_sentence, json_filename="output.json"):
    """
    Save Kannada and English sentences in structured JSON format.
    """
    data = {
        "text": kannada_sentence,
        "translated_text": translated_sentence,
        "character_count": len(kannada_sentence),
        "translated_character_count": len(translated_sentence),
    }

    try:
        # Load existing data
        with open(json_filename, "r", encoding="utf-8") as json_file:
            existing_data = json.load(json_file)
            if not isinstance(existing_data, list):
                existing_data = []
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is invalid, start with an empty list
        existing_data = []

    # Append new translation
    existing_data.append(data)

    # Write back to JSON
    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

# Function to translate Kannada text sentence by sentence
def translate_sentence_by_sentence(kannada_text):
    translator = Translator()
    sentences = re.split(r'(?<=[.:;?])', kannada_text)  # Split based on punctuation
    translated_sentences = []

    for sentence in sentences:
        if sentence.strip():  # Skip empty sentences
            translated = translator.translate(sentence.strip(), src='kn', dest='en')
            save_translation_to_json(sentence.strip(), translated.text)  # Save to JSON
            translated_sentences.append(translated.text)
    
    return " ".join(translated_sentences)  # Combine for PDF saving

# Function to save translated text to PDF
def save_to_pdf(english_text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, english_text)  # Adds the text to PDF
    pdf.output(filename)

# Streamlit App
st.title("PDF Text Extraction and Kannada-to-English Translation")
st.write("Upload a PDF, crop Kannada text, translate sentence by sentence, and download the final PDF.")

# Step 1: Upload PDF
uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_pdf:
    with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
        temp_pdf.write(uploaded_pdf.getvalue())
        pdf_path = temp_pdf.name

    # Convert PDF pages to images
    images = pdf_to_images(pdf_path)
    if not images:
        st.error("No images found in the uploaded PDF.")
    else:
        st.write("Select a page image to process:")
        page_number = st.selectbox("Select Page", list(range(1, len(images) + 1)))

        # Display the selected page image
        selected_image = images[page_number - 1]
        st.image(selected_image, caption=f"Page {page_number}", use_column_width=True)

        # Step 2: Allow area selection
        st.write("Draw a rectangle to crop Kannada text:")
        image = selected_image.resize((1400, 1700), Image.LANCZOS)
        canvas_result = st_canvas(
            fill_color="rgba(0, 0, 0, 0)",  # Transparent fill
            stroke_width=3,
            stroke_color="#FF0000",
            background_image=image,
            update_streamlit=True,
            height=850,
            width=700,
            drawing_mode="rect",
            key="canvas"
        )


        # Step 3: Process selected area
        if canvas_result.json_data is not None:
            objects = canvas_result.json_data.get("objects", [])
            if objects:
                rect = objects[0]  # Rectangle selection
                x, y, width, height = int(rect['left']), int(rect['top']), int(rect['width']), int(rect['height'])

                # Scale coordinates to original image size
                orig_width, orig_height = selected_image.size
                scale_x = orig_width / 700  # Canvas width
                scale_y = orig_height / 850  # Canvas height
                x, y, width, height = int(x * scale_x), int(y * scale_y), int(width * scale_x), int(height * scale_y)

                # Crop the selected area
                cropped_image = selected_image.crop((x, y, x + width, y + height)).convert("RGB")
                st.image(cropped_image, caption="Cropped Area", use_column_width=True)

                # Step 4: Extract text
                if st.button("Translate and Save"):
                    st.write("Extracting Kannada text...")
                    
                    # Extract text from the cropped image
                    kannada_text = pytesseract.image_to_string(cropped_image, lang="kan")
                    st.subheader("Extracted Kannada Text:")
                    st.write(kannada_text)

                    # Translate the text
                    st.write("Translating sentence by sentence...")
                    translated_text = translate_sentence_by_sentence(kannada_text)
                    st.subheader("Translated Text (English):")
                    st.write(translated_text)

                    # Save translated text to a PDF
                    save_dir = os.path.expanduser("~/Documents")  # Save to Documents directory
                    save_path = os.path.join(save_dir, "final_translation.pdf")
                    save_to_pdf(translated_text, save_path)

                    with open(save_path, "rb") as f:
                        st.download_button("Download Translated PDF", f, file_name="final_translation.pdf")
            else:
                st.info("Please draw a rectangle to select the area containing text.")
