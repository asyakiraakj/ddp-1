# --- Title ---
print('''<><><><><><><><><><><><><><><><><><>
|                                  |
|         Library Perpucil         |
|                                  |
<><><><><><><><><><><><><><><><><><>
''')

import math

# TODO: --- Pengambilan input ---
nama_peminjam = input("Masukkan Nama peminjam: ")
npm_peminjam = int(input("Masukkan NPM Peminjam: "))
nama_buku = input("Masukkan Nama Buku yang dipinjam: ")
tarif_per_hari = int(input("Masukkan Tarif Pinjaman per Hari: "))

# TODO: --- Pengambilan input yang perlu divalidasi ---
# TODO: Gunakan loop untuk validasi input
    # TODO: --- Pengambilan input ---
while True:
    print()
    bulan_peminjaman = int(input("Masukkan Bulan Peminjam: "))
    tanggal_peminjaman = int(input("Masukkan Tanggal Peminjam: "))

    print()
    bulan_pengembalian = int(input("Masukkan Bulan Pengembalian: "))
    tanggal_pengembalian = int(input("Masukkan Tanggal Pengembalian: "))

    # --- Validasi input ---
    # TODO: Pengecekan bulan (1-12)
    if not (1 <= bulan_peminjaman <= 12):
        print("Input bulan tidak valid. Harus dalam rentang 1-12.")
        continue

    # TODO: Pengecekan tanggal (1-30)
    if not (1 <= tanggal_peminjaman <= 30):
        print("Input tanggal tidak valid. Harus dalam rentang 1-30.")
        continue

    # TODO: Pengecekan peminjaman sebelum pengembalian
    if (bulan_pengembalian < bulan_peminjaman):
        print("Peminjaman harus dilakukan sebelum pengembalian!")
    elif bulan_pengembalian == bulan_peminjaman:
            if tanggal_pengembalian < tanggal_peminjaman:
                print("Peminjaman harus dilakukan sebelum pengembalian!")
            continue

    # TODO: Dibebaskan menambahkan conditional jika merasa dibutuhkan.

    break

# TODO: --- Total hari ---

total_hari = (bulan_pengembalian - bulan_peminjaman)*30 + (tanggal_pengembalian - tanggal_peminjaman)

# TODO: --- Unique ID ---
unique_id = hex(round(npm_peminjam // len(nama_peminjam)))

# tarif
tarif_bersih = total_hari*tarif_per_hari
tarif_dengan_pajak = round(tarif_bersih + 0.5 * math.sqrt(tarif_bersih))

# TODO: --- Success message ---
print()
print("--- Checkout Peminjaman ---")
# TODO: Lanjutkan print sesuai output yang diharapkan
bulan_lama_peminjaman = total_hari // 30
minggu_lama_peminjaman = (total_hari % 30) // 7
hari_lama_peminjaman = total_hari - ((bulan_lama_peminjaman)*30 + (minggu_lama_peminjaman*7))

print(f"Pembeli dengan Unique ID {unique_id} melakukan transaksi peminjaman buku {nama_buku} selama {bulan_lama_peminjaman} bulan, {minggu_lama_peminjaman} minggu, {hari_lama_peminjaman} hari dengan total biaya pinjaman sebesar Rp {tarif_dengan_pajak}.")
