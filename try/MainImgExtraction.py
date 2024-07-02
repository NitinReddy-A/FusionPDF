import pymupdf
import os

doc = pymupdf.open("documents/demo2.pdf") # open a document

# Create the images directory if it doesn't exist
if not os.path.exists('image/'):
    os.mkdir('image/')

for page_index in range(len(doc)): # iterate over pdf pages
    page = doc[page_index] # get the page
    image_list = page.get_images()

    # print the number of images found on the page
    if image_list:
        print(f"Found {len(image_list)} images on page {page_index}")
    else:
        print("No images found on page", page_index)

    for image_index, img in enumerate(image_list, start=1): # enumerate the image list
        
        if img[1] == 0:
            print(img)
            xref = img[0] # get the XREF of the image
            pix = pymupdf.Pixmap(doc, xref) # create a Pixmap

            if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

            pix.save("image/page_%s-image_%s.png" % (page_index, image_index)) # save the image as png
            pix = None