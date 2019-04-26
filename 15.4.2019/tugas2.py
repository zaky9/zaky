# cssv to json
import csv

l = []
with open('karyawan.csv','r') as karyawan:
    baca = csv.reader(karyawan)# untuk membaca csv file
    # print(baca)


    
    for i in baca:
        l.append(i)

h = []
for j in range(len(l)-1):
    dic = {}
    for k in range(len(l[0])):
        dic[l[0][k]] = l[j+1][k]
    h.append(dic)
print(h)

import json

js = json.dumps(h)
jsonku = open('dicToJson.json','w')
jsonku.write(js)