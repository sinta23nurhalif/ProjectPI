from Tampilan import Tampilan
import RentAmbulance

def AmbulanceTersedia():
  # Tampilkan jenis mobil ambulans yang tersedia beserta tarif sewa per hari-nya
  print("\nPenyewaan Ambulans")
  print("Jenis Mobil Ambulans\t\t\tTarif Sewa/Hari")
  print('==========================================================')
  for i in range(1):
    print("1. " + Tampilan.appearance[0])
    print("2. " + Tampilan.appearance[1])
  RentAmbulance.RentAmbulance()