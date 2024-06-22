from spire.pdf import *
from spire.pdf.common import *

# Create an instance of PdfDocument class
pdf = PdfDocument()

# Load the PDF document
pdf.LoadFromFile("demo.pdf")

# Create a list to store the images
images = []

# Iterate through the pages in the document
for i in range(pdf.Pages.Count):
    # Get a page
    page = pdf.Pages.get_Item(i)
    # Extract the images from the page and store them in the created list
    for img in page.ExtractImages():
        images.append(img)

# Save the images in the list as PNG files
i = 0
for image in images:
    i += 1
    image.Save("Images/Image-{0:d}.png".format(i), "PNG")

pdf.Close()