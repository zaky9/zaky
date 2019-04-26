# list

matkul = ['Kalkulus','Astoronomi', 'Elektronika']
genap = [0,2,4,6,8,10]
ganjil = [1.0, 3.0, 5.0]
boolean = [True, False]
campur = ['Andi', 21, 'Budi', 22]

x = 0
y = 1
z = 2
s = [x,y,z,3,4,5,6]         # element mulai di hitung dari 0

print(s)
print(len(s))

print(s[0])             # Mulai dari element awal
print(s[1])
print(s[2])
print(s[len(s)-1])      # mulai dari element terakhir
print(s[-2])            # mulai dari element terakhir

print(s[0:3])           #start : end 
print(s[1:7])
print(s[0:7:2])         #start : end : step
print(s[0::2])          #start : (all element) : step     

