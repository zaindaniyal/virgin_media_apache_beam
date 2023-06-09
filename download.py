import requests

def download_public_file(url, destination):
    """
    Downloads a public file from a given URL and saves it to a destination.

    This function sends a GET request to the specified URL to download the file. 
    If the response status code indicates a successful request, the function writes 
    the response content to a file at the specified destination. If the request is 
    not successful, the function raises an HTTPError.

    Args:
        url (str): The URL of the public file to download.
        destination (str): The local path where the downloaded file should be saved.

    Raises:
        HTTPError: An error occurred during the file download.
    """
    
    response = requests.get(url)
    response.raise_for_status()
    with open(destination, 'wb') as f:
        f.write(response.content)
    print(f"File downloaded to {destination}.")

url = "https://storage.googleapis.com/cloud-samples-data/bigquery/sample-transactions/transactions.csv"
destination = "transactions.csv"

download_public_file(url, destination)
