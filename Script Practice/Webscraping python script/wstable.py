import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page
url = 'https://www.marketindex.com.au/highest-dividend-yield'

# Fetch the page
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table by ID or class (modify this based on the actual table's attributes)
table = soup.find('text/javascript')  # You might need to update this

# Read the table into a pandas DataFrame
df = pd.read_html(str(table))[0]

# Write the DataFrame to a text file
df.to_csv('output.csv', sep='\t', index=False)

print('Data written to output.csv')
