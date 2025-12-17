# --- Title ---
print('''<><><><><><><><><><><><><><><><><><>
|                                  |
|         Library Perpucil         |
|                                  |
<><><><><><><><><><><><><><><><><><>
''')

# TODO: --- Pengambilan input ---
nama_peminjam = ...
npm_peminjam = ...
nama_buku = ...
tarif_per_hari = ...

# TODO: --- Pengambilan input yang perlu divalidasi ---
# TODO: Gunakan loop untuk validasi input
    # TODO: --- Pengambilan input ---
    print()
    bulan_peminjaman = ...
    tanggal_peminjaman = ...

    print()
    bulan_pengembalian = ...
    tanggal_pengembalian = ...

    # --- Validasi input ---
    # TODO: Pengecekan bulan (1-12)
    if ...:
        print("Input bulan tidak valid. Harus dalam rentang 1-12.")
        continue

    # TODO: Pengecekan tanggal (1-30)
    if ...:
        print("Input tanggal tidak valid. Harus dalam rentang 1-30.")
        continue

    # TODO: Pengecekan peminjaman sebelum pengembalian
    if ...: 
        print("Peminjaman harus dilakukan sebelum pengembalian!")
        continue

    # TODO: Dibebaskan menambahkan conditional jika merasa dibutuhkan.

    break

# TODO: --- Total hari ---
total_hari = ...

# TODO: --- Unique ID ---
unique_id = ...

# TODO: --- Success message ---
print()
print("--- Checkout Peminjaman ---")
# TODO: Lanjutkan print sesuai output yang diharapkan