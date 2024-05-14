"""
Maps Graph Of Sichuan Province, China
This program was made by kelompok 1 Struktur Data UNESA to fulfill project from our teacher Mr. I Gde Agung Sri Sidhimantra S.Kom M.Kom

Our member
1. Sekar Hanum (148)
2. Adip Setyaputra (158)
3. Regha Rahmadian Bintang (156)

See more on our github
{https://github.com/SekarHanum/Graph-Kota-Weightened-Struktur-Data-Tugas-2}

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
        
    def hitungkota(self):
        hitungan = 0
        for kota in self.listkota:
            if kota in self.listkota:
                hitungan += 1
        print(f'Jumlah kota yang ada pada peta ada {hitungan} kota')
        return hitungan
    
    def dijkstra(self,kota_asal):
        kota_belum_dikunjungi = [*self.listkota.keys()]
        rute = {}
        jarak_dilalui = {}

        for kota in kota_belum_dikunjungi:
            jarak_dilalui[kota] = float("inf")
        jarak_dilalui[kota_asal] = 0

        while kota_belum_dikunjungi:
            kota_terdekat = None
            for kota in kota_belum_dikunjungi:
                if kota_terdekat == None:
                    kota_terdekat = kota
                elif jarak_dilalui[kota] < jarak_dilalui[kota_terdekat]:
                    kota_terdekat = kota

            for kota_tetangga,jarak in self.listkota[kota_terdekat].items():
                total_jarak = (jarak_dilalui[kota_terdekat] + jarak)
                if total_jarak < jarak_dilalui[kota_tetangga]:
                    rute[kota_tetangga] = kota_terdekat
                    jarak_dilalui[kota_tetangga] = total_jarak
            kota_belum_dikunjungi.remove(kota_terdekat)

        del jarak_dilalui[kota_asal]
        return jarak_dilalui
    
    def jarakseluruhkota(self,kota_asal):
        if kota_asal not in self.listkota:
            print(f'Kota {kota_asal} tidak ada dalam peta')
        else:
            rute_kota = self.dijkstra(kota_asal) 
            print(f'Jarak setiap kota dari kota {kota_asal} adalah:')
            for kota,jarak in rute_kota.items():
                print(f'kota {kota} dengan jarak {jarak}Km')

    def printpeta(self):
        for kota in self.listkota:
            print(f'[ {kota} ]')
            for kota,jarak in self.listkota[kota].items():
                print(f'-> {kota} {jarak}Km')

SiChuan_Province = ["Garze Tibetan","Liangshan Yi","Panzhihua","Yaan","Meishan","Leshan","Chengdu","Deyang","Dazhou","Nanchong","Guang'an","Suining","Ziyang","Neijiang","Zigong","Yibin","Luzhou"]
