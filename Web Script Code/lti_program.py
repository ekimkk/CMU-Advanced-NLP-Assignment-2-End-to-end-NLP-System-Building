from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape_programs_js(driver, filename):
    js_script = """
    var data = [];
    var programBlocks = document.querySelectorAll('div[id^="block-quicktabs-"]');
    programBlocks.forEach(function(block) {
        var title = block.querySelector('h2') ? block.querySelector('h2').innerText : 'No title';
        var contents = [];
        var tabs = block.querySelectorAll('div[id^="qt-"]');
        tabs.forEach(function(tab) {
            contents.push(tab.querySelector('article > div > div > div').innerText);
        });
        data.push({title: title, contents: contents});
    });
    return data;
    """

    # Execute the JavaScript to scrape the data
    scraped_data = driver.execute_script(js_script)

    # Write the scraped data to a file
    with open(filename, 'w') as file:
        for program in scraped_data:
            file.write("----------------------\n")
            file.write(program['title'] + "\n\n")
            for content in program['contents']:
                file.write(content + "\n\n")
            file.write("----------------------\n")


# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Define the URL
    url = 'https://lti.cs.cmu.edu/learn#quicktabs-phd_lti=0&quicktabs-language_technologies=3'  # Replace with the actual URL

    # Navigate to the webpage
    driver.get(url)

    # Wait for the content to be loaded
    time.sleep(5)  # Adjust based on the actual load time of the page

    # Specify the output filename
    filename = 'program_details.txt'

    # Scrape the program data
    scrape_programs_js(driver, filename)

except Exception as e:
    print(f"An error occurred while scraping {url}: {e}")

finally:
    # Close the browser
    driver.quit()
