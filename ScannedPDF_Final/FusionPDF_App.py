import streamlit as st
import fitz  # PyMuPDF for PDF processing
from io import BytesIO
import convertapi
import app


def process_pdf(input_pdf_bytes):
    """
    Processes the input PDF and generates an output PDF.

    Args:
        input_pdf_bytes (bytes): Byte data of the input PDF.

    Returns:
        str: Path to the processed output PDF file.
    """
    # Save the uploaded file as a temporary PDF
    temp_input_pdf_path = "temp_input.pdf"
    with open(temp_input_pdf_path, "wb") as temp_file:
        temp_file.write(input_pdf_bytes)

    # Step 1: Create OCR Task
    API_KEY = 'wx6tkon97x0q5qyl8'
    RESULT_URL = 'https://techhk.aoscdn.com/api/tasks/document/ocr/'
    task_id = app.create_ocr_task(API_KEY, temp_input_pdf_path, output_format='docx')

    if 'Error' not in task_id:
        st.info(f"Task created successfully. Task ID: {task_id}")

        # Step 2: Retrieve OCR Result
        result_url = app.perform_ocr_task(task_id=task_id, api_key=API_KEY, result_url=RESULT_URL)
        st.info(f"Processed document is available at: {result_url}")
    else:
        st.error(task_id)
        return None

    # Process the document further
    intermediate_docx_path = "TextOp.docx"
    output_docx_path = "ProcessedText.docx"
    para_indices_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 23, 24]

    app.remove_paragraphs_by_index(intermediate_docx_path, output_docx_path, para_indices_to_remove)

    # Convert DOCX to PDF
    convertapi.api_secret = 'secret_HVuqFuKW4UsSHiCI'
    pdf_conversion = convertapi.convert('pdf', {'File': output_docx_path}, from_format='docx')
    final_pdf_path = "FinalOutput.pdf"
    pdf_conversion.save_files(final_pdf_path)

    # Additional processing (images, headers/footers, etc.)
    app.convert_pdf_to_jpg(final_pdf_path, "ScannedPDF_Final", zoom=3)
    app.save_headersNfooters("ScannedPDF_Final/page_1.jpg")

    header_image = "Header.jpg"
    footer_image = "Footer.jpg"
    app.create_pdf_with_images(header_image, footer_image, final_pdf_path)

    # Final enhancements and text processing
    output_json_path = "extracted_text_with_coordinates.json"
    app.extract_text_with_coordinates(final_pdf_path, output_json_path)
    app.add_text_and_character_count(final_pdf_path, output_json_path)
    app.translate_and_insert_newlines(final_pdf_path, output_json_path, dest_language='kn')

    font_path = "NotoSansKannada-VariableFont_wdth,wght.ttf"
    app.create_translated_pdf(output_json_path, final_pdf_path, font_path)

    return final_pdf_path


def main():
    st.title("PDF Processor")
    st.markdown("Upload a PDF file, process it, and download the result.")

    # File uploader for input PDF
    uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_pdf is not None:
        st.success(f"Uploaded file: {uploaded_pdf.name}")

        # Read the uploaded PDF as bytes
        input_pdf_bytes = uploaded_pdf.read()

        # Process the PDF
        st.markdown("### Processing...")
        output_pdf_path = process_pdf(input_pdf_bytes)

        if output_pdf_path:
            st.success("Processing complete!")

            # Provide a download link for the processed PDF
            with open(output_pdf_path, "rb") as file:
                processed_pdf_bytes = file.read()
                st.markdown("### Download Processed PDF")
                st.download_button(
                    label="Download",
                    data=processed_pdf_bytes,
                    file_name=f"processed_{uploaded_pdf.name}",
                    mime="application/pdf",
                )
        else:
            st.error("Processing failed. Please check the logs and try again.")


if __name__ == "__main__":
    main()
