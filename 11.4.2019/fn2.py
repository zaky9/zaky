import math

def luasLingkaran(r):
    luas = round(math.pi * r * r,1)
    print('luas lingkaran dg r =', r, 'adalah', luas)

luasLingkaran(7)
luasLingkaran(14)


def luasTrapesium(a, b, t):
    luas = (a + b) * (t/2)
    print('Luas trapesium a= ',a, 'b= ',b, 't=', t , 'adalah ', luas)

luasTrapesium(3,6,4)

'''
def halo():
    nama = input(' Ketik nama anda ')
    print('Halo ', nama)

print(halo())
'''

# return function   

def aloha():
    print('Halo andi')
def hai():
    return 'Halo Andi'      # sama saja seperti function biasa x = 'halo andi'

x = ' halo Andi'

print(x)
print(hai())

