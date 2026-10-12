class PersegiPanjang:
    # Class variable: jumlah object persegi panjang yang dibuat
    jumlah = 0

    # Constructor: dijalankan otomatis saat object dibuat
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        PersegiPanjang.jumlah += 1

    # Method dengan return: menghitung luas
    def hitung_luas(self):
        return self.panjang * self.lebar

    # Method dengan return: menghitung keliling
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    # Method dengan parameter: mengubah ukuran
    def ubah_ukuran(self, panjang_baru, lebar_baru):
        self.panjang = panjang_baru
        self.lebar = lebar_baru

    # Method dengan parameter dan return: membandingkan luas dengan object lain
    def lebih_besar_dari(self, lain):
        return self.hitung_luas() > lain.hitung_luas()

    # Method untuk menampilkan hasil lengkap
    def tampilkan_info(self):
        print(f"Panjang  : {self.panjang}")
        print(f"Lebar    : {self.lebar}")
        print(f"Luas     : {self.hitung_luas()}")
        print(f"Keliling : {self.hitung_keliling()}")

    # Class method: mengambil jumlah object
    @classmethod
    def total_object(cls):
        return cls.jumlah


# ===== Program utama =====
pp1 = PersegiPanjang(10, 5)
pp2 = PersegiPanjang(8, 8)

print("=== Persegi Panjang 1 ===")
pp1.tampilkan_info()

print()
print("=== Persegi Panjang 2 ===")
pp2.tampilkan_info()

print()
if pp1.lebih_besar_dari(pp2):
    print("Persegi panjang 1 lebih luas dari persegi panjang 2")
else:
    print("Persegi panjang 1 tidak lebih luas dari persegi panjang 2")

print()
print("=== Setelah ukuran pp1 diubah ===")
pp1.ubah_ukuran(12, 6)
pp1.tampilkan_info()

print()
print(f"Total object dibuat = {PersegiPanjang.total_object()}")