"""
Maps Graph Of Sichuan Province, China
This program was made by kelompok 1 Struktur Data UNESA to fulfill project from our teacher Mr. I Gde Agung Sri Sidhimantra S.Kom M.Kom

Our member
1. Sekar Hanum (148)
2. Adip Setyaputra (158)
3. Regha Rahmadian Bintang (156)

See more on our github
{github}

"""

class Peta:
    def __init__(self):
        self.listkota = {}

    def tambahkota(self,kota):
        if kota not in self.listkota:
            self.listkota[kota] = {}
            print(f'Kota {kota} ditambahkan kedalam Peta')
    
    def tambahJalan(self,kota1,kota2,jarak):
        if kota1 and kota2 in self.listkota:
            self.listkota[kota1][kota2] = jarak
            self.listkota[kota2][kota1] = jarak
            print(f'Jalan antara kota {kota1} dan kota {kota2} sejauh {jarak}Km telah ditambahkan ke dalam Peta')
        elif kota1 not in self.listkota:
            print(f'Error, Kota {kota1} tidak ada dalam peta')
        elif kota2 not in self.listkota:
            print(f'Error, Kota {kota2} tidak ada dalam peta')
        else:
            print(f'Error, Kota {kota1} dan kota {kota2} tidak ada dalam peta')

    def hapusKota(self,kotadihapus):
        if kotadihapus in self.listkota:
            for kota in self.listkota:
                if kotadihapus in self.listkota[kota]:
                    del self.listkota[kota][kotadihapus]
            del self.listkota[kotadihapus]
            print(f'Kota {kotadihapus} telah dihapus dari Peta')

    def hapusjalan(self,kota1,kota2):
        if kota1 and kota2 in self.listkota:
            del self.listkota[kota1][kota1]
            del self.listkota[kota2][kota1]
            print(f'Jalan antara kota {kota1} dan kota {kota2} telah dihapus dari Peta')
