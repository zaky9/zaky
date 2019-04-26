# Comparison
'''
a = 12
b = 13
c = '12'

print(a == c)
print(a <= b)
print(a <= int(c))
print(a >= b)
print(a != int(c))
'''


nilai = int(input(' Masukan nilai anda: '))


# >= 80 => lulus
#>= 60 tapi < 80 => remidial
#< 60 => ga lulus


if nilai >= 80:
    print('Nilai anda =', nilai, ' Anda lulus')
elif 80 > nilai >= 60:
    print('Nilai anda =', nilai, ' Anda remedial')
else:
   print('Nilai anda =', nilai, ' Anda ga lulus')


angka = input('Silahkan ketik angka')

if angka.isdigit():
    if int(angka) % 2 == 0:
        print('Angka', angka, 'Tergolong Genap')
    else:
        print('Angka', angka, ' Tergolong Ganjil')
else:
    print('Maaf input tidak valid')