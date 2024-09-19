# Code snippet is using the ConvertAPI Python Client: https://github.com/ConvertAPI/convertapi-python

import convertapi

convertapi.api_secret = 'secret_gtNBzUG0bOmJiQU6'

#Specify the file path here
doc = r'NewApproach\op'
#
#convertapi.convert('docx', {
#    'File': f'{doc}.pdf' 
#}, from_format = 'pdf').save_files('documents')

convertapi.convert('pdf', {
    'File': r'NewApproach\op.docx' 
}, from_format = 'docx').save_files('documents')

#ocr

#convertapi.convert('ocr', {
#    'File': 'documents/scan1.pdf'
#}, from_format = 'pdf').save_files('documents')