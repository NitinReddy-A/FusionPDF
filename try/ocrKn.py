# Step 1: Install required packages
# Ensure tesseract and required libraries are installed
# pip install pytesseract pillow

# Step 2: Import libraries
import pytesseract
from PIL import Image
from tkinter import Tk, filedialog
import os

# Step 3: Define the function to preserve layout
def convert_image_to_pdf_with_layout(input_image_path, output_pdf_path):
    # Set Kannada language for Tesseract
    lang = "kan"

    # Open the input image
    image = Image.open(input_image_path)

    # Perform OCR to generate a PDF with preserved layout
    pdf_data = pytesseract.image_to_pdf_or_hocr(image, lang=lang, config='--psm 1', extension='pdf')

    # Write the PDF data to a file
    with open(output_pdf_path, 'wb') as pdf_file:
        pdf_file.write(pdf_data)
    
    print(f"PDF with preserved layout saved to: {output_pdf_path}")

# Step 4: Use a file dialog for image selection
Tk().withdraw()  # Hide the root window
print("Select an image file to process:")
input_image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

if input_image_path:
    # Set the output path
    output_pdf_path = os.path.splitext(input_image_path)[0] + "_layout_preserved.pdf"

    # Step 5: Run the function
    convert_image_to_pdf_with_layout(input_image_path, output_pdf_path)
    print(f"Output saved at: {output_pdf_path}")
else:
    print("No file selected.")
