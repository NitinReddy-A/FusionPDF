import io
import fitz
import os
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# file path you want to extract images from
file = "demo.pdf"
# open the file
pdf_file = fitz.open(file)

# Create the images directory if it doesn't exist
if not os.path.exists('images/'):
    os.mkdir('images/')

# iterate over pdf page
for page_index in range(len(pdf_file)):
    # get the page itself
    page = pdf_file[page_index]
    image_list = page.get_images()
    # printing number of images found in this page
    if image_list:
        print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
    else:
        print("[!] No images found on page", page_index)
    for image_index, img in enumerate(page.get_images(), start=1):
        # get the XREF of the image
        xref = img[0]
        # extract the image bytes
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
        # get the image extension
        image_ext = base_image["ext"]
        print(image_ext)
        # load it to PIL
        if image_ext != 'png':
            image = Image.open(io.BytesIO(image_bytes))
        # save it to local disk
            image.save(open(f"images/image{page_index+1}_{image_index}.{image_ext}", "wb"))