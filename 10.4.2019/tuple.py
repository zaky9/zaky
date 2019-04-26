# tuple : element tidak bisa di ganti (immutable)


angkaList = [1, 2, 3, 4, 5, 6]  # list = mutable
angkaTuple = (1, 2, 3, 4, 5, 6) # Tuple = immutable

print(angkaList[0])
print(angkaTuple[0])
print(angkaTuple[-1])

angkaList[0] = 1234
print(angkaList)

#angkaTuple[0] = 1234        error
#print(angkaTuple)

angkaTuple = (
    ['a', 'b', (3, 9)],
    ['c', 'd']
)

angkaTuple[0][2] = 'Andi'
print(angkaTuple)
