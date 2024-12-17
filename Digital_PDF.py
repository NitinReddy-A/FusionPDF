import streamlit as st
import fitz 
from io import BytesIO
import convertapi
from DigitalPDF_Final import app
import tempfile
import os



def process_pdfk(input_pdf_bytes):
    """
    Process the uploaded PDF to extract text, apply translations, and generate output.
    """
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(input_pdf_bytes)
            temp_pdf_path = temp_pdf.name

        
        # Text analysis and translation
        pdf_path = temp_pdf_path
        output_json_path = r"extracted_text_with_coordinates.json"
        app.extract_text_with_coordinates(pdf_path, output_json_path)
        app.add_text_and_character_count(pdf_path, output_json_path)
        app.translate_and_insert_newlinesk(pdf_path, output_json_path, dest_language='kn')
        font_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"
        
        output_pdf_path = r"TranslatedOutput.pdf"
        app.create_pdf_with_images(pdf_path, output_pdf_path)
        
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

        
        # Text analysis and translation
        pdf_path = temp_pdf_path
        output_json_path = r"extracted_text_with_coordinates.json"
        app.extract_text_with_coordinates(pdf_path, output_json_path)
        app.add_text_and_character_count(pdf_path, output_json_path)
        app.translate_and_insert_newlinesh(pdf_path, output_json_path, dest_language='hi')
        font_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"
        
        output_pdf_path = r"TranslatedOutput.pdf"
        app.create_pdf_with_images(pdf_path, output_pdf_path)
        
        app.create_translated_pdf(output_json_path, output_pdf_path, font_path)

        # Return processed PDF as bytes
        with open(output_pdf_path, "rb") as f:
            return f.read()
    finally:
        os.unlink(temp_pdf_path)


def process_pdfr(input_pdf_bytes):
    """
    Process the uploaded PDF to extract text, apply translations, and generate output.
    """
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(input_pdf_bytes)
            temp_pdf_path = temp_pdf.name

        # Text analysis and translation
        pdf_path = temp_pdf_path
        output_json_path = r"extracted_text_with_coordinates.json"
        app.extract_text_with_coordinates(pdf_path, output_json_path)
        app.add_text_and_character_count(pdf_path, output_json_path)
        app.translate_and_insert_newlinesr(pdf_path, output_json_path, dest_language='ru')
        font_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"
        
        output_pdf_path = r"TranslatedOutput.pdf"
        app.create_pdf_with_images(pdf_path, output_pdf_path)
        
        app.create_translated_pdf(output_json_path, output_pdf_path, font_path)

        # Return processed PDF as bytes
        with open(output_pdf_path, "rb") as f:
            return f.read()
    finally:
        os.unlink(temp_pdf_path)

# Streamlit UI
st.title("PDF Linguist")
st.markdown("Upload a Digital PDF and download the translated result.")

uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_pdf is not None:
    st.success(f"Uploaded file: {uploaded_pdf.name}")
    input_pdf_bytes = uploaded_pdf.read()

    st.markdown("### Translate PDF:")
    col1, col2, col3 = st.columns([1, 1, 1])
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

    with col3:
        if st.button("Russian"):
            st.markdown("### Processing...")
            try:
                processed_pdf_bytes = process_pdfr(input_pdf_bytes)
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
