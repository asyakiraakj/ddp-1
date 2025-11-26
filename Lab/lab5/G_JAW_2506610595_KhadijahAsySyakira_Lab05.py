# ======================= GLOBAL LIST UNTUK IMPLEMENTASI DAFTAR BARANG DAN KERANJANG ==========================

# Dua list sejajar untuk menyimpan nama dan harga barang
nama_barang = []
harga_barang = []

# Dua list untuk menyimpan isi keranjang
nama_keranjang = []
harga_keranjang = []


# ======================= FUNGSI-FUNGSI PEMBANTU ==========================

# Fungsi untuk memformat harga dalam format rupiah
def format_rupiah(angka):
    # TODO: kembalikan string dalam format "RpX.XXX,-"
    digits = ""
    while angka != 0:
        last_three = angka % 1000
        digits = digits + "." + str(last_three)
        angka // 1000
        if len(str(angka)) == 1 or len(str(angka)) == 2 or len(str(angka)) == 3:
            digits = angka + "." + digits
    angka_rupiah = "Rp" + digits + ",-"

    return angka_rupiah

    pass


# Fungsi untuk memastikan input merupakan INTEGER dalam rentang tertentu (default adalah 1 sampai tak terhingga, yaitu input positif)
def validasi_input_integer(nilai, min_val=1, max_val=float('inf')):
    # TODO: return True jika input valid, False jika tidak valid
    # harga barang
    if nilai >= min_val and nilai <= max_val:
        return True
    else:
        return False

    pass

# Fungsi untuk menampilkan isi keranjang
def tampilkan_keranjang():
    # TODO: tampilkan semua barang di keranjang beserta total harganya
    print("="*33 + "\n" + "Isi Keranjang" + "-"*33 + "\n")
    total = 0
    for i in range (len(nama_keranjang)):
        print(f"{nama_keranjang[i]} | {format_rupiah(harga_keranjang[i])}")
        total += harga_keranjang[i]
    print("-"*33)
    print(f"Total: {format_rupiah(total)}")
    print("="*33)
    pass


# Fungsi untuk membeli barang dan menambahkannya ke keranjang
def beli_barang():
    # TODO: tampilkan daftar barang dan minta pengguna memilih barang
    # hint: gunakan validasi_input_integer agar input valid

    print("Daftar Barang:")
    for i in range (jumlah_barang):
        print(f"{i+1}. {nama_barang[i]} ({format_rupiah(harga_barang[i])})")

    choose_item = int(input("Pilih Barang: "))

    validasi = validasi_input_integer(choose_item, min_val=1, max_val=jumlah_barang)
    while validasi == False:
        choose_item = input("Input tidak valid, pilih barang: ")

    print(f"{nama_barang[choose_item-1]} berhasil ditambahkan ke keranjang")
    nama_keranjang += nama_barang[choose_item-1]
    pass


# Fungsi untuk mengosongkan keranjang
def kosongkan_keranjang():
    # TODO: tampilkan isi keranjang terlebih dahulu, lalu kosongkan
    print(tampilkan_keranjang)
    nama_keranjang = []
    harga_keranjang = []
    print("Keranjang berhasil dikosongkan")
    pass


# Fungsi untuk checkout keranjang
def checkout_keranjang():
    # TODO: tampilkan isi keranjang, lalu checkout dengan menampilkan pesan checkout, kemudian kosongkan keranjang
    print(tampilkan_keranjang)
    total = sum(harga_keranjang)
    print(f"Keranjang berhasil di-checkout dengan pembelian sejumlah {total}")

    kosongkan_keranjang()
    pass


# ======================= MAIN PROGRAM ==========================
print("=============================================================")
print(""" 
 888888ba                    dP                         dP                                   dP       
 88    `8b                   88                         88                                   88       
a88aaaa8P' dP    dP 88d888b. 88d888b. .d8888b. 88d888b. 88        .d8888b. 88d888b. .d8888b. 88  .dP  
 88   `8b. 88    88 88'  `88 88'  `88 88'  `88 88'  `88 88        88'  `88 88'  `88 88'  `88 88888"   
 88    .88 88.  .88 88       88    88 88.  .88 88    88 88        88.  .88 88.  .88 88.  .88 88  `8b. 
 88888888P `88888P' dP       dP    dP `88888P8 dP    dP 88888888P `88888P8 88Y888P' `88888P8 dP   `YP 
                                                                           88                         
                                                                           dP                         """)
print("=============================================================")
print("=============== Selamat datang di BurhanLapak! ==============")
print("=============================================================\n")

jumlah_barang = int(input("Masukkan jumlah barang yang ingin dijual: "))
while validasi_input_integer(jumlah_barang, min_val=1, max_val=float("inf")) == False:
    jumlah_barang = ("Input tidak valid! Masukkan jumlah barang sebagai angka positif")

# TODO: isi list nama_barang dan harga_barang dengan input integer positif bebas dari pengguna
for i in range (1, (jumlah_barang + 1)):
    input_nama_barang = input(f"Nama barang ke-{i}: ")
    nama_barang += input_nama_barang

    input_harga_barang = int(input(f"Harga barang ke-{i}: "))
    if validasi_input_integer(input_harga_barang, min_val=1, max_val=float('inf')) == True:
        harga_barang += input_harga_barang
    else:
       while validasi_input_integer(input_harga_barang, min_val=1, max_val=float('inf')) == False:
            harga_barang = input("Harga dompet tidak valid! Masukkan angka positif: ")

    print(f"Berhasil menambahkan {input_nama_barang} seharga {format_rupiah(input_harga_barang)}")
# TODO: gunakan fungsi format_rupiah untuk menampilkan harga dalam format rupiah
# TODO: gunakan fungsi validasi_input_integer untuk validasi input integer dan harga positif

while True:
    print("\nMenu:")
    print("1. Beli Barang")
    print("2. Tampilkan Keranjang")
    print("3. Kosongkan Keranjang")
    print("4. Checkout Keranjang")
    print("5. Keluar")

    
    opsi = input("Pilih opsi (1-5): ")
    while (validasi_input_integer(opsi, min_val=1, max_val=5)) == False:
        opsi = input("Opsi tidak valid! Pilih opsi (1-5): ")
    # TODO: validasi input opsi agar hanya menerima angka 1-5
    # hint: gunakan fungsi validasi_input_integer

    if opsi == 1:
        beli_barang()
    elif opsi == 2:
        tampilkan_keranjang()
    elif opsi == 3:
        kosongkan_keranjang()
    elif opsi == 4:
        checkout_keranjang()
    elif opsi == 5:
        print("\nTerima Kasih Telah Menggunakan BurhanLapak!")
        break
