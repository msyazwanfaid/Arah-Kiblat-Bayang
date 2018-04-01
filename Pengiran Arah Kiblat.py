import math
import ephem

#Penentuan
latitudkaabah = 21+25/60+21/3600
longitudkaabah = 39+49/60+34.32/3600

print("Masukkan Nama Tempat")
namatempat = str(input())
print("Masukkan Koordinate Tempat yang ingin Dikira Kiblatnya")
print("Masukkan Latitud (Utara = Positif, Selatan=Negatif)")
latitudtempatan = float(input())

print("Masukkan Longitud(Timur = Positif, Barat=Negatif)")
longitudtempatan = float(input())

print(latitudkaabah,longitudkaabah,latitudtempatan,longitudtempatan)

a = math.sin(math.radians(longitudtempatan-longitudkaabah))
b = math.cos(math.radians(latitudtempatan))*math.tan(math.radians(latitudkaabah))
c = math.sin(math.radians(latitudtempatan))*math.cos(math.radians(longitudtempatan-longitudkaabah))
d = a/(b-c)
arahkiblat1 = math.degrees(math.pi/2-math.atan(d))
arahkiblat = arahkiblat1+270
print('Arah Kiblat bagi lokasi %s adalah %0.2f'% (namatempat,arahkiblat))

