# Looping
# for, while, while loop

# while condition:
#     program

'''
angka = 1
while angka <= 10:
    print('haha ke', angka)
    angka += 1
'''

'''
#looping untuk mengakses list
angka = [1,2,3,4,5,6,7]
angka2 = []
i = 0 
while 1<= len(angka)-1:
    print(angka[i] *2)
    i += 1
'''

'''
angka = [1,2,3,4,5,6,7]
angka2 = []
angkaCopy = []
i = 0 
while i <= len(angka)-1:
    angka2.append(angka[i]*2)
    angkaCopy.append(angka[i])
    i += 1
print(angka)
print(angka2)
print(angkaCopy)
'''

'''
i = 0 
while i < 6:
    print(i)
    if i == 4:
        break # to stop the function 
    i += 1
'''


i = 0 
while i < 6:
    i += 1
    if i == 4:
        continue 
    print(i)