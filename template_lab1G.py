import turtle as t

# ======================================================================
# JANGAN UBAH BAGIAN INI
# RESEP DAN HARGA
# ======================================================================

# RESEP UNTUK 1 ROTI COKLAT
tepung_roti_coklat = 150      # gram
coklat_roti_coklat = 40       # gram
susu_roti_coklat = 100        # ml
mentega_roti_coklat = 30      # gram
gula_roti_coklat = 50         # gram
telur_roti_coklat = 1         # butir

# RESEP UNTUK 1 BROWNIES
tepung_brownies = 100         # gram
coklat_brownies = 200         # gram
susu_brownies = 0             # ml (brownies tidak pakai susu)
mentega_brownies = 100        # gram
gula_brownies = 150           # gram
telur_brownies = 2            # butir

# HARGA JUAL
harga_brownies = 40000
harga_roti = 15000

# ======================================================================
# JANGAN UBAH BAGIAN INI
# Meminta input dari supplier
# ======================================================================
print("==== TOKO ROTI SOFITA ====")
print()
print("Silakan masukkan jumlah bahan yang tersedia hari ini:")

tepung = int(float(input("Tepung (Kg): "))*1000)
coklat = int(float(input("Coklat (Kg): "))*1000)
susu = int(float(input("Susu (liter): "))*1000)
mentega = int(float(input("mentega (Kg): "))*1000)
gula = int(float(input("Gula Pasir (Kg): "))*1000)
telur = int(input("Telur (butir): "))

# ======================================================================
# TODO: Lengkapi kode di bagian ini
# LOGIKA PRODUKSI DAN PENDAPATAN
# TIP: Anda dapat memanfaatkan fungsi min(x,y,z,...) disini untuk mencari nilai paling kecil antara x,y,z,...
# ======================================================================



# ======================================================================
# TODO: Lengkapi kode di bagian ini
# Membuat Pie Chart dengan Turtle
# Hanya menggambar jika ada produk yang terjual
# TIP: Anda dapat memanfaatkan method turtle circle(radius, extent) disini
# ======================================================================
warna_brownies = 'maroon'
warna_roti = 'steelblue'
t.penup()
t.goto(0,-100)
t.pendown()
# TODO
