class Hero:
    """Kelas untuk merepresentasikan seorang hero."""

    def __init__(self, name: str, power: int):
        # Atribut diisi langsung saat objek dibuat
        self.name = name
        self.power = power

    def introduce(self):
        """Memperkenalkan diri."""
        print(f"Namaku {self.name}, power-ku {self.power}")

    def train(self, amount: int = 10):
        """Menambah power setelah latihan."""
        self.power += amount
        print(f"{self.name} berlatih! Power naik jadi {self.power}")

    def __str__(self):
        # Tampilan saat objek di-print
        return f"Hero(name={self.name}, power={self.power})"


# Membuat objek
hero_1 = Hero("Goku", 100)
hero_2 = Hero("Vegeta", 90)

# Mengakses atribut
print(hero_1.name)      # Goku
print(hero_2.name)      # Vegeta

# Memanggil method
hero_1.introduce()
hero_2.train(20)

# Print objek (memakai __str__)
print(hero_1)
print(hero_2)

# Melihat semua atribut dalam bentuk dictionary
print(hero_1.__dict__)  # {'name': 'Goku', 'power': 100}

# Membandingkan power
if hero_1.power > hero_2.power:
    print(f"{hero_1.name} lebih kuat!")
elif hero_1.power < hero_2.power:
    print(f"{hero_2.name} lebih kuat!")
else:
    print("Kekuatan mereka seimbang!")