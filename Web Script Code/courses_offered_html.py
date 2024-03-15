from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def course_offered(urls_sections, filename):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    with open(filename, 'w') as file:
        for url, section_header in urls_sections:
            try:
                # Navigate to the webpage
                driver.get(url)

                # Wait for JavaScript to load and for the table to be fully rendered
                time.sleep(5)  # Adjust the sleep time as necessary

                # Write the section header
                file.write(section_header)

                # Locate the table body using the provided XPath
                table_body = driver.find_element(By.XPATH,
                                                 '/html/body/p[3]/b/table/tbody')

                rows = table_body.find_elements(By.TAG_NAME, 'tr')
                for row in rows:
                    cells = row.find_elements(By.TAG_NAME, 'td')
                    row_data = [cell.text for cell in cells]
                    file.write("\t".join(row_data) + "\n")

                file.write("\n\n")  # Leave a blank space after each section

            except Exception as e:
                print(f"An error occurred while processing {url}: {e}")

    # Close the browser outside the loop
    driver.quit()


# Define the URLs and section headers
urls_sections = [
    ('https://enr-apps.as.cmu.edu/assets/SOC/sched_layout_spring.htm',
     'Run Date: 23-feb-2024\nSemester: Spring 2024'),
    ('https://enr-apps.as.cmu.edu/assets/SOC/sched_layout_summer_1.htm',
     'Run Date: 23-feb-2024\nSemester: Summer One/All 2024'),
    ('https://enr-apps.as.cmu.edu/assets/SOC/sched_layout_summer_2.htm',
     'Run Date: 23-feb-2024\nSemester: Summer Two 2024'),
    ('https://enr-apps.as.cmu.edu/assets/SOC/sched_layout_fall.htm',
     'Run Date: 23-feb-2024\nSemester: Fall 2023'),
]

filename = 'merged_courses_offered.txt'

# Scrape data from each URL and merge into one text file
course_offered(urls_sections, filename)
