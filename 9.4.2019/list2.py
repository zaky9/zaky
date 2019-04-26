students = [
    'Andi',
    'Budi',
    'Caca',
    'Deni',
    'Budi'
]
newStudents = ['Euis', 'Fafa']
additionalStudents = 'Gilang'

print(students.index('Budi'))
print(students.count('Budi'))

students.extend(newStudents)    #Mengambungkan 2 list, berlaku buat list saja, masukan ke index terakhir
print(students)

students.append(additionalStudents) # untuk memasukan variable ke list, masukan ke index terakhir
print(students)
students.append(newStudents)
print(students)
print(students[-1][0])

students.insert(1, 'Zaza')      # Memasukan zaza ke index no 1
print(students)

students.remove('Budi')
print(students)

#students.pop()              # Menghapus element terakhir
#students.pop(2)             # Menghapus element index ke-x
#students.clear()           # Delete All

students.sort()             # sort by alphabetic
students.reverse()          # reverse by index
print(students)

