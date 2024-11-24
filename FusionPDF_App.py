import streamlit as st
import fitz  # PyMuPDF for PDF processing
from io import BytesIO
import convertapi
from ScannedPDF_Final import app


import tempfile

def process_pdf(input_pdf_bytes):
    """
    Processes the input PDF and generates an output PDF.

    Args:
        input_pdf_bytes (bytes): Byte data of the input PDF.

    Returns:
        bytes: Byte data of the processed PDF.
    """
    # Save the input PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(input_pdf_bytes)
        temp_pdf_path = temp_pdf.name

    # Set your API key and file path
    API_KEY = 'wx6tkon97x0q5qyl8'
    RESULT_URL = 'https://techhk.aoscdn.com/api/tasks/document/ocr/'

    # Step 1: Create OCR Task
    task_id = app.create_ocr_task(API_KEY, temp_pdf_path, output_format='docx')  # Pass the file path here

    if 'Error' not in task_id:
        print(f"Task created successfully. Task ID: {task_id}")

        # Step 2: Retrieve OCR Result
        result_url = app.perform_ocr_task(task_id=task_id, api_key=API_KEY, result_url=RESULT_URL)

        print(f"Processed document is available at: {result_url}")

    else:
        print(task_id)

    # Example usage:
    file_path = 'o.docx'
    output_path = 'TextOp.docx'
    para_indices_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 23, 24]  # Example: Remove paragraphs

    app.remove_paragraphs_by_index(file_path, output_path, para_indices_to_remove)

    convertapi.api_credentials = 'secret_HVuqFuKW4UsSHiCI'
    convertapi.convert('pdf', {
        'File': r'TextOp.docx'
    }, from_format='docx').save_files('ScannedPDF_Final')

    app.convert_pdf_to_jpg(r"documents\scan1.pdf", "ScannedPDF_Final", zoom=3)

    app.save_headersNfooters(r"ScannedPDF_Final\page_1.jpg")

    header_image = "Header.jpg"  # Path to the header image
    footer_image = "Footer.jpg"  # Path to the footer image
    output_pdf_path = "FinalOutput.pdf"  # Path where the PDF will be saved

    app.create_pdf_with_images(header_image, footer_image, output_pdf_path)

    pdf_path = r"ScannedPDF_Final/TextOp.pdf"
    output_json_path = r"extracted_text_with_coordinates.json"
    app.extract_text_with_coordinates(pdf_path, output_json_path)
    app.add_text_and_character_count(pdf_path, output_json_path)
    app.translate_and_insert_newlines(pdf_path, output_json_path, dest_language='kn')
    font_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"
    app.create_translated_pdf(output_json_path, output_pdf_path, font_path)

    # Return processed PDF as bytes
    with open(output_pdf_path, "rb") as f:
        return f.read()



st.title("PDF Processor")
st.markdown("Upload a PDF file, process it, and download the result.")
# File uploader for input PDF
uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_pdf is not None:
    st.success(f"Uploaded file: {uploaded_pdf.name}")
    # Read the uploaded PDF as bytes
    input_pdf_bytes = uploaded_pdf.read()
    # Delay process_pdf execution until user explicitly clicks a button
    if st.button("Process PDF"):
        st.markdown("### Processing...")
        processed_pdf_bytes = process_pdf(input_pdf_bytes)
        st.success("Processing complete!")
        # Provide a download link for the processed PDF
        st.markdown("### Download Processed PDF")
        st.download_button(
            label="Download",
            data=processed_pdf_bytes,
            file_name=f"processed_{uploaded_pdf.name}",
            mime="application/pdf",
        )

