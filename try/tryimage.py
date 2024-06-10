# Import required dependencies
import fitz
import os
from PIL import Image
import io

# Define path to PDF file
file_path = r"C:\Users\len\OneDrive\Desktop\Repo\FusionPDF\try\demo.pdf"

# Define path for saved images
images_path = 'images/'

# Create the directory if it doesn't exist
if not os.path.exists(images_path):
    os.makedirs(images_path)

# Open PDF file
pdf_file = fitz.open(file_path)

# Get the number of pages in PDF file
page_nums = len(pdf_file)

# Create empty list to store images information
images_list = []

# Extract all images information from each page
for page_num in range(page_nums):
    page_content = pdf_file[page_num]
    images_list.extend(page_content.get_images(full=True))

# Raise error if PDF has no images
if len(images_list) == 0:
    raise ValueError(f'No images found in {file_path}')

# Save all the extracted images
for i, img in enumerate(images_list, start=1):
    # Extract the image object number
    xref = img[0]
    # Extract image
    base_image = pdf_file.extract_image(xref)
    # Store image bytes
    image_bytes = base_image['image']
    # Store image extension
    image_ext = base_image['ext']
    # Generate image file name
    image_name = str(i) + '.' + image_ext

    # Convert image to a common format if necessary
    if image_ext.lower() in ['jpx', 'jp2', 'j2k']:
        # Open image using PIL
        image = Image.open(io.BytesIO(image_bytes))
        # Handle images with alpha channel (transparency)
        if image.mode == 'RGBA':
            # Convert to RGB
            image = image.convert('RGB')
        image_name = str(i) + '.png'
        image.save(os.path.join(images_path, image_name), 'PNG')
    elif image_ext.lower() == 'png':
        # For PNG images, ensure they are properly converted if needed
        image = Image.open(io.BytesIO(image_bytes))
        if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
            # Convert to RGB
            image = image.convert('RGBA').convert('RGB')
        image_name = str(i) + '.png'
        image.save(os.path.join(images_path, image_name), 'PNG')
    else:
        # Save image as is
        with open(os.path.join(images_path, image_name), 'wb') as image_file:
            image_file.write(image_bytes)
