# penghitung jumlah huruf di nama seseorang (spasi tdk di hitung)

kalimat = "anti tidak masuk sekolah hari ini karena tidak sekolah"
x = len(kalimat)
y = len(kalimat.split(' '))-1

# print( kalimat, "ada ", x-y, " huruf")

# penghitung jumlah huruf tertentu dlm suatu kata

kata = 'sekolah'
kata.lower()
z = len(kalimat.lower().split(kata))-1
print("di dalam kalimat: \n",kalimat)
print("ada: ",z, "kata", kata)
