# Extracting images from pdf ##pikepdf ##new method
from pikepdf import Pdf, Name, PdfImage

old_pdf = Pdf.open("demo.pdf")
page1 = old_pdf.pages[0]
print(list(page1.images.keys())) #['/Im0']

raw_image = page1.images['/Im0']
pdf_img = PdfImage(raw_image)
pdf_img.extract_to(fileprefix="test1")