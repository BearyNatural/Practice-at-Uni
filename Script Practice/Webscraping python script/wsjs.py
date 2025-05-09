from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Setup WebDriver
service = Service('path/to/your/chromedriver')  # Update path to your WebDriver
driver = webdriver.Chrome(service=service)

# URL of the page
url = 'https://www.marketindex.com.au/highest-dividend-yield'

# Open the page
driver.get(url)

# Wait for the JavaScript to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//xpath-to-element')))  # Update XPATH to target

# Now you can parse the page source with BeautifulSoup or directly with Selenium
page_source = driver.page_source

# Close the driver
driver.quit()

# Use BeautifulSoup or Selenium to extract the data you need from page_source here
# For BeautifulSoup:
# soup = BeautifulSoup(page_source, 'html.parser')
# For direct Selenium use, navigate and extract data as needed

# Example of data extraction and conversion to DataFrame would go here

# Remember to replace '//xpath-to-element' with the actual XPATH to the data you are interested in.
