from Tampilan import Tampilan
import json
import Bukti

def Bill(mobil, bayar, date):
  #menyetak struk tagihan penyewaan
  bill = open("tagihan.txt", "w")
  bill.write(Tampilan.date)
  bill.write('\n')
  bill.write(Tampilan.appearance[mobil-1])
  bill.write('\n')
  bill.write("Total \t\t\t\t\t\tRp. ")
  bill.write(Tampilan.total)
  bill.close()  
