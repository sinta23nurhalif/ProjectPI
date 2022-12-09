import datetime
ambulance_rate = 0

def show_available_ambulances():
  # Tampilkan jenis mobil ambulans yang tersedia beserta tarif sewa per hari-nya
  print("Jenis Mobil Ambulans\t\t\tTarif Sewa/Hari")
  print('==========================================================')
  print("1. Mobil Ambulans Umum\t\t\tRp. 500.000")
  print("2. Mobil Ambulans Gabungan\t\tRp. 1.000.000\n")

def rent_ambulance():
  while True :# Dapatkan input jenis mobil ambulans yang dipilih 
    while True :
        try:
            ambulance_type = int(input("Masukkan jenis mobil ambulans (1/2): "))
        except (SyntaxError,NameError, ValueError):
            print("pilihan invalid masukkan pilihan hanya 1 / 2!")
            continue
        break       
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

  # Dapatkan input tanggal pemesanan
    
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
    
    tampilan(printdata(), 60)
    

def tampilan(c,w):
#w fungsinya untuk parameter jumlah karakter yang ingin ditampilkan
    print('┏' + ('━' * w)                       + '┓')
    print('┃' + ' {} '.format(c).center(w, '░') + '┃')
    print('┃' + ' {} '.format(" \npastikan data anda benar!").center(w, '░') + '┃')
    print('┡' + ('━' * w)                       + '┩')

show_available_ambulances()
rent_ambulance()