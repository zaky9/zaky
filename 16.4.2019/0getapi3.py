import requests
import json
nama = input('Ketik nama pemain: ')
url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?p='+nama

players = requests.get(url)
# print(type(players.json()))
# print(players.json(['player']))
for player in players.json()['player']:
    print(player['strTeam'])