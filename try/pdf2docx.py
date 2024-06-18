from spire.pdf.common import *
from spire.pdf import *

# Create a PdfDocument object
pdf = PdfDocument()
# Load a PDF file
pdf.LoadFromFile("demo.pdf")

# Convert the PDF file to a Word DOCX file
pdf.SaveToFile("PdfToDocx.docx", FileFormat.DOCX)
# Close the PdfDocument object
pdf.Close()