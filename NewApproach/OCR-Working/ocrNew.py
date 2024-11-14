import requests

# Set your API key and endpoint
API_KEY = 'wx6tkon97x0q5qyl8'
OCR_CONVERSION_URL = 'https://techhk.aoscdn.com/api/tasks/document/ocr'

# Specify the path to your scanned PDF file
pdf_file_path = r'C:\Users\Lenovo\Desktop\repo\FusionPDF\documents\scan1.pdf'  # Replace with your actual file path

# Prepare the request headers and payload
headers = {
    'X-API-KEY': API_KEY
}

# Prepare the request payload
files = {'file': open(pdf_file_path, 'rb')}
data = {'format': 'docx'}  # Desired output format (e.g., 'docx', 'txt')

# Send a POST request to create the OCR conversion task
response = requests.post(OCR_CONVERSION_URL, headers=headers, data=data, files=files)

# Check if the request was successful
if response.status_code == 200:
    task_id = response.json().get('data', {}).get('task_id')
    if task_id:
        print(f"OCR task created successfully! Task ID: {task_id}")
    else:
        print(f"Error: {response.json().get('message')}")
else:
    print(f"Error: {response.status_code} - {response.text}")
