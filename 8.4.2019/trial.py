# penghitung jumlah huruf di nama seseorang (spasi tdk di hitung)

nama = "anti tidak masuk sekolah hari ini karena tidak sekolah"
x = len(nama)
y = len(nama.split(' '))-1

print( nama, "ada ", x-y, " huruf")

# penghitung jumlah huruf tertentu dlm suatu kata

huruf = 'sekolah'
huruf.lower()
z = len(nama.lower().split(huruf))-1
print("jumlah ",huruf,"dalam", nama ,"adalah: ", z)
