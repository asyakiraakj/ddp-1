# Lab 6: Management Jadwal Latihan Coaching Session
# Nama : Khadijah Asy Syakira
# NPM  : 2506610595

MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]

KODE_SESI_TERSEDIA = [
    ["court a",     HARI[0] + JAM[8] + 0,    HARI[0] +  JAM[9] + 40],
    ["court a",     HARI[2] + JAM[8] + 0,    HARI[2] +  JAM[9] + 40],
    ["court b",     HARI[1] + JAM[8] + 0,    HARI[1] +  JAM[9] + 40],
    ["court c",     HARI[0] + JAM[9] + 0,    HARI[0] + JAM[10] + 40],
    ["court d",     HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40],
    ["court e",     HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40]
]

"""
Merepresentasikan jadwal “court a” hari senin 08.00 sampai 09.40, serta hari rabu jam 08.00 sampai 09.40

Jadwal “court b” hari selasa jam 08.00 sampai 09.40
Jadwal “court c” hari senin jam 09.00 sampai 10.40
Jadwal “court d” hari rabu jam 09.00 sampai 10.40
Jadwal “court e” hari rabu jam 09.00 sampai 10.40
"""

sesi_diambil = []

def format_by_coaching_session(sesi_list):
    """Format sesi berdasarkan coaching session"""
    unique_courts = []
    for sesi in sesi_list:
        if sesi[0] not in unique_courts:
            unique_courts.append(sesi[0])

    for court in unique_courts:
        print(f"{court}:")
        for sesi in sesi_list:
            if sesi[0] == court:
                print(f"   {format_waktu_sesi(sesi)}")
    print()

def konversi_hari(hari_value):
    """Konversi nilai hari ke nama hari"""
    # TODO: lengkapi fungsi ini
    # Senin = 0, Selasa = 1, Rabu = 2, Kamis = 3, Jumat = 4, Sabtu = 5, Minggu = 6
    # dijamin value hari_value adalah integer antara 0 sampai 6

def format_waktu_sesi(sesi):
    """Format waktu sesi menjadi string yang mudah dibaca"""
    # TODO: lengkapi fungsi ini
    

def print_menu():
    """Menampilkan menu utama"""
    print("=========== SUSUN JADWAL ===========")
    print("1  Add sesi")
    print("2  Drop sesi")
    print("3  Cek ringkasan")
    print("4  Lihat daftar sesi")
    print("5  Selesai ")
    print("====================================")

def tambah_sesi():
    """Menu untuk menambah sesi"""
    print("Sesi yang tersedia dan grup by coaching session:")
    # TODO: panggil fungsi format_by_coaching_session dengan parameter KODE_SESI_TERSEDIA
    format_by_coaching_session(KODE_SESI_TERSEDIA)

    sesi_input = input("Masukkan nama sesi: ")
    # TODO: lengkapi bagian berikut
    # cari sesi di KODE_SESI_TERSEDIA yang sesuai dengan input
    # jika tidak ditemukan, tampilkan “Sesi latihan tidak ditemukan” (tanpa tanda petik)
    # jika ditemukan, tambahkan ke sesi_diambil
    print()

def hapus_sesi():
    """Menu untuk menghapus sesi"""
    print("Sesi yang diambil dan group by coaching session:")
    # TODO: panggil fungsi format_by_coaching_session dengan parameter sesi_diambil

    sesi_input = input("Masukkan nama sesi: ")
    # TODO: lengkapi bagian berikut
    # cari sesi di sesi_diambil yang sesuai dengan input
    # jika tidak ditemukan, tampilkan “Sesi latihan tidak ditemukan” (tanpa tanda petik)
    # jika ditemukan, hapus dari sesi_diambil
    print()

def cek_ringkasan():
    """Menu untuk mengecek konflik jadwal sesi"""
    # TODO: lengkapi fungsi ini
    # Cek apakah ada sesi yang bentrok di sesi_diambil
    # Jika ada yang bentrok, maka cetak semua kombinasi pasangan sesi latihan yang bentrok tersebut (lihat contoh test case di soal).
    # Jika tidak ada yang bentrok, tampilkan pesan “Tidak ada sesi latihan yang bermasalah” (tanpa tanda petik)

def lihat_daftar_sesi():
    """Menu untuk melihat daftar sesi yang diambil"""
    # TODO: lengkapi fungsi ini
    # Tampilkan semua sesi di sesi_diambil, formatnya sama seperti di fungsi tambah_sesi, HINT: gunakan fungsi format_by_coaching_session
    # Jika sesi_diambil kosong, tampilkan pesan “Belum ada sesi latihan yang diambil” (tanpa tanda petik)

    if # TODO: cek apakah sesi_diambil kosong
        print("Belum ada sesi latihan yang diambil\n")
    else:
        print("daftar sesi yang telah diambil: ")
        # TODO: panggil fungsi format_by_coaching_session dengan parameter sesi_diambil

def main():
    """Fungsi utama program"""
    while True:
        print_menu()
        menu = input("\nMasukkan pilihan: ")
        # Sort sesi_diambil berdasarkan waktu mulai
        sesi_diambil.sort(key=func)

        if menu == "1":
            tambah_sesi()
        elif menu == "2":
            hapus_sesi()
        elif menu == "3":
            cek_ringkasan()
        elif menu == "4":
            lihat_daftar_sesi()
        elif menu == "5":
            print("Terima kasih!")
            break
        else:
            print("Maaf, pilihan tidak tersedia\n")

def func(e) :
    """kode untuk mengembalikan waktu mulai sesi"""
    return e[1]

if __name__ == "__main__":
    main()

