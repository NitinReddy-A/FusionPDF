import streamlit as st
import fitz 
from io import BytesIO
import convertapi
from ScannedPDF_Final import app
from ScannedPDF_PreProcessing import DimensionofCircular
import tempfile
import os

def preview_pdf(input_pdf_bytes):
    """
    Generate a preview of the uploaded PDF's first page with grid and selection areas.
    """
    temp_pdf_path = None  # Initialize variable to ensure it's accessible in finally block
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(input_pdf_bytes)
            temp_pdf_path = temp_pdf.name

        # Convert the PDF to an image (page 1) and calculate image dimensions
        app.convert_pdf_to_jpg(temp_pdf_path, "ScannedPDF_Final", zoom=3)
        preview_image_path = r"ScannedPDF_Final\page_1.jpg"
        fig = DimensionofCircular.imageDimensions(preview_image_path)
        return fig
    except Exception as e:
        raise RuntimeError(f"Error in preview_pdf: {e}")
    finally:
        if temp_pdf_path and os.path.exists(temp_pdf_path):
            try:
                os.unlink(temp_pdf_path)  # Delete temporary file
            except PermissionError:
                pass  # Handle cases where the file might still be in use



def process_pdfk(input_pdf_bytes):
    """
    Process the uploaded PDF to extract text, apply translations, and generate output.
    """
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(input_pdf_bytes)
            temp_pdf_path = temp_pdf.name

        # OCR and text extraction
        API_KEY = 'wxj3ry5ayzkbk33ff'
        RESULT_URL = 'https://techhk.aoscdn.com/api/tasks/document/ocr/'

        task_id = app.create_ocr_task(API_KEY, temp_pdf_path, output_format='docx')
        if 'Error' in task_id:
            raise ValueError(f"OCR Task Error: {task_id}")

        result_url = app.perform_ocr_task(task_id=task_id, api_key=API_KEY, result_url=RESULT_URL)
        st.info(f"Processed document is available at: {result_url}")

        # Post-OCR processing
        file_path = 'o.docx'
        output_path = 'TextOp.docx'
        para_indices_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 23, 24]
        app.remove_paragraphs_by_index(file_path, output_path, para_indices_to_remove)

        convertapi.api_credentials = 'secret_KWmzJQRIOe8M5ueS'
        convertapi.convert('pdf', {'File': output_path}, from_format='docx').save_files('ScannedPDF_Final')

        # Text analysis and translation
        pdf_path = r"ScannedPDF_Final/TextOp.pdf"
        output_json_path = r"extracted_text_with_coordinates.json"
        app.extract_text_with_coordinates(pdf_path, output_json_path)
        app.add_text_and_character_count(pdf_path, output_json_path)
        app.translate_and_insert_newlinesk(pdf_path, output_json_path, dest_language='kn')
        font_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"
        
        output_pdf_path = r"TranslatedOutput.pdf"
        app.create_pdf_with_images("Header.jpg", "Footer.jpg", output_pdf_path)
        
        app.create_translated_pdf(output_json_path, output_pdf_path, font_path)

        # Return processed PDF as bytes
        with open(output_pdf_path, "rb") as f:
            return f.read()
    finally:
        os.unlink(temp_pdf_path)

def process_pdfh(input_pdf_bytes):
    """
    Process the uploaded PDF to extract text, apply translations, and generate output.
    """
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(input_pdf_bytes)
            temp_pdf_path = temp_pdf.name

        # OCR and text extraction
        API_KEY = 'wxj3ry5ayzkbk33ff'
        RESULT_URL = 'https://techhk.aoscdn.com/api/tasks/document/ocr/'

        task_id = app.create_ocr_task(API_KEY, temp_pdf_path, output_format='docx')
        if 'Error' in task_id:
            raise ValueError(f"OCR Task Error: {task_id}")

        result_url = app.perform_ocr_task(task_id=task_id, api_key=API_KEY, result_url=RESULT_URL)
        st.info(f"Processed document is available at: {result_url}")

        # Post-OCR processing
        file_path = 'o.docx'
        output_path = 'TextOp.docx'
        para_indices_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 23, 24]
        app.remove_paragraphs_by_index(file_path, output_path, para_indices_to_remove)

        convertapi.api_credentials = 'secret_KWmzJQRIOe8M5ueS'
        convertapi.convert('pdf', {'File': output_path}, from_format='docx').save_files('ScannedPDF_Final')

        # Text analysis and translation
        pdf_path = r"ScannedPDF_Final/TextOp.pdf"
        output_json_path = r"extracted_text_with_coordinates.json"
        app.extract_text_with_coordinates(pdf_path, output_json_path)
        app.add_text_and_character_count(pdf_path, output_json_path)
        app.translate_and_insert_newlinesh(pdf_path, output_json_path, dest_language='hi')
        font_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"
        
        output_pdf_path = r"TranslatedOutput.pdf"
        app.create_pdf_with_images("Header.jpg", "Footer.jpg", output_pdf_path)
        
        app.create_translated_pdf(output_json_path, output_pdf_path, font_path)

        # Return processed PDF as bytes
        with open(output_pdf_path, "rb") as f:
            return f.read()
    finally:
        os.unlink(temp_pdf_path)

# Streamlit UI
st.title("PDF Linguist")
st.markdown("Upload a Scanned file and download the translated result.")

uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_pdf is not None:
    st.success(f"Uploaded file: {uploaded_pdf.name}")
    input_pdf_bytes = uploaded_pdf.read()

    # Layout for preview and header/footer selection
    st.markdown("### Page Preview:")
    try:
        preview_buf = preview_pdf(input_pdf_bytes)
        st.image(preview_buf, caption="Preview with Selected Areas and Grid", use_column_width=True)
    except Exception as e:
        st.error(f"Error generating preview: {e}")
    col1, col2 = st.columns([1, 1])
    with col1:
        
        st.markdown("### Header Selection:")
        x0_h = st.number_input("Header Top-left x (x0):", step=1, value=0, key="x0_h")
        y0_h = st.number_input("Header Top-left y (y0):", step=1, value=0, key="y0_h")
        width_h = st.number_input("Header Width:", step=1, value=100, key="width_h")
        height_h = st.number_input("Header Height:", step=1, value=50, key="height_h")

        if st.button("Confirm Header"):
            app.save_headers(r"ScannedPDF_Final\page_1.jpg",x0_h, y0_h,width_h,height_h)
            st.success("Header area selected successfully.")

    with col2:

        st.markdown("### Footer Selection:")
        x0_f = st.number_input("Footer Top-left x (x0):", step=1, value=0, key="x0_f")
        y0_f = st.number_input("Footer Top-left y (y0):", step=1, value=0, key="y0_f")
        width_f = st.number_input("Footer Width:", step=1, value=100, key="width_f")
        height_f = st.number_input("Footer Height:", step=1, value=50, key="height_f")
        
        if st.button("Confirm Footer"):
            app.save_footers(r"ScannedPDF_Final\page_1.jpg",x0_f, y0_f,width_f,height_f)
            st.success("Footer area selected successfully.")

    st.markdown("### Translate PDF:")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Kannada"):
            st.markdown("### Processing...")
            try:
                processed_pdf_bytes = process_pdfk(input_pdf_bytes)
                st.success("Processing complete!")
                st.markdown("### Download the Translated PDF")
                st.download_button(
                    label="Download",
                    data=processed_pdf_bytes,
                    file_name=f"Translated_{uploaded_pdf.name}",
                    mime="application/pdf",
                )
            except Exception as e:
                st.error(f"Error during processing: {e}")

    with col2:
        if st.button("Hindi"):
            st.markdown("### Processing...")
            try:
                processed_pdf_bytes = process_pdfh(input_pdf_bytes)
                st.success("Processing complete!")
                st.markdown("### Download the Translated PDF")
                st.download_button(
                    label="Download",
                    data=processed_pdf_bytes,
                    file_name=f"Translated_{uploaded_pdf.name}",
                    mime="application/pdf",
                )
            except Exception as e:
                st.error(f"Error during processing: {e}")
