import requests
from bs4 import BeautifulSoup

# fetch and parse the page
response = requests.get('https://kgalvan.dev')
soup = BeautifulSoup(response.text, 'html.parser') # converts html into searchable object, html.parser is the built-in parser
print(soup.prettify()) # formats the html nicely for easier reading

# find main content container
content_div = soup.find('div', class_='main-content')