# Date Time
import datetime

x = datetime.datetime.now()

print(x)
print(x.year)           # Tahun
print(x.strftime('%m')) # Bulan index
print(x.strftime('%B')) # Nama Bulan
print(x.strftime('%A')) # Hari eng
print(x.strftime('%d')) # Tanggal
print(x.strftime('%H')) # Jam 24h
print(x.strftime('%I')) # Jam 12h
print(x.strftime('%M')) # Menit
print(x.strftime('%S')) # detik
print(x.strftime('%c')) # hr bln tnggl waktu thun
print(x.strftime('%x')) # 
print(x.strftime('%X')) # 


# tanggal ='12/4/2019'
# ubahStrkeDate = datetime.datetime.strptime

# from datetime import datetime
# x = '12/4/2019'
# y = '12 Apr 2019'
# z = '12-04-19 21.45'
# a = 'Firday, 12 April 2019'
# b = "Jum'at, 12 April 2019"
# ubahStrkeDate = datetime.strptime(x, '%d/%m/%Y')
# ubahStrkeDate = datetime.strptime(y, '%d %b %Y')
# ubahStrkeDate = datetime.strptime(z, '%d-%m-%y %H.%M')
# ubahStrkeDate = datetime.strptime(a, '%A, %d %B %Y')
# ubahStrkeDate = datetime.strptime(a, '%A, %d %B %Y')
# ubahStrkeDate = datetime.strptime(b, '%A, %d %B %Y')

# print(ubahStrkeDate)
# print(type(ubahStrkeDate))
# print(ubahStrkeDate.strftime('%A'))

print(x.strftime('Sekarang hari %A jam %H tgl %d-%B-%Y'))

namaHari = {
    'Monday' : 'Senin',
    'Tuesday' : 'Selasa',
    'Wednesday' : 'Rabu',
    'Thursday' : 'Khamis',
    'Friday' : 'Jumat',
    'Saturday' : 'Sabtu',
    'Sunday' : 'Minggu'
}

# namaBulan = {
#     'January' = 'Januari',
#     'February' = 'Febuari'
# }

hariIni = namaHari[x.strftime('%A')]
print(hariIni)