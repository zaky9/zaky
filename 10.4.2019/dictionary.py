# { 'key' : "value"} = Dictionary

namaHari = {
    '1' : 'Senin',
    '2' : 'Selasa',
    '3' : 'Rabu',
    '4' : 'Khamis',
    'Friday' : 'Jumat',
    'Sunday' : 'Minggu'
}

print(type(namaHari))

print(namaHari['1'])
print(namaHari['Friday'])
print(namaHari.get('Friday'))
print(namaHari.get('Saturday', 'Maaf data tidak ada'))

namaHari['Saturday'] = '6'
print(namaHari)

print(namaHari.keys())          # Memanggil keys
print(list(namaHari.keys()))

print(namaHari.values())        # Memanggil values
print(list(namaHari.values()))

print(namaHari['Friday'])

x = ['Andi', 'Budi', 'Caca']
print(x.index('Budi'))

# Access key by value
print(
    list(namaHari.keys())[list(namaHari.values()).index('Rabu')]
)