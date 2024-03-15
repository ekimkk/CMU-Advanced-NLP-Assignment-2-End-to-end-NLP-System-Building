import json


def parse_faculty_name_pub_map(path: str) -> dict:
    """
    Parse the faculty name to publication mapping from a given file

    Sample file content:
    {
        "Chenyan Xiong": [{
            "title": "Conversational Search",
            "pub_year": "2023",
            "citation": "Neural Approaches to Conversational Information Retrieval, 39-69, 2023"
        }]
    }

    Args:
        path (str): The path to the faculty name to publication mapping file

    Returns:
        dict: The faculty name to publication mapping
    """
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def generate_faculty_pub_name_map(faculty_name_pub_map: dict) -> dict:
    """
    Generate a mapping of publications to faculty names

    Sample output:
    {
        "Chenyan Xiong": ["Paper 1", "Paper 2"]
    }

    Args:
        faculty_name_pub_map (dict): The faculty name to publication mapping

    Returns:
        dict: The publication to faculty name mapping
    """
    faculty_pub_name_map = {faculty: [] for faculty in faculty_name_pub_map}
    for faculty, pubs in faculty_name_pub_map.items():
        for pub in pubs:
            faculty_pub_name_map[faculty].append(pub["title"])
    return faculty_pub_name_map
