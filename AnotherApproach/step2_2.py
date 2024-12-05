import fitz
import pymupdf
import os

# Open the PDF document
doc = fitz.open(r"TranslatedOutput.pdf") #---------> Specify the input file
new_pdf_path = r"enOp.pdf" #-----------> Specify the output file

# Create a new PDF document
new_doc = fitz.open()

# Create the images directory if it doesn't exist
if not os.path.exists('images/'):
    os.mkdir('images/')

# FOR IMAGES ------------------------------------------>
for page_index in range(doc.page_count):
    page = doc.load_page(page_index)
    # Get the original page
    original_page = doc.load_page(page_index)

    # Create a new page with the same size as the original page
    new_page = new_doc.new_page(width=original_page.rect.width, height=original_page.rect.height)

    # Get the list of images on the page
    image_list = page.get_images(full=True)

    # Iterate through each image and save it in the images folder
    for img_index, img in enumerate(image_list):
        try:
            if img[1] == 0:
                print(img)
                bbox = page.get_image_bbox(img)
                xref = img[0] # get the XREF of the image
                pix = pymupdf.Pixmap(doc, xref) # create a Pixmap
                if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
                    pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
                pix.save(f"images/page{page_index}-image{img_index}.png") # save the image as png
                pix = None
                new_page.insert_image(bbox, stream=open(f"images/page{page_index}-image{img_index}.png", "rb").read())
                print(f"Image {img_index} on page {page_index}: {bbox}")
        except Exception as e:
            print(f"An error occurred while extracting image: {e}")

# Save the new PDF document
new_doc.save(new_pdf_path)
new_doc.close()