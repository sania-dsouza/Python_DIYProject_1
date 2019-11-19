# Get the headlines of the NY Times using requests and BS

import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
print(list(title for title in soup.find('h2').text))