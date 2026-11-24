# CLASS DAN OBJECT
class Perpustakaan:
    def __init__(self):
        self.nama = "Perpustakaan Daerah"
        self.alamat = "Jl. Jenderal Sudirman No. 45, Serang"
        self.koleksi_buku = 15000

    def info_perpustakaan(self):
        print(f"Informasi Gedung: {self.nama} beralamat di {self.alamat}.")
        print(f"Jumlah Total Koleksi Buku: {self.koleksi_buku} Eksemplar.")
        print("Fasilitas: Ruang baca ber-AC, WiFi gratis, dan area diskusi kelompok.")

class Pengunjung:
    # Class Attribute
    tempat = "Perpustakaan Daerah"
    
    # Constructor untuk data pengunjung
    def __init__(self, nama, kegiatan, umur, perpustakaan):
        self.nama = nama
        self.kegiatan = kegiatan
        self.umur = umur
        self.perpustakaan = perpustakaan

    # Method perkenalan
    def kenalan(self):
        print(f"Halo, salam kenal nama saya {self.nama}.")
        print(f"Saat ini usia saya menginjak {self.umur} tahun.")
        print(f"Kegiatan utama saya hari ini yaitu {self.kegiatan}.")
        print(f"Lokasi saya sekarang berada di dalam {self.perpustakaan}.")
        print("Saya sangat senang bisa berkunjung ke sini untuk menambah wawasan.")

    # Method percakapan sapaan
    def hello(self, nama):
        print(f"Halo {nama}, senang bisa bertemu denganmu kembali di sini.")
        print("Bagaimana kabar perkuliahan dan tugas-tugasmu sejauh ini?")
        print(f"Usia kita sama yaitu {self.umur} tahun, jadi kita bisa lebih nyambung kalau ngobrol.")
        print("Mari kita manfaatkan waktu luang ini dengan hal-hal yang positif.")

    # Method menampilkan kegiatan
    def kegiatan_pengunjung(self):
        print(f"Identitas Pengunjung: Nama saya {self.nama}.")
        print(f"Status Kegiatan: Saya sedang {self.kegiatan}.")
        print("Rutinitas ini sangat membantu saya dalam menyelesaikan tugas akademik tepat waktu.")

    # Method percakapan panjang antara dua pengunjung
    def percakapan(self, teman):
        print("===== PERCAKAPAN PANJANG DAN MENDALAM DI PERPUSTAKAAN =====")
        print(f"{self.nama}: Halo Dini, selamat siang menjelang sore! Wah, tidak disangka kita bisa bertemu di rak buku komputer.")
        print(f"{teman.nama}: Halo juga Hadi! Selamat siang. Iya nih, kebetulan banget jadwal kuliah kita lagi kosong.")
        print(f"{self.nama}: Ngomong-ngomong, dari tadi saya perhatikan kamu serius banget baca buku. Lagi cari referensi apa emangnya?")
        print(f"{teman.nama}: Aku lagi cari referensi materi Pemrograman Berorientasi Objek, khususnya tentang penerapan Class, Object, dan Constructor di Python.")
        print(f"{self.nama}: Wah, seriusan? Topik itu kan yang lagi kita pelajari dari dosen kita, Pak Dieng Asep Jamaludin.")
        print(f"{teman.nama}: Betul sekali, Hadi! Makanya aku pengen paham lebih dalam supaya tugas kodingnya nanti tidak ada yang salah.")
        print(f"{self.nama}: Kebetulan banget kalau gitu. Aku juga baru selesai merangkum materi tentang penggunaan Method dan atribut dalam suatu Class.")
        print(f"{teman.nama}: Kalau begitu, maukah kamu meluangkan waktu sebentar buat menjelaskan beberapa baris kode yang bikin aku pusing?")
        print(f"{self.nama}: Dengan senang hati, Dini! Belajar bareng justru bakal jauh lebih cepat masuk ke kepala ketimbang belajar sendirian.")
        print(f"{teman.nama}: Asyik! Oh iya, nanti setelah ini kita cari meja kosong di dekat jendela sudut utara yuk, udaranya lebih adem.")
        print(f"{self.nama}: Ide bagus. Tapi sebelum itu, coba kamu pinjam dulu dua buku panduan Python itu di meja sirkulasi.")
        print(f"{teman.nama}: Siap, nanti aku yang urus peminjamannya di petugas perpustakaan.")
        print(f"{self.nama}: Mantap! Kalau semua tugas ini selesai cepat, bagaimana kalau kita lanjut mampir ke kafe depan buat ngopi bareng?")
        print(f"{teman.nama}: Ide yang menarik, tapi traktir ya kalau nilainya nanti dapat A haha!")
        print(f"{self.nama}: Siap diatur kalau itu! Yang penting kita fokus belajar dulu sekarang.")
        print(f"{teman.nama}: Oke deh, mari kita mulai diskusinya sekarang juga.")

# Membuat object perpustakaan
perpus1 = Perpustakaan()

# Menampilkan informasi perpustakaan
print("===== INFORMASI GEDUNG PERPUSTAKAAN =====")
perpus1.info_perpustakaan()
print()

# Membuat object pengunjung pertama (Hadi, 19 tahun)
pengunjung1 = Pengunjung("Hadi", "Mencari literatur dan berdiskusi", 19, perpus1.nama)

# Membuat object pengunjung kedua (Dini, 19 tahun)
pengunjung2 = Pengunjung("Mempelajari modul pemrograman", 19, perpus1.nama)

# Memanggil method perkenalan
print("===== PERKENALAN PENGUNJUNG =====")
pengunjung1.kenalan()
print()
pengunjung2.kenalan()
print()

# Memanggil method kegiatan
print("===== KEGIATAN PENGUNJUNG =====")
pengunjung1.kegiatan_pengunjung()
print()
pengunjung2.kegiatan_pengunjung()
print()