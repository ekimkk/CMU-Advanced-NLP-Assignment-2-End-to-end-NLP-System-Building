"""
This module provides a function to search for authors by name and a function to search for an author's publication in a specific year.

They use the scholarly library to call google scholar's API to get data.
"""

from scholarly import scholarly


def search_author_by_name_api(author_name: str) -> dict:
    """
    Search for a CMU faculty by name using scholarly api, CMU is appended to the search query to ensure the author is from CMU.
    If the author is not found, then search for the author without appending CMU to the search query.

    Args:
        author_name (str): The name of the author to search for

    Returns:
        dict: The author information if the request was successful, None otherwise
    """
    search_query = scholarly.search_author(author_name + ", Carnegie Mellon University")
    author = next(search_query, None)
    if author is None:
        search_query = scholarly.search_author(author_name)
        author = next(search_query, None)
    return author


def search_author_publication_in_year_api(author: dict, year: str) -> list:
    """
    Search for a CMU faculty's publication in a specific year

    Args:
        author (dict): The author to search for
        year (int): The year to search for

    Returns:
        list: The list of publications if the request was successful, None otherwise
    """
    res = []
    if not author:
        return []
    author = scholarly.fill(author)
    for pub in author["publications"]:
        if "bib" in pub and "pub_year" in pub["bib"] and pub["bib"]["pub_year"] == year:
            res.append(pub["bib"])
    return res