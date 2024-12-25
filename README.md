# **PDF Linguist** : A Seamless PDF Content Extraction, Merging and Translation Tool

## Overview

PDF Linguist is a comprehensive tool designed for seamless extraction of text and images from PDF documents, with the ability to translate the extracted content and generate both PDF and Word documents. This tool preserves the original layout, formatting, and images, making it ideal for document translation and content manipulation. The tool supports two distinct functionalities:

1. **Translation of Digital PDFs**
2. **Translation of Scanned PDFs**

Both options are integrated into a single application, allowing users to select the desired mode for processing their PDF files.

## Features

### Digital PDFs

- **Extract Text and Images**: Efficiently extracts searchable text and embedded images from digital PDFs.
- **Translate Content**: Translates extracted text into a specified language.
- **Render Complex Scripts** (Indic languages): Accurately renders complex scripts like Devanagari and other Asian languages, utilizing the **HarfBuzz software package** to handle intricate ligatures and unicode combinations.
- **Merge and Preserve Layout**: Merges translated text and extracted images into a new PDF, maintaining the original layout and formatting.
- **Generate Multiple Formats**: Creates both PDF and Word (DOCX) documents from the translated content.
- **Multi-page Handling**: Supports extraction and processing across multiple pages of a PDF.



### Scanned PDFs

- **OCR-Based Text Extraction**: Utilizes Tesseract OCR to extract text from scanned PDF images.
- **Customizable Content Cropping**: Users can specify dimensions for preserving headers and footers or removing irrelevant content.
- **Translate Content**: Translates OCR-extracted text into a specified language, ensuring high-quality rendering of regional languages.
- **Merge and Preserve Layout**: Combines the translated text with the scanned PDF layout for a seamless final output.
- **Generate Multiple Formats**: Outputs the translated content as PDF and Word (DOCX) documents.

## Installation

Clone the repository:

```bash
git clone https://github.com/NitinReddy-A/PDFLinguist.git
```

Navigate to the project directory:

```bash
cd PDFLinguist
```

Setup a virtual environment (Optional):

```bash
python -m venv virtual-env
virtual-env\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Prepare Your PDF Document

- Place the PDF document you want to process in the **documents/** directory.

### Run the Application

- Launch the Streamlit app:

```bash
streamlit run app.py
```

- Select the type of PDF to process:
  - **Digital PDF**: For PDFs with searchable text.
  - **Scanned PDF**: For image-based PDFs requiring OCR.

### Digital PDFs

1. **Upload PDF**: Use the file uploader to select the PDF.
2. **Select Language**: Choose the target language for translation.
3. **Process**: Click the button to extract, translate, and reassemble the PDF.
4. **Download Output**: Save the translated PDF or DOCX from the provided download links.

### Scanned PDFs

1. **Upload PDF**: Use the file uploader to select the scanned PDF.
2. **Crop Dimensions (Optional)**: Define areas to select headers or footers for cleaner text extraction.
3. **Select Language**: Choose the target language for translation.
4. **Process**: Click the button to extract text via OCR, translate, and reassemble the PDF.
5. **Download Output**: Save the translated PDF or DOCX from the provided download links.

## Note

- You need an API key for ConvertAPI and LightPDF API. Update the script with your API key.
- Modify the destination language code as needed in the translation function.

## Dependencies

- **Streamlit**: For building the interactive web application.
- **PyMuPDF (fitz)**: For handling digital PDFs and converting pages to images.
- **Pillow (PIL)**: For image processing tasks such as cropping and resizing.
- **PyTesseract**: For OCR-based text extraction from scanned PDFs.
- **Googletrans**: For language translation.
- **FPDF**: For generating translated PDF files.
- **PDF2Image**: For converting PDF pages to images for OCR.



## APIs Utilized

- **LightPDF API**: Supports  conversions between Scanned PDF into other formats using OCR.
- **ConvertAPI**: Facilitates conversions between PDF and other formats.



## Output Files

- Translated PDFs and DOCX files are saved in the **documents/** directory.
- Both formats retain the layout and formatting of the original document, excluding unwanted sections like headers and footers.

## Summary

PDF Linguist simplifies the processing of both digital and scanned PDFs, offering high accuracy in content extraction and translation while maintaining the document's original structure. The dual-mode functionality ensures versatility, catering to diverse user needs in document management and translation.

