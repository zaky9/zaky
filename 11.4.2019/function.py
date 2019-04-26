# Function

# f(x) = x + 1
# untuk x = 1 maka f(x) = f(1) = 1 + 1 = 2

'''
def namaFunsi():
    program

namaFunsi()
'''

def tes():
    print('Halo ini function!')

tes()           #calling function

def tes2(x):
        print('Halo', x)

tes2('Andi')
tes2('Budi')
tes2(input('Ketik nama: '))

def tes3(x,y):
    z= x**y
    print('Hasil Kali', x , "dan", y, "=", x*y)
    print('Hasil', x, ' pangkat ', y, "= ",z)

tes3(input('no x: '),input('no y: '))
