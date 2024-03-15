from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def cmu_important_date(url, filename):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Navigate to the webpage
        driver.get(url)

        # Wait for the content section to be loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "content"))
        )

        # Use JavaScript to extract the information
        js_script = """
        var data = [];
        var sections = document.querySelectorAll('#content > div.content > div');
        sections.forEach(function(section) {
            var header = section.querySelector('h2, h3');
            if (header) {
                var title = header.innerText;
                var tableTexts = Array.from(section.querySelectorAll('table')).map(function(table) {
                    return table.innerText;
                });
                data.push(title + "\\n" + tableTexts.join("\\n"));
            }
        });
        return data.join("\\n\\n");
        """
        content_data = driver.execute_script(js_script)

        # Open the file for writing
        with open(filename, 'w') as file:
            # Write the extracted data
            file.write(content_data)

    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")

    finally:
        # Close the browser
        driver.quit()

# Define the URL
url = 'https://www.cmu.edu/hub/calendar/important-dates.html'

# Specify the output filename
filename = 'cmu_important_date.txt'

# Scrape data from the URL and write it into a text file
cmu_important_date(url, filename)
