# from abc import ABC, abstractmethod

# # 1. Interface
# class Transportasi(ABC):

#     @abstractmethod
#     def hitung_ongkir(self, jarak):
#         pass

#     @abstractmethod
#     def lacak_status(self):
#         pass


# # 2. Implementasi Class

# class SepedaMotor(Transportasi):
#     def hitung_ongkir(self, jarak):
#         return 5000 * jarak

#     def lacak_status(self):
#         return "Kurir sedang meluncur di kemacetan"


# class MobilBox(Transportasi):
#     def hitung_ongkir(self, jarak):
#         return (10000 * jarak) + 20000

#     def lacak_status(self):
#         return "Mobil dalam perjalanan via jalan tol"


# class Drone(Transportasi):
#     def hitung_ongkir(self, jarak):
#         return 15000 * jarak

#     def lacak_status(self):
#         return "Drone sedang terbang menuju koordinat"


# # 3. Fungsi Polimorfisme
# def proses_pengiriman(nomor, transport, jarak):
#     biaya = transport.hitung_ongkir(jarak)
#     status = transport.lacak_status()
    
#     # Ambil nama class
#     nama = transport.__class__.__name__
    
#     # Rapikan nama
#     if nama == "MobilBox":
#         nama = "Mobil Box"
#     elif nama == "SepedaMotor":
#         nama = "Sepeda Motor"
    
#     print(f"Pengiriman {nomor} ({nama}):")
#     print(f"Status     : {status}.")
#     print(f"Total Biaya: Rp{biaya}")
#     print()


# # 4. Main Program
# motor = SepedaMotor()
# mobil = MobilBox()
# drone = Drone()

# proses_pengiriman(1, motor, 10)
# proses_pengiriman(2, mobil, 10)
# proses_pengiriman(3, drone, 10)

# from abc import ABC, abstractmethod

# class Koleksi(ABC):
#     def __init__(self, judul, tahun_terbit, penerbit, kode):
#         self.judul = judul
#         self.tahun_terbit = tahun_terbit
#         self.penerbit = penerbit
#         self.kode = kode
#         # self.edisi = edisi

#     @abstractmethod
#     def tampilkan_info(self):
#         pass


# # class Buku
# class Buku(Koleksi):
#     def __init__(self, kode, judul, tahun_terbit, pengarang, penerbit):
#         super().__init__(judul, tahun_terbit, penerbit, kode)
#         self.pengarang = pengarang

#     def tampilkan_info(self):
#         print(
#             "DATA BUKU\n"
#             f"Masukkan Kode Buku    : {self.kode}\n"
#             f"Masukkan Judul Buku   : {self.judul}\n"
#             f"Masukkan Tahun Terbit : {self.tahun_terbit}\n"
#             f"Masukkan Pengarang    : {self.pengarang}\n"
#             f"Masukkan Penerbit     : {self.penerbit}\n"
#         )


# # class Majalah
# class Majalah(Koleksi):
#     def __init__(self, kode, judul, tahun_terbit, edisi, penerbit):
#         super().__init__(judul, tahun_terbit, penerbit, kode)
#         self.edisi = edisi

#     def tampilkan_info(self):   
#         print(
#             "DATA MAJALAH\n"
#             f"Masukkan Kode Koleksi    : {self.kode}\n"
#             f"Masukkan Judul           : {self.judul}\n"
#             f"Masukkan Tahun Terbit    : {self.tahun_terbit}\n"
#             f"Masukkan Penerbit        : {self.penerbit}\n"
#             f"Masukkan Edisi           : {self.edisi}\n"
#         )


# # class Jurnal
# class Jurnal(Koleksi):
#     def __init__(self, kode, judul, tahun_terbit, tanggal_terbit, penerbit, bidang_studi, impact_factor):
#         super().__init__(judul, tahun_terbit, penerbit, kode)
#         self.tanggal_terbit = tanggal_terbit
#         self.bidang_studi = bidang_studi
#         self.impact_factor = impact_factor

#     def tampilkan_info(self):
#         print(
#             "DATA JURNAL\n"
#             f"Masukkan Kode Koleksi    : {self.kode}\n"
#             f"Masukkan Judul           : {self.judul}\n"
#             f"Masukkan Tahun Terbit    : {self.tahun_terbit}\n"
#             f"Masukkan Penerbit        : {self.penerbit}\n"
#             f"Masukkan Tanggal Terbit  : {self.tanggal_terbit}\n"
#             f"Masukkan Bidang Studi    : {self.bidang_studi}\n"
#             f"Masukkan Impact Factor   : {self.impact_factor}\n"
#         )

# #Class DVD
# class DVD(Koleksi):
#     def __init__(self, kode, judul, tahun_terbit, sutradara, durasi, penerbit):
#         super().__init__(judul, tahun_terbit, penerbit, kode)
#         self.sutradara = sutradara
#         self.durasi = durasi

#     def tampilkan_info(self):
#         print(
#             "DATA DVD\n"
#             f"Kode        : {self.kode}\n"
#             f"Judul       : {self.judul}\n"
#             f"Tahun Terbit: {self.tahun_terbit}\n"
#             f"Sutradara   : {self.sutradara}\n"
#             f"Durasi      : {self.durasi} menit\n"
#             f"Penerbit    : {self.penerbit}\n"
#         )

# # Menu Koleksi
# daftar_koleksi = []

# def tambah_data():
#     print("Pilih Jenis Koleksi:")
#     print("1. Buku")
#     print("2. Majalah")
#     print("3. Jurnal")
#     print("4. DVD")
#     pilihan = input("Masukkan pilihan (1/2/3): ")
#     print( "input tidak ada")

#     if pilihan == '1':
#         kode = input("Masukkan Kode Buku: ")
#         judul = input("Masukkan Judul Buku: ")
#         tahun_terbit = input("Masukkan Tahun Terbit: ")
#         pengarang = input("Masukkan Pengarang: ")
#         penerbit = input("Masukkan Penerbit: ")
#         buku = Buku(kode, judul, tahun_terbit, pengarang, penerbit)
#         daftar_koleksi.append(buku)
#         print("Data buku berhasil ditambahkan.\n")

#     elif pilihan == '2':
#         kode = input("Masukkan Kode Majalah: ")
#         judul = input("Masukkan Judul Majalah: ")
#         tahun_terbit = input("Masukkan Tahun Terbit: ")
#         edisi = input("Masukkan Edisi: ")
#         penerbit = input("Masukkan Penerbit: ")
#         majalah = Majalah(kode, judul, tahun_terbit, edisi, penerbit)
#         daftar_koleksi.append(majalah)
#         print("Data majalah berhasil ditambahkan.\n")

#     elif pilihan == '3':
#         kode = input("Masukkan Kode Jurnal: ")
#         judul = input("Masukkan Judul Jurnal: ")
#         tahun_terbit = input("Masukkan Tahun Terbit: ")
#         tanggal_terbit = input("Masukkan Tanggal Terbit (DD/MM/YY): ")
#         penerbit = input("Masukkan Penerbit: ")
#         bidang_studi = input("Masukkan Bidang Studi: ")
#         impact_factor = input("Masukkan Impact Factor: ")
#         koran = Jurnal(kode, judul, tahun_terbit, tanggal_terbit, penerbit, bidang_studi, impact_factor)
#         daftar_koleksi.append(koran)
#         print("Data koran berhasil ditambahkan.\n")

#     elif pilihan == '4':
#         kode = input("Masukkan Kode DVD: ")
#         judul = input("Masukkan Judul DVD: ")
#         tahun_terbit = input("Masukkan Tahun Terbit: ")
#         sutradara = input("Masukkan Sutradara: ")
#         durasi = input("Masukkan Durasi (menit): ")
#         penerbit = input("Masukkan Penerbit: ")
#         dvd = DVD(kode, judul, tahun_terbit, sutradara, durasi, penerbit)
#         daftar_koleksi.append(dvd)
#         print("Data DVD berhasil ditambahkan.\n")
#     else:
#         print("Pilihan tidak valid. Silakan coba lagi.\n")

# #Menghapus Data
# def hapus_data():
#     print(
#         "----------------------------------------------\n"
#         "HAPUS DATA KOLEKSI\n"
#     )
#     kode = input("Masukkan Kode Koleksi: ")

#     global daftar_koleksi
#     for i, koleksi in enumerate(daftar_koleksi):
#         if koleksi.kode == kode:
#             del daftar_koleksi[i]
#             print("Data koleksi berhasil dihapus.\n")
#             return

#     print("Kode koleksi tidak ditemukan.\n")

# # Menampilkan Semua Koleksi
# def tampilkan_semua():
#     print(
#         "----------------------------------------------\n"
#         "DAFTAR KOLEKSI\n"
#     )
#     if not daftar_koleksi:
#         print("Tidak ada koleksi yang tersedia.\n")
#     else:
#         for i, item in enumerate(daftar_koleksi, start=1):
#             print(
#                 f"Koleksi {i}:\n"
#                 )
#             item.tampilkan_info()
#             print("\n")
    
#     print("----------------------------------------------\n")
#     input("Tekan Enter untuk kembali ke menu utama...")

# # Menu utama
# def menu_utama():
#     while True:
#         print("Menu Koleksi:")
#         print("1. Tambah Koleksi")
#         print("2. Hapus Koleksi")
#         print("3. Tampilkan Semua Koleksi")
#         print("4. Keluar")
#         pilihan = input("Masukkan pilihan: ")

#         if pilihan == '1':
#             tambah_data()
#         elif pilihan == '2':
#             hapus_data()
#         elif pilihan == '3':
#             tampilkan_semua()
#         elif pilihan == '4':
#             print("Terima kasih telah menggunakan program ini.")
#             break
#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.\n")

# if __name__ == "__main__":
#     menu_utama()

from datetime import date

class BankAccount:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.__saldo = saldo_awal
        self.__log = []  # Log transaksi
        self.__log_header = (
            "-" * 80 + "\n" 
            + f"| {'Tanggal':<15} | {'Keterangan':<20} | {'Jumlah':>20} | {'Saldo':>20} |\n"
            + "-" * 80 + "\n"
        )
        self.__log.append(
            f"| {str(date.today()):<15} | {'Saldo Awal':<20} | {self.format_rupiah(saldo_awal):>20} | {self.format_rupiah(self.__saldo):>20} |"
        )

    #mengatur digit sesuai rupiah
    def format_rupiah(self, jumlah):
        return f"Rp{jumlah:,.2f}".replace(".", ",").replace(".", ",", 1)
    
    #menampilkan semua nasabah
    def tampilkan_nasabah(self):
        print(f"{'No.':<5} {'Nama':<20} {'Saldo':>50}")
        print("-" * 75)
        for i, akun in enumerate(daftar_akun, start=1):
            print(f"| {i:<5} | {akun.pemilik:<30} | {self.format_rupiah(akun.get_saldo()):>30} |")
        print("-" * 75)

    #method untuk menampilkan informasi akun
    def info_akun(self):
        print(f"Pemilik Akun: {self.pemilik}")
        print(f"Saldo Awal  : {self.format_rupiah(self.__saldo)}")
        # print(f"Log Transaksi: {len(self.__log)} transaksi tercatat.")

    # Method getter untuk membaca saldo (tanpa bisa diubah langsung)
    def get_saldo(self):
        return self.__saldo

    # Method setter untuk memperbarui saldo dengan validasi
    def set_saldo(self, jumlah):
        if jumlah < 0:
            print("Jumlah saldo tidak boleh negatif!")
        else:
            self.__saldo = jumlah
            print(f"Saldo berhasil diperbarui menjadi: {self.format_rupiah(self.__saldo)}")

    # Metode untuk menambah saldo
    def deposit(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Saldo bertambah: {self.format_rupiah(jumlah)}, Saldo sekarang: {self.format_rupiah(self.__saldo)}")
            self.__log.append(
                f"| {str(date.today()):<15} | {'Deposit':<20} | {self.format_rupiah(jumlah):>20} | {self.format_rupiah(self.__saldo):>20} |"
            )
        else:
            print("Jumlah deposit harus positif!")

    # Metode untuk menarik saldo
    def withdraw(self, jumlah):
        if jumlah > 0 and jumlah <= self.__saldo:
            self.__saldo -= jumlah
            self.__log.append(
                f"| {str(date.today()):<15} | {'Penarikan':<20} | {self.format_rupiah(jumlah):>20} | {self.format_rupiah(self.__saldo):>20} |"
            )
            print(f"Berhasil menarik: {self.format_rupiah(jumlah)}, Saldo sekarang: {self.format_rupiah(self.__saldo)}")
        else:
            print("Penarikan gagal: saldo tidak mencukupi atau jumlah tidak valid")

    # Metode untuk menampilkan log transaksi
    def tampilkan_log(self):
        print(self.__log_header, end="")
        for entry in self.__log:
            print(entry)
        print("-" * 80)

daftar_akun = [
    BankAccount("Anindya Ramadhani",   50000000),
    BankAccount("Aurhel Alana",   72500000),
    BankAccount("Cathleen Nixie",  43000000),
    BankAccount("Fritzy Rosmerian", 98000000),
    BankAccount("Chelsea Davina",   61000000),
    BankAccount("Freya Jayawardana",   35000000),
    BankAccount("Marsha Lenathea",  27500000),
    BankAccount("Angelina Christy",  80000000),
    BankAccount("Abigail Rachel",    92000000),
    BankAccount("Cornelia Vanisha",  45000000),
    BankAccount("Michelle Alexandra",  67000000),
]


def tambah_akun():
    nama = input("Masukkan nama nasabah: ")
    saldo_awal = int(input("Masukkan saldo awal: Rp"))
    akun_baru = BankAccount(nama, saldo_awal)
    daftar_akun.append(akun_baru)
    print("Akun berhasil ditambahkan.\n")

def menu_utama():
    while True:
        print("Menu Bank Account:")
        print("1. Tambah Akun")
        print("2. Tampilkan Nasabah")
        print("3. Detail nasabah")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            tambah_akun()
        elif pilihan == '2':
            print(f"DAFTAR NASABAR BANK JARWO Tanggal {date.today()}\n")
            print("-" * 75)
            print(f"| {'No.':<5} | {'Nama':<30} | {'Saldo':>30} |")
            print("-" * 75)
            for i, akun in enumerate(daftar_akun, start=1):
                print(f"| {i:<5} | {akun.pemilik:<30} | {akun.format_rupiah(akun.get_saldo()):>30} |")
            print("-" * 75)
        elif pilihan == '3':
                print("Pilih detail akun:\n")
                nama_akun = input("Masukkan nama nasabah: ")
                akun_ditemukan = None
                for akun in daftar_akun:
                    if nama_akun.lower() == akun.pemilik.lower():
                        akun_ditemukan = akun
                        break
                if akun_ditemukan:
                    while True:
                        akun_ditemukan.info_akun()
                        print("1. Tambah Saldo")
                        print("2. Tarik Saldo")
                        print("3. Tampilkan Log Transaksi")
                        print("4. Kembali ke Menu Utama")
                        sub_pilihan = input("Masukkan pilihan: ")
                        if sub_pilihan == '1':
                            jumlah = int(input("Masukkan jumlah deposit: Rp"))
                            akun_ditemukan.deposit(jumlah)
                            akun_ditemukan.tampilkan_log()
                        elif sub_pilihan == '2':
                            jumlah = int(input("Masukkan jumlah penarikan: Rp"))
                            akun_ditemukan.withdraw(jumlah)
                            akun_ditemukan.tampilkan_log()
                        elif sub_pilihan == '3':
                            akun_ditemukan.tampilkan_log()
                        else:
                            menu_utama()
                        print("\n")
                else:
                    print("Nasabah tidak ditemukan.\n")
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")
# Contoh Penggunaan
if __name__ == "__main__":
    menu_utama()