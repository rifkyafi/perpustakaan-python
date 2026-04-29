from abc import ABC, abstractmethod

class Koleksi(ABC):
    def __init__(self, judul, tahun_terbit, penerbit, kode):
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit
        self.kode = kode
        # self.edisi = edisi

    @abstractmethod
    def tampilkan_info(self):
        pass


# class Buku
class Buku(Koleksi):
    def __init__(self, kode, judul, tahun_terbit, pengarang, penerbit):
        super().__init__(judul, tahun_terbit, penerbit, kode)
        self.pengarang = pengarang

    def tampilkan_info(self):
        print(
            "DATA BUKU\n"
            f"Masukkan Kode Buku    : {self.kode}\n"
            f"Masukkan Judul Buku   : {self.judul}\n"
            f"Masukkan Tahun Terbit : {self.tahun_terbit}\n"
            f"Masukkan Pengarang    : {self.pengarang}\n"
            f"Masukkan Penerbit     : {self.penerbit}\n"
        )


# class Majalah
class Majalah(Koleksi):
    def __init__(self, kode, judul, tahun_terbit, edisi, penerbit):
        super().__init__(judul, tahun_terbit, penerbit, kode)
        self.edisi = edisi

    def tampilkan_info(self):   
        print(
            "DATA MAJALAH\n"
            f"Masukkan Kode Koleksi    : {self.kode}\n"
            f"Masukkan Judul           : {self.judul}\n"
            f"Masukkan Tahun Terbit    : {self.tahun_terbit}\n"
            f"Masukkan Penerbit        : {self.penerbit}\n"
            f"Masukkan Edisi           : {self.edisi}\n"
        )


# class Jurnal
class Jurnal(Koleksi):
    def __init__(self, kode, judul, tahun_terbit, tanggal_terbit, penerbit, bidang_studi, impact_factor):
        super().__init__(judul, tahun_terbit, penerbit, kode)
        self.tanggal_terbit = tanggal_terbit
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor

    def tampilkan_info(self):
        print(
            "DATA JURNAL\n"
            f"Masukkan Kode Koleksi    : {self.kode}\n"
            f"Masukkan Judul           : {self.judul}\n"
            f"Masukkan Tahun Terbit    : {self.tahun_terbit}\n"
            f"Masukkan Penerbit        : {self.penerbit}\n"
            f"Masukkan Tanggal Terbit  : {self.tanggal_terbit}\n"
            f"Masukkan Bidang Studi    : {self.bidang_studi}\n"
            f"Masukkan Impact Factor   : {self.impact_factor}\n"
        )

#Class DVD
class DVD(Koleksi):
    def __init__(self, kode, judul, tahun_terbit, sutradara, durasi, penerbit):
        super().__init__(judul, tahun_terbit, penerbit, kode)
        self.sutradara = sutradara
        self.durasi = durasi

    def tampilkan_info(self):
        print(
            "DATA DVD\n"
            f"Kode        : {self.kode}\n"
            f"Judul       : {self.judul}\n"
            f"Tahun Terbit: {self.tahun_terbit}\n"
            f"Sutradara   : {self.sutradara}\n"
            f"Durasi      : {self.durasi} menit\n"
            f"Penerbit    : {self.penerbit}\n"
        )

# Menu Koleksi
daftar_koleksi = []

def tambah_data():
    print("Pilih Jenis Koleksi:")
    print("1. Buku")
    print("2. Majalah")
    print("3. Jurnal")
    print("4. DVD")
    pilihan = input("Masukkan pilihan (1/2/3): ")
    print( "input tidak ada")

    if pilihan == '1':
        kode = input("Masukkan Kode Buku: ")
        judul = input("Masukkan Judul Buku: ")
        tahun_terbit = input("Masukkan Tahun Terbit: ")
        pengarang = input("Masukkan Pengarang: ")
        penerbit = input("Masukkan Penerbit: ")
        buku = Buku(kode, judul, tahun_terbit, pengarang, penerbit)
        daftar_koleksi.append(buku)
        print("Data buku berhasil ditambahkan.\n")

    elif pilihan == '2':
        kode = input("Masukkan Kode Majalah: ")
        judul = input("Masukkan Judul Majalah: ")
        tahun_terbit = input("Masukkan Tahun Terbit: ")
        edisi = input("Masukkan Edisi: ")
        penerbit = input("Masukkan Penerbit: ")
        majalah = Majalah(kode, judul, tahun_terbit, edisi, penerbit)
        daftar_koleksi.append(majalah)
        print("Data majalah berhasil ditambahkan.\n")

    elif pilihan == '3':
        kode = input("Masukkan Kode Jurnal: ")
        judul = input("Masukkan Judul Jurnal: ")
        tahun_terbit = input("Masukkan Tahun Terbit: ")
        tanggal_terbit = input("Masukkan Tanggal Terbit (DD/MM/YY): ")
        penerbit = input("Masukkan Penerbit: ")
        bidang_studi = input("Masukkan Bidang Studi: ")
        impact_factor = input("Masukkan Impact Factor: ")
        koran = Jurnal(kode, judul, tahun_terbit, tanggal_terbit, penerbit, bidang_studi, impact_factor)
        daftar_koleksi.append(koran)
        print("Data koran berhasil ditambahkan.\n")

    elif pilihan == '4':
        kode = input("Masukkan Kode DVD: ")
        judul = input("Masukkan Judul DVD: ")
        tahun_terbit = input("Masukkan Tahun Terbit: ")
        sutradara = input("Masukkan Sutradara: ")
        durasi = input("Masukkan Durasi (menit): ")
        penerbit = input("Masukkan Penerbit: ")
        dvd = DVD(kode, judul, tahun_terbit, sutradara, durasi, penerbit)
        daftar_koleksi.append(dvd)
        print("Data DVD berhasil ditambahkan.\n")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")

#Menghapus Data
def hapus_data():
    print(
        "----------------------------------------------\n"
        "HAPUS DATA KOLEKSI\n"
    )
    kode = input("Masukkan Kode Koleksi: ")

    global daftar_koleksi
    for i, koleksi in enumerate(daftar_koleksi):
        if koleksi.kode == kode:
            del daftar_koleksi[i]
            print("Data koleksi berhasil dihapus.\n")
            return

    print("Kode koleksi tidak ditemukan.\n")

# Menampilkan Semua Koleksi
def tampilkan_semua():
    print(
        "----------------------------------------------\n"
        "DAFTAR KOLEKSI\n"
    )
    if not daftar_koleksi:
        print("Tidak ada koleksi yang tersedia.\n")
    else:
        for i, item in enumerate(daftar_koleksi, start=1):
            print(
                f"Koleksi {i}:\n"
                )
            item.tampilkan_info()
            print("\n")
    
    print("----------------------------------------------\n")
    input("Tekan Enter untuk kembali ke menu utama...")

# Menu utama
def menu_utama():
    while True:
        print("Menu Koleksi:")
        print("1. Tambah Koleksi")
        print("2. Hapus Koleksi")
        print("3. Tampilkan Semua Koleksi")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            hapus_data()
        elif pilihan == '3':
            tampilkan_semua()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

if __name__ == "__main__":
    menu_utama()