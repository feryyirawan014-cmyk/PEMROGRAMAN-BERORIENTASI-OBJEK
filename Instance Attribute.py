class Mahasiswa:

    # Class variable (dimiliki bersama oleh semua object)
    jumlah_mahasiswa = 0

    def __init__(self, name, nim, prodi):
        self.name = name
        self.nim = nim
        self.prodi = prodi
        Mahasiswa.jumlah_mahasiswa += 1
        print("Membuat Object Mahasiswa dengan nama " + self.name)

    # Instance method: menampilkan data mahasiswa
    def tampilkan_data(self):
        print("Nama   : " + self.name)
        print("NIM    : " + self.nim)
        print("Prodi  : " + self.prodi)

    # Class method: mengambil total mahasiswa
    @classmethod
    def total_mahasiswa(cls):
        return cls.jumlah_mahasiswa

    # Destructor: dipanggil saat object dihapus
    def __del__(self):
        Mahasiswa.jumlah_mahasiswa -= 1
        print("Menghapus Object Mahasiswa dengan nama " + self.name)


# --- Program utama ---
mhs1 = Mahasiswa("Fira", "25241007", "Teknik Informatika")
print("Total Mahasiswa : " + str(mhs1.jumlah_mahasiswa))

mhs2 = Mahasiswa("Ika", "25241028", "Teknik Industri")
print("Total Mahasiswa : " + str(mhs2.jumlah_mahasiswa))

print()
print("Total Mahasiswa : " + str(Mahasiswa.jumlah_mahasiswa))

print()
print("=== Data Mahasiswa ===")
mhs1.tampilkan_data()
print()
mhs2.tampilkan_data()

print()
print("Total via class method :", Mahasiswa.total_mahasiswa())

# Menghapus object mhs2
print()
del mhs2
print("Total Mahasiswa setelah dihapus : " + str(Mahasiswa.jumlah_mahasiswa))