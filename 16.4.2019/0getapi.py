# get API https://jsonplaceholder.typicode.com/users
# requests = 3rd party libary => pip

#instal package vai pip
# 1. pip instal namaPackage => pip install requests
# 2. py -m pip install namaPackage


import requests
import json
url = 'https://jsonplaceholder.typicode.com/users'

data = requests.get(url)
print(data.json())
print(type(data.json()))

hasilJson = json.dumps(data.json())
fileJson = open('users.json','w')
fileJson.write(hasilJson)

