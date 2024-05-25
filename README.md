# ******FusionPDF****** : A Seamless PDF Content Extraction and Merging Tool

## Overview
This tool allows you to seamlessly extract text and images from a PDF document, and merge them into a new PDF while preserving the original layout, formatting, and images.

## Features
  Extract text and images from PDF documents.
  
  Merge extracted text and images into a new PDF.
  
  Preserve the layout, formatting, and images of the original PDF.
  
  Handle multiple pages in the original PDF.
  
## Installation
Clone the repository:

    git clone https://github.com/NitinReddy-A/FusionPDF.git
Navigate to the project directory:

    cd FusionPDF
Steup a virtual env(Optional):

    python -m venv virtual-env
    virtual-env\Scripts\activate
Install the required dependencies:

    pip install -r requirements.txt
## Usage
Import the necessary modules:

    import fitz  # PyMuPDF
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from PIL import Image
    import io
    import os
Extract content from a PDF document:

    content_list = extract_content(pdf_path)
Create a new PDF with the extracted content:

    create_new_pdf(new_pdf_path, content_list, pdf_path)
Replace pdf_path with the path to the original PDF, new_pdf_path with the desired path for the new PDF, and content_list with the extracted content.

## Contributing
Contributions are welcome! Please follow these steps:

  Fork the repo.

  Create a new branch (git checkout -b feature/new-feature).
  
  Make your changes.
  
  Commit your changes (git commit -am 'Add new feature').
  
  Push to the branch (git push origin feature/new-feature).
  
  Create a new Pull Request.

## Acknowledgements
  PyMuPDF - Python bindings for the MuPDF library.
  
  ReportLab - Python PDF generation library.
  
  Pillow - Python Imaging Library (PIL) fork.
