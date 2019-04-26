# if statement
    #if condition:
        #    program
'''
sudahKerja = True

if sudahKerja == True:  # == use for comparison
    print('Traktir dong!')
else:
    print('Sukses cari kerja ya')

job = 'PNS'
if job == 'PNS': # first statement is true
    print('')
elif job == 'Swasta':
    print('Anda swasta')
else:
    print('Anda ngnggur')

'''

bekerja = False
jomblo = False

if bekerja and jomblo:
    print('Anda sudah kerja, kok jomblo?')
elif bekerja and not(jomblo):
    print('Selamat ')
elif bekerja == False and jomblo == True:
    print('Anda belum kerja, ko sudah taken?')
else:
    print('cari kerja dulu')
