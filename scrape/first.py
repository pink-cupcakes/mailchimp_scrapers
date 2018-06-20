import requests, bs4

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#print(page)
#print(page.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
