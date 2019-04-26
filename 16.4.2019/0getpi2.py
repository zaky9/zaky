import requests
import json
namaKlub = input('Ketik nama klub: ')
url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='+namaKlub

players = requests.get(url)
# print(type(players.json()))
# print(players.json(['player']))
for player in players.json()['player']:
    print(player['strPlayer'],'(', player['strNationality'],')')