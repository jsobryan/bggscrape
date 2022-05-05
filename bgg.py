from bs4 import BeautifulSoup
import requests
import json

bgg_info = []
base_url = "https://authority.pub/negative-adjectives/"

response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")
games = soup.find_all('p.strong')
for game in games:
    names = game.find('a')
    bgg_info.append(names.get_text())

for i, item in enumerate(bgg_info,1):
    print(i, '. ' + item, sep='',end='\n')

