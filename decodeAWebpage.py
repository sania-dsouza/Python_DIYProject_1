# Get the headlines of the NY Times using requests and BS

import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
soup1 = soup.find_all('div', class_="css-1ez5fsm esl82me1")
resList = [i.get_text() for i in soup1]

if __name__ == '__main__':
    print(resList)

