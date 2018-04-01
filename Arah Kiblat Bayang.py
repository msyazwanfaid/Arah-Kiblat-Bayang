import math
import ephem

#Penentuan Lintasan Arah Kiblat Harian
latitudkaabah = 21+25/60+21/3600
longitudkaabah = 39+49/60+34.32/3600

print("Masukkan Nama Tempat")
namatempat = str(input())
print("Masukkan Koordinate Tempat yang ingin Dikira Kiblatnya")

lokasi = ephem.Observer()
print("Masukkan Latitud (Utara = Positif, Selatan=Negatif)")
lokasi.lat = input()

print("Masukkan Longitud(Timur = Positif, Barat=Negatif)")
lokasi.long = input()

print("Masukkan Jam")
t = float(input())

print("Masukkan Hari")
d = int(input())

print("Masukkan Bulan")
m = int(input())

print("Masukkan Tahun")
y = int(input ())

print("Masukkan Time Zone")
tz = int(input())
tz1 = t - tz


#Pengiraan Time Zone#
if tz1 < 0:
    dtz = d - 1
    ttz = (24 + t) - tz

elif tz1 <= 24:
    ttz = t-tz
    dtz=d
else :
    dtz = d+1
    ttz = ((t-tz)-24)
#print('')
#print('Waktu UTC mengikut timezone %i adalah %i dan hari %i'% (tz,ttz,dtz))

#Pengiraan Tahun Lompat
x = y%4
if x == 0:
    k = 1
    dt = 366
else:
    k = 2
    dt = 365

#Pengiraan Hari dalam Setahun dan Nisbah Hari dalam setahun#
n =  round(((275*m)/9)-0.5) - k * round(((m+9)/12)-0.5) + dtz -30 - 1 + ttz/24
y1 = str(y+ (n/dt))
d = ephem.Date(y1)
lokasi.date=d
mata = ephem.Sun()

#Pengiraan Waktu Istiwa
n= lokasi.next_transit(mata)
o = float(n)
waktuistiwa =(o-int(o)-0.5)*24+tz
waktuistiwadegrees = int(waktuistiwa)
temp = 60 * (waktuistiwa - waktuistiwadegrees)
waktuistiwaminute = int(temp)
waktuistiwasaat = 60 * (temp - waktuistiwaminute)


#formula arah kiblat
print('')
longitudtempatan = math.degrees(lokasi.long)
latitudtempatatan = math.degrees(lokasi.lat)
a = math.sin(math.radians(longitudtempatan-longitudkaabah))
b = math.cos(math.radians(latitudtempatatan))*math.tan(math.radians(latitudkaabah))
c = math.sin(math.radians(latitudtempatatan))*math.cos(math.radians(longitudtempatan-longitudkaabah))
d = a/(b-c)
arahkiblat1 = math.degrees(math.pi/2-math.atan(d))
arahkiblat = arahkiblat1+270
#print('Arah Kiblat bagi lokasi %s adalah %0.2f'% (namatempat,arahkiblat))

#azimuthmatahari
mata = ephem.Sun()
mata.compute (lokasi)
mataaz = float(math.degrees(mata.az))


#arahkiblatdaribayangmatahari
bezaazimuthkiblatbayangmatahari = arahkiblat-mataaz
lokasi.date = lokasi.date + ephem.hour * tz
print('Pada  %s beza azimuth antara bayang matahari dengan arah kiblat adalah %0.2f'%(lokasi.date,bezaazimuthkiblatbayangmatahari))