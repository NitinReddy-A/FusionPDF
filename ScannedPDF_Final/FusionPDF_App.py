import streamlit as st
import fitz  # PyMuPDF for PDF processing
from io import BytesIO
import app


def process_pdf(input_pdf_bytes):
    """
    Processes the input PDF and generates an output PDF.

    Args:
        input_pdf_bytes (bytes): Byte data of the input PDF.

    Returns:
        bytes: Byte data of the processed PDF.
    """
    # Open the input PDF
    input_pdf = fitz.open(stream=input_pdf_bytes, filetype="pdf")

    # Create a new PDF to store processed output
    output_pdf = fitz.open()

    # Set your API key and file path
    API_KEY = 'wx6tkon97x0q5qyl8'
    RESULT_URL = 'https://techhk.aoscdn.com/api/tasks/document/ocr/'
    pdf_file_path = input_pdf

    # Step 1: Create OCR Task
    task_id = app.create_ocr_task(API_KEY, pdf_file_path, output_format='docx')

    if 'Error' not in task_id:
        print(f"Task created successfully. Task ID: {task_id}")

        # Step 2: Retrieve OCR Result
        result_url = app.perform_ocr_task(task_id=task_id, api_key=API_KEY, result_url=RESULT_URL)

        print(f"Processed document is available at: {result_url}")

    else:
        print(task_id)

    # Save the processed PDF to a byte stream
    output_stream = BytesIO()
    output_pdf.save(output_stream)
    output_pdf.close()

    # Return processed PDF as bytes
    return output_stream.getvalue()


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


if __name__ == "__main__":
    main()
