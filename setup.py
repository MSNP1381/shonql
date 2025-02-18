import requests
import sys

def download_file(url, local_filename):
    """
    Download a file from a URL and save it to the current directory.
    
    :param url: URL of the file to download.
    :param local_filename: Name to save the downloaded file as.
    :return: The local file name.
    """
    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Check for HTTP errors
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # Filter out keep-alive chunks.
                    file.write(chunk)
    return local_filename

if __name__ == '__main__':


    url = sys.argv[1]
    local_filename = sys.argv[2]

    try:
        url='https://www.antlr.org/download/antlr-4.13.2-complete.jar'
        local_filename='./antlr-4.13.2-complete.jar'
        downloaded_file = download_file(url, local_filename)
        print(f"File successfully downloaded as '{downloaded_file}'")
    except Exception as err:
        print(f"Error downloading file: {err}")
        sys.exit(1)
    try:
        url='https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k/resolve/main/xlam_function_calling_60k.json'
        local_filename='./xlam_function_calling_60k.json'
        downloaded_file = download_file(url, local_filename)
        print(f"File successfully downloaded as '{downloaded_file}'")
    except Exception as err:
        print(f"Error downloading file: {err}")
        sys.exit(1)