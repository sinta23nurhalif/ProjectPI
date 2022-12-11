from Tampilan import Tampilan
import Bukti
import datetime

def inputdata(para):
    #ambulance_rate = ambulance_rate.rent_ambulance()
    print("Tanggal pemesanan (dd/mm/yyyy): ")
    day = int(input("Hari: "))
    month = int(input("Bulan: "))
    year = int(input("Tahun: "))
    booking_date = datetime.date(year, month, day)
    Tampilan.date = str(booking_date)

    # Dapatkan input lama sewa
    duration = int(input("Lama sewa: "))
    nama_penyewa = input("Nama penyewa: ")
    Tampilan.bayar = para*duration
    Tampilan.total = str("{:,}".format(Tampilan.bayar).replace(',','.'))
    def printdata():
        print('\t   =====        DATA PENYEWAAN      =====')
        return  nama_penyewa, booking_date, duration, Tampilan.bayar
    Bukti.Bukti(printdata(), 60, Tampilan.bayar, Tampilan.date)
    
