# TEMPLATE: Sistem Silsilah Keluarga Digital (sederhana, tanpa utilitas umum)
# Ide umum: simpan anak di dict {orang_tua: [(anak, tahun), ...]}

keluarga = {}   # { "Nama": [("NamaAnak", tahun), ...], ... }
# CONTOH:
# keluarga = {
#     "Andi": [("Budi", 1980), ("Cici", 1985)],
#     "Budi": [("Deni", 2005)],
#     "Cici": [],
#     "Deni": []
# }

root = None     # maksimal 1 root, sesuaikan saat pertama kali tambah anggota keluarga



# =========================
# Method helper, silakan ubah sesuai kebutuhan
# =========================
def print_tree(nama: str, level: int):
    """
    Cetak pohon keluarga mulai dari 'nama' sebagai akar lokal.
    Aturan cetak:
    - Jika level == 0, tampilkan: "<nama> (root)"
    - Jika level > 0:
        - Jika tahun tersedia: "  " * level + "<nama> (<tahun>)"
        - Jika tidak:          "  " * level + "<nama>"
    - Lalu, untuk setiap anak dari 'nama', panggil print_tree(anak, level+1)

    Lakukan:
    - Cetak baris untuk node saat ini sesuai aturan di atas.
    - Ambil daftar anak dari 'keluarga[nama]' jika ada.
    - Rekursi memanggil dirinya untuk setiap anak dengan level+1.
    """
    # cari tahun lahir 'nama' jika tersedia (dicatat pada daftar anak siapa pun)
    tahun = None
    for parent, anak_list in keluarga.items():
        for (anak, t) in anak_list:
            if anak == nama:
                tahun = t
                break
        if tahun is not None:
            break

    # cetak baris untuk node saat ini
    if level == 0:
        print(f"{nama} (root)")
    else:
        if tahun is not None:
            print("  " * level + f"{nama} ({tahun})")
        else:
            print("  " * level + f"{nama}")

    # ambil daftar anak dan rekursi
    anak_list = keluarga.get(nama, [])
    for (anak, _) in anak_list:
        print_tree(anak, level + 1)


def find_member(nama: str, level: int, target: str):
    """
    Cari 'target' mulai dari node 'nama' (Depth-First Search).
    Return:
    - Jika ketemu: tuple (nama, tahun_atau_-1, level)
        * Gunakan -1 jika tahun tidak diketahui (None)
    - Jika tidak ketemu: None

    Langkah umum:
    1) Basis: jika nama == target -> siapkan tuple hasil dan kembalikan.
    2) Jika 'nama' punya anak:
       - Telusuri satu per satu anak (rekursi: find_member(anak, level+1, target)).
       - Jika ada yang ketemu, langsung kembalikan hasilnya.
    3) Jika semua anak tidak ketemu -> kembalikan None.
    """
    # basis: jika node saat ini adalah target
    if nama == target:
        # cari tahun seperti pada aturan (tahun disimpan di daftar anak parent)
        tahun = None
        for parent, anak_list in keluarga.items():
            for (anak, t) in anak_list:
                if anak == nama:
                    tahun = t
                    break
            if tahun is not None:
                break

        return (nama, tahun if tahun is not None else -1, level)

    # rekursi pada anak-anak
    for (anak, _) in keluarga.get(nama, []):
        res = find_member(anak, level + 1, target)
        if res is not None:
            return res

    return None


def count_desc(nama: str) -> int:
    """
    Hitung jumlah keturunan (anak langsung + cucu + dst) dari 'nama'.
    Rumus umum (rekursi):
      total = jumlah_anak_langsung(nama) + sum(count_desc(anak) untuk setiap anak)

    Lakukan:
    - Ambil daftar anak 'nama' dari dict (jika tidak ada, anggap 0).
    - Jumlahkan panjang daftar anak + hasil rekursi count_desc untuk tiap anak.
    - Kembalikan total.
    """
    anak_list = keluarga.get(nama, [])
    total = len(anak_list)
    for (anak, _) in anak_list:
        total += count_desc(anak)
    return total

print("========================================")
print("SISTEM SILSILAH KELUARGA DIGITAL")
print("========================================\n")
print("Menu:")
print("1. Tambah anggota keluarga")
print("2. Tampilkan pohon keluarga")
print("3. Cari anggota keluarga")
print("4. Hitung jumlah keturunan")
print("5. Keluar")
while True:
    pilihan = input("\nMasukkan pilihan (1-5): ").strip()

    if pilihan == "1":
        # Tambah (parent)-(child, tahun). Set root jika masih None.
        parent = input("Nama orang tua: ").strip()
        child  = input("Nama anak baru: ").strip()
        tahun  = int(input("Tahun lahir anak: ").strip())

        # Inisialisasi key parent jika belum ada
        if parent not in keluarga:
            keluarga[parent] = []

        # Inisialisasi key child jika belum ada
        if child not in keluarga:
            keluarga[child] = []

        # Jika root None, set root = parent
        if root is None:
            root = parent

        # tambahkan (child, tahun) ke keluarga[parent]
        keluarga[parent].append((child, tahun))



    elif pilihan == "2":
        # Cetak pohon mulai dari nama akar yang diminta.
        nama_root = input("Masukkan nama akar keluarga: ").strip()

        # validasi bahwa nama_root ada di data
        if nama_root not in keluarga:
            print("Nama akar tidak ditemukan dalam data.")
            continue

        # telusuri dan cetak pohon dari nama_root.
        print_tree(nama_root, 0)
        


    elif pilihan == "3":
        # Cari anggota: tampilkan (nama, tahun, level), trace mulai dari root.
        target = input("Masukkan nama yang dicari: ").strip()

        # validasi bahwa nama ada di data
        if target not in keluarga:
            print("Nama tidak ditemukan dalam data.")
            continue

        if root is None:
            print("Belum ada root. Tambahkan anggota terlebih dahulu.")
            continue

        # telusuri dari root dan tentukan level target
        res = find_member(root, 0, target)

        # cetak tuple (nama, tahun, level) atau pesan tidak ditemukan
        if res is None:
            print("Anggota tidak ditemukan pada pohon yang dimulai dari root.")
        else:
            print(res)



    elif pilihan == "4":
        # Hitung total keturunan (langsung + tak langsung).
        nama = input("Masukkan nama: ").strip()


        # validasi nama ada di data
        if nama not in keluarga:
            print("Nama tidak ditemukan dalam data.")
            continue

        # hitung total keturunan dari 'nama'
        total = count_desc(nama)

        # cetak jumlah keturunan
        print(f"Jumlah keturunan dari {nama}: {total}")



    elif pilihan == "5":
        print("Program selesai. Terima kasih telah membantu Dek Depe!")
        break

    else:
        print("Pilihan tidak valid.\n")
