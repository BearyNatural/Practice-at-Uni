import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page
url = 'https://www.marketindex.com.au/highest-dividend-yield'

# Fetch the page
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with the data attribute you're interested in. 
# Replace 'data-attribute-name' with the actual name of the data attribute.
# This is just a placeholder for whatever attributes you're trying to scrape.
elements = soup.find_all(attrs={'data-attribute-name': True})

# Create a list to hold your data
data = []

# Extract the data from each element
for element in elements:
    # Extract data here based on the structure of your elements and what data you need
    data.append({
        'Attribute1': element.get('data-attribute1'),  # Example attribute
        'Attribute2': element.text.strip(),  # Example text content
        # Add more attributes as needed
    })

# Convert the list to a DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to a text file
df.to_csv('/home/kaylene/Documents/GitHub/Practice-at-Uni/Script Practice/Webscraping python script/output.csv', sep='\t', index=False)

print('Data written to output')
