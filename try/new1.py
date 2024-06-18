from pdf2docx import Converter

def pdf_to_word(pdf_file, word_file):
    # Create a Converter object
    cv = Converter(pdf_file)
    
    # Convert the PDF to a DOCX file
    cv.convert(word_file, start=0, end=None)
    
    # Close the converter
    cv.close()
    
    print(f"Conversion complete: {word_file}")

# Example usage
pdf_file = 'demo.pdf'
word_file = 'demoh.docx'

pdf_to_word(pdf_file, word_file)
