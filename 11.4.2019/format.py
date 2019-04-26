# format function
x= 200
print(x)
print('{:,}'.format(x))
print('{:,}'.format(x).replace(',','.'))

print('Halo {}, umurmu {}'.format('Andi', 27))
print('Halo {1}, umurmu {0}'.format('Andi', 27))
print('Asalmu dari {kota}'.format(kota = 'Depok'))
print('Suhu udara = {0:f}'.format(25))  # string formating methode {string:format} f= float, s= string,c,d,