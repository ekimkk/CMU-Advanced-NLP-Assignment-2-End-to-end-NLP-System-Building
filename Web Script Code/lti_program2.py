from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL you want to scrape
url = "https://lti.cs.cmu.edu/learn"

# Open the URL
driver.get(url)

# Let the page load. Adjust the sleep time as necessary.
time.sleep(5)  # Sleep for 5 seconds

# Use the CSS selector to find the element with ID 'page' and get its HTML content
element = driver.find_element(By.CSS_SELECTOR, "#page")
content = element.get_attribute('innerHTML')

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Extract the text
text_only = soup.get_text(separator="\n", strip=True)

# Write the extracted text to a file
with open("test.txt", "w", encoding="utf-8") as file:
    file.write(text_only)

print("Extracted text has been written to extracted_text.txt")

# Close the browser
driver.quit()
