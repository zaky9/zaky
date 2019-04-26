angka = [14, 2, 34, 12, 67, 2]
print(angka)

x = angka[0:3]
x.sort()
print(x)

JumlahKarakterPertamaYangAkanDisortir = 5
x = angka[0:JumlahKarakterPertamaYangAkanDisortir]
x.sort()
print(x)

angka[0:len(x)]= x
print(angka)
