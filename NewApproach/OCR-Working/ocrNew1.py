import time
import requests

# Set your API key and endpoint
API_KEY = 'wx6tkon97x0q5qyl8'
RESULT_URL = 'https://techhk.aoscdn.com/api/tasks/document/ocr/'

# Replace with the task_id obtained from the previous step
task_id = '80419355-6fb2-4f3b-a0ed-f95de9cbd6ea'  # Replace with your actual task_id

headers = {
    'X-API-KEY': API_KEY
}

# Function to check the status of the OCR task
def check_ocr_status(task_id):
    response = requests.get(f"{RESULT_URL}{task_id}", headers=headers)
    return response.json()

# Query the result until it's complete
for _ in range(30):  # Check for up to 30 seconds
    result = check_ocr_status(task_id)
    state = result.get('data', {}).get('state')
    
    if state == 1:  # State 1 indicates completion
        file_url = result.get('data', {}).get('file')
        if file_url:
            file_response = requests.get(file_url)
            if file_response.status_code == 200:
                with open('output.docx', 'wb') as output_file:
                    output_file.write(file_response.content)
                print("OCR conversion successful! Output saved as 'output.docx'.")
            else:
                print(f"Error downloading the file: {file_response.status_code} - {file_response.text}")
        else:
            print("Error: File URL not found in the response.")
        break
    elif state < 0:  # Any negative state indicates failure
        print(f"OCR conversion failed with state: {state}.")
        break
    else:
        print(f"OCR conversion in progress... {result.get('data', {}).get('progress', 0)}% complete.")
        time.sleep(1)  # Wait for 1 second before checking again
