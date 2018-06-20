from lxml import html
import requests
import json

page = requests.get('https://www.ideo.com/news?page=2')
tree = html.fromstring(page.content)

title = tree.xpath('//*[@id="ScrollAnchor"]/div/div[1]/div[1]/div[1]/h4/a/text()')
date = tree.xpath('//*[@id="ScrollAnchor"]/div/div[1]/div[1]/div[1]/p/text()')

store = {"title":title,"date":date}

print(title)
print(date)

with open('data.txt', 'w') as outfile:
    json.dump(store, outfile)
