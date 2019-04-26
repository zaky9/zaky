# nested loop

# for i in range(5):
#     for j in range(5):
#         print(i, 'dan' j)

listku = [
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
]

# for baris in listku:
#     for elemen in baris:
#         print(elemen)

data = [
    [
        ['Andi', 'Budi', 'Caca'],
        ['Deni', 'Euis', 'Fafa'],
        ['Gigi', 'Hani', 'Inne']
    ],
    [
        ['Judy', 'Kiki', 'Luli'],
        ['Mimi', 'Nina', 'Opik'],
        ['Peni', 'Qiqi', 'Rogi']
    ]
]

for i in data:
    for j in i:
        for k in j:
            print(k)