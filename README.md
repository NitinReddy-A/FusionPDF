# ******FusionTranslate****** : A Seamless PDF Content Extraction, Merging and Translation Tool

## Overview
FusionTranslate is a comprehensive tool designed for seamless extraction of text and images from PDF documents, with the ability to translate the extracted content and generate both PDF and Word documents. This tool preserves the original layout, formatting, and images, making it ideal for document translation and content manipulation.

## Features
  - **Extract Text and Images**: Efficiently extracts text and images from PDF documents.
    
  - **Translate Content**: Translates extracted text into a specified language.
    
  - **Merge and Preserve Layout**: Merges translated text and extracted images into a new PDF, maintaining the original layout and formatting.
    
  - **Generate Multiple Formats**: Creates both PDF and Word (DOCX) documents from the translated content.
    
  - **Multi-page Handling**: Supports extraction and processing across multiple pages of a PDF.
  
## Installation
Clone the repository:

    git clone https://github.com/NitinReddy-A/FusionPDF.git
Navigate to the project directory:

    cd FusionPDF
Setup a virtual env(Optional):

    python -m venv virtual-env
    virtual-env\Scripts\activate
Install the required dependencies:

    pip install -r requirements.txt

## Usage
### Prepare your PDF Document:

  - Place the PDF document you want to process in the **documents/** directory.
### Run the Script:

  - Update the script with the correct input and output file paths.
  - Ensure the appropriate font file is available and correctly referenced.
  - Execute the script to process the PDF document, extract and translate content, and generate new PDF and DOCX files.
### Output Files:

  - The processed files will be saved in the **documents/** directory.
## Note
  - You need an API key for convertapi. Update the script with your API key.
    
  - Modify the destination language code as needed in the translation function.
## Dependencies
  - PyMuPDF
  - googletrans
  - convertapi
