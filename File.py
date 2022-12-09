import requests
import json
import datetime

response = requests.get('https://dekontaminasi.com/api/id/covid19/hospitals')
ambl = response.json()
ambulance_rate = 0

def Tampilan():
  print("Penyewaan Ambulans")
  print("Mencari Rumah Sakit Terdekat Berdasarkan")
  print("1. Kabupaten/Kota")
  print('2. Province')
  print()
  
def Mulai():
  try:
    n = 1
    pilihan = int(input("Masukkan Pilihan Anda : "))
    if pilihan == 1:
        reg = input("Masukkan Kabupaten/Kota : ").upper()
        print("\nRumah Sakit yang terdapat di daerah " + reg + " : ")
        for region in ambl:
          try:
            if reg in region['region'].upper():
                print('%d.' %n, "Rumah Sakit : ", region['name'])
                print("   Alamat      : ", region['address'])
                print("   No. Telp    : ", region['phone'])
                n = n + 1
                print()
          except:
            Tampilan()
            Mulai()
        rs = int(input("Masukkan pilihan Rumah Sakit : "))
        if rs < 5:
          AmbulanceTersedia()
    elif pilihan == 2:
      prov = input("Masukkan Kabupaten/Kota : ").upper()
      print("\nRumah Sakit yang terdapat di daerah" + prov + " : ")
      for province in ambl:
        try:
          if prov == province['province'].upper():
            print('%d.' %n, "Rumah Sakit : ", province['name'])
            print("   Alamat      : ", province['address'])
            print("   No. Telp    : ", province['phone'])
            n = n + 1
            print()
        except:
          Tampilan()
          Mulai()
      rs = int(input("Masukkan pilihan Rumah Sakit : "))
      if rs < 5:
        AmbulanceTersedia()
  except:
    print("Pilihan invalid masukkan pilihan hanya 1 / 2!")
    Mulai()
  
def AmbulanceTersedia():
  # Tampilkan jenis mobil ambulans yang tersedia beserta tarif sewa per hari-nya
  appearance = ["1. Mobil Ambulans Umum\t\t\tRp. 500.000", 
  "2. Mobil Ambulans Gabungan\t\tRp. 1.000.000\n"]
  print("Jenis Mobil Ambulans\t\t\tTarif Sewa/Hari")
  print('==========================================================')
  for i in range(2):
    print(appearance[i])
  RentAmbulance()

def rent_ambulance():
  # Dapatkan input jenis mobil ambulans yang dipilih 
  try:
    ambulance_type = int(input("Masukkan jenis mobil ambulans (1/2): "))
    if ambulance_type == 1:
        ambulance_type = "Mobil Ambulans Umum"
        ambulance_rate = 500000
        inputdata(ambulance_rate)    
    elif ambulance_type == 2:
        ambulance_type = "Mobil Ambulans Gabungan"
        ambulance_rate = 1000000
        inputdata(ambulance_rate)
    else:
        print("Jenis mobil ambulans tidak valid")        
    return
  except (SyntaxError,NameError, ValueError):
    print("pilihan invalid masukkan pilihan hanya 1 / 2!")
    
def inputdata(self):
    #ambulance_rate = ambulance_rate.rent_ambulance()
    print("Tanggal pemesanan (dd/mm/yyyy): ")
    day = int(input("Hari: "))
    month = int(input("Bulan: "))
    year = int(input("Tahun: "))
    booking_date = datetime.date(year, month, day)

    # Dapatkan input lama sewa
    duration = int(input("Lama sewa: "))
    nama_penyewa = input("Nama penyewa: ")
    bayar = self*duration
    def printdata():
        # print('=====        DATA PENYEWAAN      =====')
        # print('Nama Penyewa : ', nama_penyewa, '\n', 'Tanggal sewa : ', booking_date, 'Lama sewa:  ', duration,'Harga yang harus dibayar', bayar )
        return  nama_penyewa, booking_date, duration, bayar
    Bukti(printdata(), 60)
    

def Bukti(c,w):
#w fungsinya untuk parameter jumlah karakter yang ingin ditampilkan
    print('┏' + ('━' * w)                       + '┓')
    print('┃' + ' {} '.format(c).center(w, '░') + '┃')
    print('┃' + ' {} '.format(" \npastikan data anda benar!").center(w, '░') + '┃')
    print('┡' + ('━' * w)                       + '┩')
    
Tampilan()
Mulai()
