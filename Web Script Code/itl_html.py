from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def lti_selenium(url):
    # Setup Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    faculty_info_list = []  # Initialize a list to hold faculty information

    try:
        # Navigate to the webpage
        driver.get(url)

        # Wait for JavaScript to load
        time.sleep(5)  # Adjust the sleep time if necessary

        # Use XPath to locate the table rows
        rows = driver.find_elements(By.XPATH, '//*[@id="content"]/div[3]/div[2]/table/tbody/tr')

        # Iterate through rows to extract information from both columns
        for row in rows:
            # Extract information from the first and second columns
            for col in range(1, 3):  # Adjust based on the number of columns
                try:
                    name_info = row.find_element(By.XPATH, f'./td[{col}]').text
                    faculty_info_list.append(name_info)
                except:
                    # If there is no column, skip
                    continue
    finally:
        # Close the browser
        driver.quit()
    return faculty_info_list

if __name__ == '__main__':
    # Define the URLs and section headers
    urls_sections = [
        ('https://lti.cs.cmu.edu/directory/all/154/1', 'Faculty'),
        ('https://lti.cs.cmu.edu/directory/all/154/1?page=1', 'Faculty'),
        ('https://lti.cs.cmu.edu/directory/all/154/2728', 'Affiliated Faculty'),
        ('https://lti.cs.cmu.edu/directory/all/154/200', 'Adjunct Faculty'),
    ]

    # Open a file to write
    with open('LTI_faculty_directory.txt', 'w') as file:
        for url, section in urls_sections:
            # Write the section header
            file.write(f"=={section}==\n\n")
            # Scrape the information
            faculty_info_list = lti_selenium(url)
            # Write the information to the file, each faculty on a new line
            for info in faculty_info_list:
                file.write(f"{info}\n\n")  # Double newline for clear separation
            file.write("\n")  # Extra newline after each section for clarity
