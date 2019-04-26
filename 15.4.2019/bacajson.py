import json

# convert dict => json
x = {
    'nama' : 'Andi',
    'Usia' : 23
}
'''
y = json.dumps(x)       #.dumps untuk menulis di json
print(x)
print(y)        # json menggunakan " " dan tidak pakai ',' buat terakhir

x2 = ['Andi', 'Budi']

y = json.dumps(x)       # .dumps takes an object and produces a string
y2 = json.dumps(x2)

print(x2)
print(y2)

z1 = 'Aku string biasa'
z2 = json.dumps(z1)

print(z2)
'''

x = '{"nama": "Andi"}'
x2 = '["Andi", "Budi", "Caca"]'
y = json.loads(x)       # take a file-like object, read the data from that object, and use that string to create an object
y2 = json.loads(x2)

print(x)
print(y)
print(y['nama'])

print(x2)
print(y2)
print(y2[1])



