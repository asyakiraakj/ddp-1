import turtle as t
# radius = min(100, 200, 300, 50) #50
# t.begin_fill()
# t.fillcolor("orange")
# t.circle(radius, 45)
# t.left(90)
# t.forward(radius)
# t.goto(0,0)
# t.end_fill()
# t.exitonclick()

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

# Menghitung jumlah bahan untuk brownies
tepung_brownies_used = tepung // tepung_brownies
coklat_brownies_used = coklat // coklat_brownies
mentega_brownies_used = mentega // mentega_brownies
gula_brownies_used = gula // gula_brownies
telur_brownies_used = telur // telur_brownies

# Menghitung jumlah bahan untuk roti coklat
brownies = min(tepung_brownies_used, coklat_brownies_used, mentega_brownies_used, gula_brownies_used, telur_brownies_used)
tepung_roti_coklat_used = (tepung - (tepung_brownies*brownies)) // tepung_roti_coklat
coklat_roti_coklat_used = (coklat - (coklat_brownies*brownies)) // coklat_roti_coklat
susu_roti_coklat_used = susu // susu_roti_coklat
mentega_roti_coklat_used = (mentega - (mentega_brownies*brownies)) // mentega_roti_coklat
gula_roti_coklat_used = (gula - (gula_brownies*brownies)) // gula_roti_coklat
telur_roti_coklat_used = (telur - (telur_brownies*brownies)) // telur_roti_coklat
print(tepung_roti_coklat_used, coklat_roti_coklat_used, mentega_roti_coklat_used, gula_roti_coklat_used, telur_roti_coklat_used)

# Brownies hari ini
brownies = min(tepung_brownies_used, coklat_brownies_used, mentega_brownies_used, gula_brownies_used, telur_brownies_used)
roti_coklat = min(tepung_roti_coklat_used, coklat_roti_coklat_used, mentega_roti_coklat_used, gula_roti_coklat_used, telur_roti_coklat_used)

if brownies >= 0 and roti_coklat >= 0:
    print(f"Produksi hari ini adalah {brownies} brownies dan {roti_coklat} roti")
else:
    ""

pendapatan_brownies = brownies*harga_brownies
pendapatan_roti_cokelat = roti_coklat*harga_roti
pendapatan_total = pendapatan_brownies + pendapatan_roti_cokelat
if pendapatan_total > 300000:
    tabung_usd = (pendapatan_total*0.4) / 16500
    sisa_uang = pendapatan_total - tabung_usd
    print(f"Pendapatan hari ini: {pendapatan_total} Rupiah")
    print(f"Uang yang ditabung dalam USD: {tabung_usd}")
else:
    print(f"Pendapatan hari ini: {pendapatan_total} Rupiah")
    print(f"Tidak ada uang yang ditabung dalam USD.")

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
total_produksi = brownies + roti_coklat
if pendapatan_brownies > pendapatan_roti_cokelat:
    radius = 50
    t.begin_fill()
    t.fillcolor(warna_brownies)
    t.circle(radius, 360)
    t.left(90)
    t.forward(radius)
    t.goto(0,0)
    t.end_fill()
    if pendapatan_roti_cokelat !=0:
        t.begin_fill()
        t.fillcolor(warna_roti)
        t.circle(radius, (pendapatan_roti_cokelat/total_produksi)*360)
        t.left(90)
        t.forward(radius)
        t.goto(0,0)
        t.end_fill()
        t.exitonclick()
    else:
        t.exitonclick
elif (pendapatan_brownies == 0) and (pendapatan_roti_cokelat == 0):
    t.exitonclick
else:
    radius = 50
    t.begin_fill()
    t.fillcolor(warna_roti)
    t.circle(radius, 360)
    t.left(90)
    t.forward(radius)
    t.goto(0,0)
    t.end_fill()
    t.exitonclick()
    if pendapatan_brownies !=0:
        t.begin_fill()
        t.fillcolor(warna_brownies)
        t.circle(radius, (pendapatan_brownies/total_produksi)*360)
        t.left(90)
        t.forward(radius)
        t.goto(0,-100)
        t.end_fill()
        t.exitonclick()
    else:
        t.exitonclick