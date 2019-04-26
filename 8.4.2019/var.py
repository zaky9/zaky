#variable

nama = "Andi Susilo Siregar Hadi"
usia = 23
berat = 76.8
jomblo = True

print("hai saya "+ nama)
print("hai saya", nama)
print("hai saya", nama, "umurku", usia, "th")
print("hai saya "+ nama + " umurku " + str(usia) + " th")  # usia harus di tukar ke string value

#jum'at
print("jum'at") # atau print('jum\'at)
print('jum\'at')
print('hello\tgaes!') #tab ke samping
print('hello\ngaes!') #tab ke bawah

print(nama.lower()) # huruf kecil semua
print(nama.upper()) # huruf besar semua
print(nama.islower()) # menanyakan huruf kecil
print(nama.isupper()) # menanyakan huruf besar

print(nama.lower().islower()) # membuat huruf kecil, abis itu menanyakan huruf kecil
print(nama.upper().isupper()) # viseversa
print(len(nama)) # menghitung berapa sepasi (menhitung huruf dan spasi). menggunakan integer
print(nama[0]) # mennyakan no karakter itu apa, 0 artinya huruf pertama
print(nama[len(nama) - 1])

print(nama.index('S'))
print(nama.index('Siregar'))
print(nama.replace('Hadi', "Hadiwijaya"))

print(nama.split('i')) #memotong huruf i
print(nama.split(' ')[1]) # memanggil menghitung no spasi

# penghitung jumlah huruf di nama seseorang (spasi tdk di hitung)
# penghitung jumlah huruf tertentu dlm suatu kata

'''
kata = 'andi'
cari = 'a'
cari ?
'''

