# Code snippet is using the ConvertAPI Python Client: https://github.com/ConvertAPI/convertapi-python

import convertapi

convertapi.api_secret = '4OYbALQ2RREClhvm'

#Specify the doc path here
doc = 'documents/TranslatedDemo2'

convertapi.convert('docx', {
    'File': f'{doc}.pdf' 
}, from_format = 'pdf').save_files('documents')

convertapi.convert('pdf', {
    'File': f'{doc}.docx' 
}, from_format = 'docx').save_files('documents')