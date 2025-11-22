# scraper.py

import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://quotes.toscrape.com"

# Send a GET request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Extract quotes
quotes = soup.find_all('span', class_='text')

# Print quotes
for quote in quotes:
    print(quote.text)
