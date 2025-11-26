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
    # TODO: implementasi print_tree
    if level == 0:
        print(f"{nama} (root)")
    elif level > 0:
        print(f"{" "*level} + {keluarga[nama]}")

    child = []
    for names in keluarga.keys():
        child = keluarga[nama][0]
        
    return print_tree(child[0], level+1)

    pass  # placeholder

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
    # TODO: implementasi find_member
    if nama == target:
        return keluarga[nama], level
    else:
        return find_member(keluarga[nama], level+1, target)

    return None  # placeholder


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
    # TODO: implementasi count_desc
    if not keluarga[nama] or not keluarga[child]:
        return 0
    else:
        return sum(keluarga[nama]) + count_desc(keluarga[child])


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

        # TODO: tambahkan (child, tahun) ke keluarga[parent]
        keluarga[parent] = (child, tahun)



    elif pilihan == "2":
        # Cetak pohon mulai dari nama akar yang diminta.
        nama_root = input("Masukkan nama akar keluarga: ").strip()

        # TODO: validasi bahwa nama_root ada di data
        if nama_root in keluarga:
            print_tree(nama_root, )
        # TODO: telusuri dan cetak pohon dari nama_root.
        # Gunakan method print_tree 
        


    elif pilihan == "3":
        # Cari anggota: tampilkan (nama, tahun, level), trace mulai dari root.
        target = input("Masukkan nama yang dicari: ").strip()

        # TODO: validasi bahwa nama ada di data
        if target in keluarga.keys():
            find_member(target, 0)
            print(keluarga.items(), )
        # TODO: telusuri dari root dan tentukan level target
        # Gunakan method find_member

        # TODO: cetak tuple (nama, tahun, level) atau pesan tidak ditemukan
        


    elif pilihan == "4":
        # Hitung total keturunan (langsung + tak langsung).
        nama = input("Masukkan nama: ").strip()


        # TODO: validasi nama ada di data
        if nama in keluarga.keys():
            print(count_desc(nama))
        # TODO: hitung total keturunan dari 'nama'
        # Gunakan method count_desc

        # TODO: cetak jumlah keturunan


    elif pilihan == "5":
        print("Program selesai. Terima kasih telah membantu Dek Depe!")
        break

    else:
        print("Pilihan tidak valid.\n")
