import time
import requests

api_key = "mqUKFguzWZ245BssnO3D67uA9l080ZVqFgOOwuZc"
base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
session = requests.Session()
session.headers.update({"x-api-key": api_key})


def get_paper_info_api(search_string: str, limit: str, retry_times: int) -> dict:
    """
    Search paper details (Fields: openAccessPdf,title,abstract,publicationVenue,tldr) based on the search string, and limit the number of results. It uses the Semantic Scholar API.
    Year is specified as 2023.

    Since we may fail because of too many requests, we retry the request for a specified number of times. Each time we wait for 3 seconds before retrying.

    Args:
        search_string (str): The search string to use
        limit (str): The maximum number of results to return
        retry_times (int): The number of times to retry the request if it fails

    Returns:
        dict: The paper details if the request was successful, None otherwise
    """
    if retry_times < 0:
        return None

    query_params = {
        "query": search_string,
        "fields": "openAccessPdf,title,abstract,publicationVenue,tldr",
        "year": "2023",
        "limit": limit,
    }
    response = session.get(base_url, params=query_params)

    # Check for a successful response
    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Error fetching data for {search_string}: {response.status_code}, {response.text}. Retry: {retry_times}"
        )
        # Wait for 3 seconds before retrying
        time.sleep(3)
        return get_paper_info_api(search_string, limit, retry_times - 1)
