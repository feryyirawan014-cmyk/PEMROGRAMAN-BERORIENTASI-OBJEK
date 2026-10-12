class Mahasiswa:
    """Kelas untuk merepresentasikan data seorang mahasiswa."""

    # Atribut kelas: dipakai bersama oleh semua objek
    jumlah_mahasiswa = 0

    def __init__(self, name: str, nim: str, prodi: str):
        # Validasi: NIM harus berupa angka
        if not nim.isdigit():
            raise ValueError("NIM harus berupa angka")

        self.name = name
        self.nim = nim
        self.prodi = prodi

        Mahasiswa.jumlah_mahasiswa += 1

    def tampilkan_info(self):
        """Menampilkan data mahasiswa dengan format rapi."""
        print(f"Nama  : {self.name}")
        print(f"NIM   : {self.nim}")
        print(f"Prodi : {self.prodi}")

    def ubah_prodi(self, prodi_baru: str):
        """Mengubah program studi mahasiswa."""
        print(f"Prodi {self.name} diubah dari {self.prodi} menjadi {prodi_baru}")
        self.prodi = prodi_baru

    def __str__(self):
        # Tampilan saat objek di-print
        return f"Mahasiswa(name={self.name}, nim={self.nim}, prodi={self.prodi})"


# Membuat objek
mhs1 = Mahasiswa("Askiyah", "25241012", "Informatika")
mhs2 = Mahasiswa("Fira", "25241007", "Sistem Informasi")

# Menampilkan semua data dengan perulangan (tanpa menulis print berulang)
print("=== Data Mahasiswa ===")
for i, mhs in enumerate([mhs1, mhs2], start=1):
    print(f"Mahasiswa ke-{i}")
    mhs.tampilkan_info()
    print("Dict  :", mhs.__dict__)
    print()

# Memakai __str__
print(mhs1)

# Memanggil method untuk mengubah data
mhs2.ubah_prodi("Teknik Informatika")
print(mhs2)

# Mengakses atribut kelas
print("Total mahasiswa:", Mahasiswa.jumlah_mahasiswa)