# Not working
import fitz
import io
import os
from PIL import Image
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
file = 'demo.pdf'
pdf_file = fitz.open(file)
for page_number in range(len(pdf_file)): 
    page=pdf_file[page_number]
    image_list = page.get_images()
    print(image_list)
    
    for image_index, img in enumerate(page.get_images(),start=1):
        print(image_index)
        xref = img[0] 
        # extract image bytes 
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
        # get image extension
        image_ext = base_image["ext"]
        #print(base_image)
# Create a PIL Image object from the image bytes
        pil_image = Image.open(io.BytesIO(image_bytes))

        # Save the image to disk
        image_path = f"image_{page_number}_{image_index}.{image_ext}"
        pil_image.save(image_path)