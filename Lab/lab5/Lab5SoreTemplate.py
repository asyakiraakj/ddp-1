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
    pass


# Fungsi untuk memastikan input merupakan INTEGER dalam rentang tertentu (default adalah 1 sampai tak terhingga, yaitu input positif)
def validasi_input_integer(nilai, min_val=1, max_val=float('inf')):
    # TODO: return True jika input valid, False jika tidak valid
    pass

# Fungsi untuk menampilkan isi keranjang
def tampilkan_keranjang():
    # TODO: tampilkan semua barang di keranjang beserta total harganya
    pass


# Fungsi untuk membeli barang dan menambahkannya ke keranjang
def beli_barang():
    # TODO: tampilkan daftar barang dan minta pengguna memilih barang
    # hint: gunakan validasi_input_integer agar input valid
    pass


# Fungsi untuk mengosongkan keranjang
def kosongkan_keranjang():
    # TODO: tampilkan isi keranjang terlebih dahulu, lalu kosongkan
    pass


# Fungsi untuk checkout keranjang
def checkout_keranjang():
    # TODO: tampilkan isi keranjang, lalu checkout dengan menampilkan pesan checkout, kemudian kosongkan keranjang
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

jumlah_barang = int(input("Masukkan jumlah barang yang tersedia: "))
# TODO: isi list nama_barang dan harga_barang dengan input integer positif bebas dari pengguna
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
