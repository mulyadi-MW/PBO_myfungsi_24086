class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

    def info(self):
        print("Merk kendaraan:", self.merk)

class Motor(Kendaraan):
    def __init__(self, merk, warna):
        super().__init__(merk)  # Memanggil __init__ dari kelas induk
        self.warna = warna
        self.jarak_temuh = 4000  # Inisialisasi jarak tempuh ke 0

    def info(self):
        super().info()  # Memanggil info() dari kelas induk
        print("Warna motor:", self.warna)
        print("Jarak tempuh:", self.jarak_temuh, "km")

    def jalan(self):
        print("Motor berjalan")

    def tambah_jarak(self, km):
        """Menambah jarak tempuh motor."""
        self.jarak_temuh += km
        print(f"Jarak tempuh ditambah {km} km. Total sekarang: {self.jarak_temuh} km")

# Contoh penggunaan
m = Motor("Yamaha", "Merah")
m.info()
m.jalan()
m.tambah_jarak(50)  # Menambah 50 km
m.info()  # Menampilkan info lagi setelah penambahan
