# Set {a, b, c} tidak bisa mengakses data element, no indexing

data = {1, 2, 3}
print(data)

# print(data[0]) error
'''
dataL = [1,2,3]
dataT = (1,2,3)
dataS = {1,2,3}

print(2 in dataL)
print(2 in dataT)
print(2 in dataS)

print(dataT[0:2:1])
print(dataT + dataT)
print(dataT * 3)

#dataT += dataT      # dataT = dataT + dataT
#print(dataT)

#dataT *= 3          # dataT = dataT * 3
#print(dataT)
'''

dataS = {'Andi', 'Budi', 'Caca'}

for element in dataS:
    print(element)

dataS.add('Deni')  # no indexing thus it randomize the element, no sorting
print(dataS)

dataS.add('Deni') # Use add when adding single element
print (dataS)
dataS.update(['Euis', 'Fafa']) # use update when adding multiple element
print (dataS)
dataS.update({'Gigi', 'Didi'})
print (dataS)

dataS.remove('Fafa') # when the element is not on the list there is an error
print(dataS)
dataS.discard('Deni') # viseverse 
print(dataS)

del dataS  # DataS set is deleted

