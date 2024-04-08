import requests
import csv
from io import StringIO

def download_csv_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to download CSV. Status code: {response.status_code}")

def save_csv_to_file(csv_data, filename):
    with open(filename, 'w', newline='') as csvfile:
        csvfile.write(csv_data)

if __name__ == "__main__":
    url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240131%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240131T190720Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a72b77b0155ee9352ba802ff9bd624947e29786a8e17fe49aa1131f3894b2b82"

    csv_data = download_csv_from_url(url)
    save_csv_to_file(csv_data, 'Popular_Baby_Names.csv')