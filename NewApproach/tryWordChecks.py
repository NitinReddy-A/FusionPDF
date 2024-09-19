from docx import Document

def remove_text_from_docx(file_path):
    # Load the document
    doc = Document(file_path)

    # Loop through the paragraphs and remove the ones containing text to be removed
    for para in doc.paragraphs:
        print(para.text)
        print("-----------------------------------------------------------------------------")

# Example usage:
file_path = 'FinOp.docx'

remove_text_from_docx(file_path)
