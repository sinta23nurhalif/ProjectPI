from Tampilan import Tampilan
import Bill
import inputdata
import os
import Mulai
import AmbulanceTersedia


def Bukti(c,w,a, date):
#w fungsinya untuk parameter jumlah karakter yang ingin ditampilkan
  print('┏' + ('━' * w)                       + '┓')
  print('┃' + ' {} '.format(c).center(w, '░') + '┃')
  print('┃' + ' {} '.format("pastikan data anda benar!").center(w, '░') + '┃')
  print('┡' + ('━' * w)                       + '┩')
  print("Apakah data anda sudah benar? (Y/T)")
  pilihan = input("Masukkan Input : ")
  if (pilihan == 'Y' or pilihan == 'y'):
    Bill.Bill(Tampilan.mobil, Tampilan.total, Tampilan.date)
    os.system('clear')
    print("Transaksi Selesai")
    print("\nIngin kembali ke menu? (Y/T)")
    ingput = input("Masukkan input : ").upper()
    if (ingput == 'Y'):
      Mulai.Mulai()
    elif (ingput == 'T'):
      print("\nTerima Kasih!")
      exit()
  elif (pilihan == 'T' or pilihan == 't'):
    AmbulanceTersedia.AmbulanceTersedia()
  else:
    print("Masukkan inputan yang valid!")
    input()
    Mulai.Mulai()
    
    
