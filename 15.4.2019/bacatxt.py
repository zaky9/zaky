# 'r' => read .txt files 
# open() => local files
# 'w' => write
# 'a' => append file


# file = open('note.txt','r')

# r = read

# print(file.readable())
# print(file.read())

# if file.readable():
#     # print(file.read())
#     mylist = file.readlines()
#     print(mylist[0])
#     for x in mylist:
#         print(x)
# else:
#     print(' Maaf file tidak ke baca')


# w = write

# file = open('note.txt','w')
# file.write('Selamat pagi')
# file = open('note2.docx','w')
# file.write('Selamat pagi')

# file = open('13.py','w')
# file.write('print(\'halo!-1\')\n')
# file = open('13.py','w')
# file.write('print(\'halo!-2\')')


'''
# a = append file

file = open('13.py','w')
file.write('print(\'halo!-1\')\n')
file = open('13.py','a')
file.write('print(\'halo!-2\')')
'''

# list = ['Andi', 'Budi', 'Cici']

# file = open('note.txt','w')
# file.write(str(list))

list = ['Andi', 'Budi', 'Cici']
file = open('12.txt','a')

for x in list:
    file.write('\n'+ x)