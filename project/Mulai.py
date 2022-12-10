from Tampilan import Tampilan
import AmbulanceTersedia
import os

def Mulai():
  os.system('clear')
  Tampilan.Awal()
  n = 1
  jmlh = 0
  pilihan = int(input("Masukkan Pilihan Anda : "))
  if (pilihan == 1):
      reg = input("Masukkan Kabupaten/Kota : ").upper()
      print("\nRumah Sakit yang terdapat di daerah " + reg + " : ")
      for region in Tampilan.ambl:
          if (reg in region['region'].upper()):
              jmlh += 1
              print('%d.' %n, "Rumah Sakit : ", region['name'])
              print("   Alamat      : ", region['address'])
              print("   No. Telp    : ", region['phone'])
              n = n + 1
              print()
      if (jmlh == 0):
        print("Tidak ada dalam database\n")
        input("Press ENTER to continue\n")
        Mulai()
      rs = int(input("Masukkan pilihan Rumah Sakit : "))
      if (rs < n):
        AmbulanceTersedia.AmbulanceTersedia()
      else :
        print("Pilihan Rumah Sakit Tidak Tersedia")
        input("Press ENTER to continue\n")
        Mulai()
  elif (pilihan == 2):
    prov = input("Masukkan Kabupaten/Kota : ").upper()
    print("\nRumah Sakit yang terdapat di daerah " + prov + " : ")
    for province in Tampilan.ambl:
        if (prov == province['province'].upper()):
          jmlh += 1
          print('%d.' %n, "Rumah Sakit : ", province['name'])
          print("   Alamat      : ", province['address'])
          print("   No. Telp    : ", province['phone'])
          n = n + 1
          print()
    if (jmlh == 0):
        print("Tidak ada dalam database\n")
        input("Press ENTER to continue\n")
        Mulai()
    rs = int(input("Masukkan pilihan Rumah Sakit : "))
    if (rs < n):
      AmbulanceTersedia.AmbulanceTersedia()
    else :
      print("Pilihan Rumah Sakit Tidak Tersedia")
      input("Press ENTER to continue\n")
      Mulai()
  else:
    print("Pilihan invalid masukkan pilihan hanya 1 / 2!")
    input("Press ENTER to continue\n")
    Mulai()