import requests
import time

def create_ocr_task(api_key, file_path, output_format='docx'):
    """
    Creates an OCR task for a scanned document.
    
    :param api_key: The API key for authentication.
    :param file_path: The path to the scanned PDF file.
    :param output_format: The desired output format (default is 'docx').
    :return: The task ID if successful, otherwise an error message.
    """
    OCR_CONVERSION_URL = 'https://techhk.aoscdn.com/api/tasks/document/ocr'
    
    # Prepare the request headers and payload
    headers = {'X-API-KEY': api_key}
    files = {'file': open(file_path, 'rb')}
    data = {'format': output_format}
    
    try:
        # Send a POST request to create the OCR conversion task
        response = requests.post(OCR_CONVERSION_URL, headers=headers, data=data, files=files)
        
        # Check if the request was successful
        if response.status_code == 200:
            task_id = response.json().get('data', {}).get('task_id')
            if task_id:
                return task_id
            else:
                return f"Error: {response.json().get('message')}"
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"


def perform_ocr_task(task_id, api_key, result_url, output_path='o.docx', timeout=30):
    """
    Perform OCR task by checking status and downloading the result.

    :param task_id: ID of the OCR task
    :param api_key: API key for authentication
    :param result_url: URL endpoint for the OCR task
    :param output_path: Path to save the output file
    :param timeout: Maximum time in seconds to wait for task completion
    """
    headers = {'X-API-KEY': api_key}
    
    for _ in range(timeout):
        # Check OCR task status
        response = requests.get(f"{result_url}{task_id}", headers=headers)
        if response.status_code != 200:
            print(f"Error checking OCR status: {response.status_code} - {response.text}")
            return False

        result = response.json()
        state = result.get('data', {}).get('state')

        if state == 1:  # State 1 indicates completion
            file_url = result.get('data', {}).get('file')
            if file_url:
                # Download the file
                file_response = requests.get(file_url)
                if file_response.status_code == 200:
                    with open(output_path, 'wb') as output_file:
                        output_file.write(file_response.content)
                    print(f"OCR conversion successful! Output saved as '{output_path}'.")
                    return True
                else:
                    print(f"Error downloading the file: {file_response.status_code} - {file_response.text}")
                    return False
            else:
                print("Error: File URL not found in the response.")
                return False
        elif state < 0:  # Any negative state indicates failure
            print(f"OCR conversion failed with state: {state}.")
            return False
        else:
            progress = result.get('data', {}).get('progress', 0)
            print(f"OCR conversion in progress... {progress}% complete.")
            time.sleep(1)  # Wait 1 second before checking again

    print("OCR conversion timed out.")
    return False


# Set your API key and file path
API_KEY = 'wx6tkon97x0q5qyl8'
RESULT_URL = 'https://techhk.aoscdn.com/api/tasks/document/ocr/'
pdf_file_path = r'C:\Users\Lenovo\Desktop\repo\FusionPDF\documents\scan1.pdf'

# Step 1: Create OCR Task
task_id = create_ocr_task(API_KEY, pdf_file_path, output_format='docx')

if 'Error' not in task_id:
    print(f"Task created successfully. Task ID: {task_id}")
    
    # Step 2: Retrieve OCR Result
    result_url = perform_ocr_task(task_id=task_id, api_key=API_KEY, result_url=RESULT_URL)
    
    if 'Error' not in result_url:
        print(f"Processed document is available at: {result_url}")
    else:
        print(result_url)
else:
    print(task_id)
