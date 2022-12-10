import requests
import json
import datetime

class Tampilan:
  response = requests.get('https://dekontaminasi.com/api/id/covid19/hospitals')
  ambl = response.json()
  date = 0
  ambulance_rate = 0
  x = 0
  bayar = 0 
  a = ''
  appearance = ["Mobil Ambulans Umum\t\t\tRp. 500.000", "Mobil Ambulans Gabungan\t\tRp. 1.000.000\n"]  
  def Awal():
    print("Penyewaan Ambulans")
    print("Mencari Rumah Sakit Terdekat Berdasarkan")
    print("1. Kabupaten/Kota")
    print('2. Province')
    print()