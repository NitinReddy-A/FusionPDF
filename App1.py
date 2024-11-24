import streamlit as st
import fitz  # PyMuPDF
from googletrans import Translator
import numpy as np
import matplotlib.pyplot as plt


def render_pdf_page_with_pixel_scale(pdf_file, page_number=0):
    """
    Renders a page from a PDF file as an image with pixel scale and gridlines.

    Args:
        pdf_file (bytes): The PDF file as raw byte data.
        page_number (int): The page number to render (0-based index).

    Returns:
        matplotlib.figure.Figure: The matplotlib figure object with the visualization.
    """
    # Open the PDF from raw bytes
    doc = fitz.open(stream=pdf_file, filetype="pdf")

    # Validate page number
    if page_number < 0 or page_number >= len(doc):
        raise ValueError(f"Invalid page number: {page_number}. The PDF has {len(doc)} pages.")

    # Load the specified page
    page = doc[page_number]

    # Set a matrix to scale the page by a zoom factor (2 = 200% size)
    mat = fitz.Matrix(2, 2)
    pix = page.get_pixmap(matrix=mat)

    # Convert pixmap to NumPy array
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)

    # Convert to grayscale if the image is RGB
    if img.shape[-1] == 3:  # Check if the image has RGB channels
        img = np.mean(img, axis=2).astype(np.uint8)  # Convert to grayscale

    # Get image dimensions
    height, width = img.shape[:2]

    # Create the figure
    fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size for better visibility
    ax.imshow(img, cmap="gray")  # Display the image

    # Add axes with pixel scale
    ax.set_xticks(range(0, width + 1, max(1, width // 10)))  # X-axis scale
    ax.set_yticks(range(0, height + 1, max(1, height // 10)))  # Y-axis scale

    # Add grid lines for better visualization
    ax.grid(color="blue", linestyle="--", linewidth=0.15)

    # Add labels and title
    ax.set_xlabel("Width (pixels)")
    ax.set_ylabel("Height (pixels)")
    ax.set_title(f"Page {page_number + 1} with Pixel Scale", fontsize=14)

    return fig


def main():
    # App branding
    st.title("PDFLinguist")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file is not None:
        st.write(f"Uploaded File: **{uploaded_file.name}**")

        # Read the uploaded file as bytes
        pdf_data = uploaded_file.read()

        # Open the PDF
        doc = fitz.open(stream=pdf_data, filetype="pdf")
        num_pages = len(doc)

        # Page selection
        page_number = st.selectbox("Select a page to visualize:", range(1, num_pages + 1)) - 1

        # Display the image with pixel scale
        fig = render_pdf_page_with_pixel_scale(pdf_data, page_number)
        st.pyplot(fig)

        # Selection method toggle
        st.markdown("### Selection Method")
        selection_method = st.radio(
            "Choose how to select an area for translation:",
            ("Enter pixel values manually",)
        )

        if selection_method == "Enter pixel values manually":
            st.markdown("#### Enter the pixel values for Header:")
            x0 = st.number_input("Top-left x-coordinate (x0):", min_value=0, step=1)
            y0 = st.number_input("Top-left y-coordinate (y0):", min_value=0, step=1)
            width = st.number_input("Width of the area (from x0):", min_value=1, step=1)
            height = st.number_input("Height of the area (from y0):", min_value=1, step=1)
            st.markdown("#### Enter the pixel values for Footer:")
            x1 = st.number_input("Top-left x-coordinate (x1):", min_value=0, step=1)
            y1 = st.number_input("Top-left y-coordinate (y1):", min_value=0, step=1)
            width1 = st.number_input("Width of the area (from x1):", min_value=1, step=1)
            height1 = st.number_input("Height of the area (from y1):", min_value=1, step=1)

            if st.button("Translate"):
                rect = fitz.Rect(x0, y0, x0 + width, y0 + height)
                st.warning("Translation functionality is under development.")
                # handle_translation(doc, page_number, rect)

        st.markdown("### Translation Output")
        st.info("Your translation output will be displayed here after selecting the area.")


if __name__ == "__main__":
    main()
