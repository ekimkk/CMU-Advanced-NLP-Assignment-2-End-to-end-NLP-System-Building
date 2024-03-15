"""
This module provides functionality to generate the paper details data. It parses the faculty name to publication bib mapping from a given file, and generate faculty name to paper title mapping. Then it fetches the paper details using the Semantic Scholar API and saves the result to a file.

Example result:
{"Yonatan Bisk":[{
         "total":1,
         "offset":0,
         "data":[{
               "paperId":"e41482f4ee984f17382f6cdd900df094d928be06",
               "publicationVenue":{
                  "id":"1901e811-ee72-4b20-8f7e-de08cd395a10",
                  "name":"arXiv.org",
                  "alternate_names":[
                     "ArXiv"
                  ],
                  "issn":"2331-8422",
                  "url":"https://arxiv.org"
               },
               "title":"WebArena: A Realistic Web Environment for Building Autonomous Agents",
               "abstract":"abstract",
               "openAccessPdf":{
                  "url":"https://arxiv.org/pdf/2307.13854",
                  "status":"GREEN"
               },
               "tldr":{
                  "model":"tldr@v2.0.0",
                  "text":"tldr"
               }
            }]
      }]}
"""

from data import parse_faculty_name_pub_map, generate_faculty_pub_name_map
from api import get_paper_info_api
from collections import defaultdict
import json


def generate_paper_details_data(
    faculty_name_pub_file_path: str, output_path: str
) -> None:
    """
    Generate the paper details data. It parses the faculty name to publication bib mapping from a given file, and generate faculty name to paper title mapping.
    Then it fetches the paper details using the Semantic Scholar API and saves the result to a file.

    If the faculty name to title mapping is empty, we search by the faculty name and limit the number of results to 20.
    If the faculty name to title mapping is not empty, we search by the paper title and limit the number of results to 3. Because we may get multiple duplicate papers with the same title.

    Args:
        faculty_name_pub_file_path (str): The path to the faculty name to publication mapping file
        output_path (str): The path to save the faculty name to publication mapping
    """
    hm = parse_faculty_name_pub_map(faculty_name_pub_file_path)
    hm = generate_faculty_pub_name_map(hm)

    res = defaultdict(list)
    for faculty, pub_name in hm.items():
        print(f"Processed data: {round((len(res) / len(hm)) * 100, 2)}%")

        if not pub_name:
            details = get_paper_info_api(faculty, "20", 5)
            if details:
                res[faculty] = [details]
        else:
            for name in pub_name:
                details = get_paper_info_api(name, "3", 5)
                if details:
                    res[faculty].append(details)

    with open(output_path, "w") as file:
        file.write(json.dumps(res, indent=4))


if __name__ == "__main__":
    generate_paper_details_data(
        "paper_data/faculty_name_pub_map.txt", "paper_data/paper_details.txt"
    )
