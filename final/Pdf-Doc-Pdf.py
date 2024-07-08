# Code snippet is using the ConvertAPI Python Client: https://github.com/ConvertAPI/convertapi-python

import convertapi

convertapi.api_secret = '4OYbALQ2RREClhvm'

convertapi.convert('docx', {
    'File': 'documents/demo1Kannada.pdf'
}, from_format = 'pdf').save_files('documents')

convertapi.convert('pdf', {
    'File': 'documents/demo1Kannada.docx'
}, from_format = 'docx').save_files('documents')