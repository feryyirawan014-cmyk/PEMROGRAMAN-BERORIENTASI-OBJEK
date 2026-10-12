class Hero:
    # class variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1

    def siapa(self):
        return f"{self.name} memiliki power {self.power}"

    def healthUp(self, up):
        self.health += up

    def gethealth(self):
        return self.health

    # --- Method tambahan ---
    def healthDown(self, down):
        self.health -= down
        if self.health < 0:
            self.health = 0

    def getarmor(self):
        return self.armor

    def info(self):
        print(f"Nama   : {self.name}")
        print(f"Health : {self.health}")
        print(f"Power  : {self.power}")
        print(f"Armor  : {self.armor}")

    @classmethod
    def total_hero(cls):
        return cls.jumlah


# --- Program utama ---
hero1 = Hero("Sniper", 100, 10, 5)
hero2 = Hero("Axe", 200, 15, 0)

print(hero1.siapa())          # diperbaiki: sebelumnya hero1.print(...)
print(hero2.siapa())

hero1.armor = 10
print(f"Armor {hero1.name} = {hero1.armor}")
print(f"Jumlah hero = {Hero.jumlah}")

hero1.healthUp(20)
print(f"Health {hero1.name} = {hero1.gethealth()}")
print(f"Health {hero2.name} = {hero2.gethealth()}")

# Contoh penggunaan method tambahan
hero2.healthDown(50)
print(f"Health {hero2.name} setelah diserang = {hero2.gethealth()}")

print()
print("=== Info Hero ===")
hero1.info()
print()
hero2.info()

print()
print(f"Total hero via class method = {Hero.total_hero()}")