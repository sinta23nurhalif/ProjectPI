import Bill
import inputdata
from Tampilan import Tampilan

def Bukti(c,w,a, date):
#w fungsinya untuk parameter jumlah karakter yang ingin ditampilkan
  print('┏' + ('━' * w)                       + '┓')
  print('┃' + ' {} '.format(c).center(w, '░') + '┃')
  print('┃' + ' {} '.format("pastikan data anda benar!").center(w, '░') + '┃')
  print('┡' + ('━' * w)                       + '┩')
  print("Apakah data anda sudah benar? (Y/T)")
  pilihan = input("Masukkan Input : ")
  if (pilihan == 'Y' or pilihan == 'y'):
    Bill.Bill(Tampilan.x, Tampilan.a, Tampilan.date)