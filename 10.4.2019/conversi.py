# conversi mata uang

mataUang= int(input('Tekan (1) untuk conversi USD ke IDR atau Tekan (2) untuk conversi IDR ke USD : '))

pilihan= {
    '1' : 'USD to IDR',
    '2' : 'IDR to USD'
}
if mataUang == 1:
    usd = int(input('Nilai USD: '))
    x = usd * 1416400
    print(usd, 'USD = ', x, 'IDR')

elif mataUang == 2:
    idr = int(input('Nilai IDR: '))
    y = idr * 0.000071
    print(idr, 'IDDR = ', y, 'USD')
else:
    print('Coba pilih lagi, tekan: ')
    print(pilihan)




# idr =int(input())
# usd =int(input)
