# Basic calculator
no1 = int(input('Masukan angka pertama: '))
operator = input(' Masukan symbol operator (+,-,/,*): ')
no2 = int(input('Masukan angka kedua: '))

if operator == '+':
    print(no1,"+",no2,"=",no1 + no2)
elif operator == '-':
    print(no1,"-",no2,"=",no1 - no2)
elif operator == '*':
    print(no1,"*",no2,"=",no1 * no2)
elif operator == '/':
    print(no1,"/",no2,"=",no1 / no2)
else:
    print('invalid operator, coba ulang lagi')
