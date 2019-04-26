# conversion

kurs = {
    '1' : 0.00071,
    '2' : 14157
}
def konversi():
    print('Selamat datang di web konversiDuit.com')
    print('Silahkan pilihh metode knoversi: ')
    print('1. IDR ke USD')
    print('2. USD ke IDR')
    methode = input(' Ketik pilihan Anda: ')
    if methode == '1':
        nominal = input('Ketik nominal Rupiah : Rp ')
        if nominal.replace('.', '').replace(',', '').isdigit():
            hasil = float(nominal.replace(',', '.')) * kurs[methode]
            print('Rp: ',nominal, ' = ', '$: ', hasil)
        else:
            print('Mohon inputkan hanya angka')
    elif methode == '2':
        nominal = input(' Ketik nominal Dollar : $')
        if nominal.replace('.', '').replace(',', '').isdigit():
            hasil = float(nominal.replace(',', '.')) * kurs[methode]
            print('$: ',nominal, ' = ', 'Rp: ', hasil)
        else:
            print('Mohon inputkan hanya angka')
    else:
        print(' pilih antara 1 atau 2')

# konversi()


