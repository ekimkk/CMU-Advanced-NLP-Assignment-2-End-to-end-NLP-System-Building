import requests
import json

def get_pdf_by_url(url: str, output_path: str) -> None:
    """
    Download a PDF from a given URL

    Args:
        url (str): The URL of the PDF to download
        output_path (str): The path to save the downloaded PDF
    """
    try:
        response = requests.get(url, stream=True)
        with open(output_path, "wb") as output_file:
            for chunk in response.iter_content(chunk_size=128):
                output_file.write(chunk)
    except Exception as e:
        print(f"Error downloading PDF from {url}: {e}")

# Path to your JSON file
file_path = "paper_data/paper_details.txt"


# Function to extract open access PDF URLs
def extract_openaccesspdf_urls(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    urls = []
    for author in data.values():
        for papers in author:
            for paper in papers.get("data", []):
                open_access_pdf = paper.get("openAccessPdf")
                if open_access_pdf and open_access_pdf.get("url"):
                    urls.append(open_access_pdf["url"])

    return urls


# Extract URLs
urls = extract_openaccesspdf_urls(file_path)
for i, url in enumerate(urls):
    print(f"Downloading paper {i+1}/{len(urls)}")
    get_pdf_by_url(url, f"pdf_data/paper_{i}.pdf")