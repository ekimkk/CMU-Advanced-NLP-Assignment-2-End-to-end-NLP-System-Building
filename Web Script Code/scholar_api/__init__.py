"""
This module provides a function to generate a mapping of faculty names to their publications in a specific year. It uses google scholar to search for the author and their publications in a specific year. The result is saved to a file.

Example result:
{
    "Yonatan Bisk": [{
        "title": "WebArena: A Realistic Web Environment for Building Autonomous Agents",
        "pub_year": "2023",
        "citation": "The Twelfth International Conference on Learning Representations (ICLR), 2023"
    }]
}
"""

import json
from api import search_author_by_name_api, search_author_publication_in_year_api


def generate_author_pub_map(faculty_names: list, output_path: str, year: str) -> None:
    """
    Generate a mapping of faculty names to their publications in a specific year

    Example result:
        {
            "Yonatan Bisk": [{
                "title": "WebArena: A Realistic Web Environment for Building Autonomous Agents",
                "pub_year": "2023",
                "citation": "The Twelfth International Conference on Learning Representations (ICLR), 2023"
            }]
        }

    Args:
        faculty_names (list): The list of faculty names to search for
        output_path (str): The path to save the faculty name to publication mapping

    Returns:
        None
    """
    faculty_name_pub_map = {}

    for faculty in faculty_names:
        print(
            f"Faculty: {faculty}, Percentage of completion: {faculty_names.index(faculty)/len(faculty_names)*100:.2f}%"
        )
        author = search_author_by_name_api(faculty)
        if author:
            faculty_name_pub_map[faculty] = search_author_publication_in_year_api(
                author, year
            )
        else:
            faculty_name_pub_map[faculty] = []

    # save the faculty name to author ID mapping to a file
    with open(output_path, "w") as file:
        file.write(json.dumps(faculty_name_pub_map, indent=4))


# Example usage
if __name__ == "__main__":
    faculty_names = [
        "Yonatan Bisk",
        "Ralf Brown",
        "Jamie Callan",
        "Justine Cassell",
        "Mona Diab",
        "Fernando Diaz",
        "Scott Fahlman",
        "Robert Frederking",
        "Daniel Fried",
        "Anatole Gershman",
        "Alexander Hauptmann",
        "Daphne Ippolito",
        "Lori Levin",
        "Lei Li",
        "Teruko Mitamura",
        "Louis-Philippe Morency",
        "David Mortensen",
        "Graham Neubig",
        "Eric Nyberg",
        "Kemal Oflazer",
        "Bhiksha Raj",  # Bhiksha Ramakrishnan
        "Carolyn Rosé",
        "Alexander Rudnicky",
        "Maarten Sap",
        "Michael Shamos",
        "Rita Singh",  # not found on google scholar
        "Emma Strubell",
        "Alexander Waibel",
        "Shinji Watanabe",
        "Sean Welleck",
        "Eric Xing",  # Eric P. Xing
        "Chenyan Xiong",
        "Yiming Yang",
    ]
    generate_author_pub_map(faculty_names, "faculty_name_pub_map.txt", "2023")
