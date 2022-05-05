from bs4 import BeautifulSoup
import requests
import json

bgg_info = []
base_url = "https://boardgamegeek.com/browse/boardgame"

response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")
games = soup.find_all('td', {'class': 'collection_objectname'} )
for game in games:
    names = game.find('a')
    bgg_info.append(names.get_text())

for i, item in enumerate(bgg_info,1):
    print(i, '. ' + item, sep='',end='\n')

