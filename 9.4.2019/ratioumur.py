total= int(input('umur total dua orang adalah: '))
ratio= float(input('ratio umur: '))

org1 = int(total / (1+ ratio))
org2 = int(total - org1)

print('Usia org1 =', org1, 'th & usia org2 = ', org2, 'th')