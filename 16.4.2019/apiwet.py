# 'https://api.openweathermap.org/data/2.5/weather?q='+ namakota +'&APPID=

import requests
import json

url = 'https://api.openweathermap.org/data/2.5/weather?q='
namaKota = input('Ketik nama kota: ')
appID = '9d880f8a846fa442e6fa9ef159258460'

dataCuaca = requests.get(url+namaKota+'&APPID='+appID)

cuaca = dataCuaca.json()['weather'][0]['main']
suhu = dataCuaca.json()['main']['temp']

lembab = dataCuaca.json()['main']['humidity']


print('Cuaca = ', cuaca)
print('Suhu = ', round(suhu-273,2),'*C')
print('Kelembaban = ', lembab, '%')

# print(dataCuaca.json())
