# entri = int(input("Masukkan Entri : "))

# halaman = ((entri - 1) // 12 ) + 1
# baris = (((entri - 1) // 3) + 1 ) - ((halaman - 1) * 4)
# baris = (((entri - 1) // 3) + 1 ) - ((halaman - 1) * 4)
# #baris = ((entri - ((halaman - 1) * 12)) // 3) + 1
# #kolom = ((entri - ((baris - 1) * 3)) // 4) + 1
# kolom = ((entri - 1) % 3 ) + 1

# print(f"Entri ke {entri} berada di halaman {halaman}, baris {baris} dan kolom {kolom}")


# TODO: --- Pengambilan input yang perlu divalidasi ---
# TODO: Gunakan loop untuk validasi input
# TODO: --- Pengambilan input ---
print()
bulan_peminjaman = int(input("Masukkan Bulan Peminjaman: "))
tanggal_peminjaman = int(input("Masukkan Tanggal Peminjaman: "))

print()
bulan_pengembalian = int(input("Masukkan Bulan Pengembalian: "))
tanggal_pengembalian = int(input("Masukkan Tanggal Pengembalian: "))

if tanggal_peminjaman > tanggal_pengembalian:
    selisih_tanggal = tanggal_peminjaman - tanggal_pengembalian
elif tanggal_pengembalian > tanggal_peminjaman:
    selisih_tanggal = tanggal_pengembalian - tanggal_peminjaman
else:
    selisih_tanggal = 0
print(selisih_tanggal)

total_hari = (bulan_pengembalian - bulan_peminjaman)*30 + selisih_tanggal
print(total_hari)