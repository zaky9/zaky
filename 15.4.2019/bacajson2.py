import json

with open('datajson.json') as dataku:
    data = json.load(dataku)        #.load = buka file not in string

print(data)
print(type(data))
print(data[0]['nama'])

# bikin fil