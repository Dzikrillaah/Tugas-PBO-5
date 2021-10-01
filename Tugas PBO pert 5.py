class UPI:
    def intro(self):
        print("UPI merupakan salah satu perguruan tinggi negeri yang ada di Indonesia")

    def deskripsi(self):
        print("Kampus UPI bukan hanya terletak di Bandung, namun ada juga yang terletak di Serang")

class Bumsil(UPI):
    def deskripsi(self):
        print("Bumsil Merupakan Kampus UPI yang ada di Bandung")

class Serang(UPI):
    def deskripsi(self):
        print("Serang Merupakan Kota lain dimana UPI berada, sebagai kampus daerah")

obj_UPI = UPI()
obj_Bumsil = Bumsil()
obj_Serang = Serang()

obj_UPI.intro()
obj_UPI.deskripsi()

obj_Bumsil.intro()
obj_Bumsil.deskripsi()

obj_Serang.intro()
obj_Serang.deskripsi()