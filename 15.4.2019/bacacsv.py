
# file = open('karyawan.csv','r')
# print(file.read())

import csv
'''
with open('karyawan.csv','r') as fileku:
    baca = csv.reader(fileku)# untuk membaca csv file
    # print(baca)
    for i in baca:
        print(i)
'''

'''
# DictReader
with open('karyawan.csv','r') as fileku:
    baca = csv.DictReader(fileku)
    for i in baca:
        print(dict(i))
'''

# Append
myData = []
with open('karyawan.csv','r') as fileku:
    baca = csv.DictReader(fileku)
    for i in baca:
        # print(dict(i))
        myData.append(dict(i))

print(myData)