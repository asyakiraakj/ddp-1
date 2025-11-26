import math

num_of_kerucut = int(input("Banyaknya kerucut: "))
radius = float(input("Jari-jari kerucut: ")) # isi variabel adalah alamat (reference), BUKAN objek
height = float(input("Tinggi kerucut: ")) # by deafult, tipe data input adalah string
total_vol = 1/3 * math.pi * (radius ** 2) * height * num_of_kerucut

# cetak menggunakan f-string
print(f"Total volume {num_of_kerucut} kerucut adalah {total_vol}")

#-----------------------------------#
#Argumen: inputnya fungsi 
# Jenis Potongan Program
# 1. Statement : tdk bisa dievluasi, mengubah state, isi variable di memory
    # - assigment: 
    # - print: muncul sesuatu di layar (hasil cetak/print)
# 2. Expression: bisa DIEVALUASI menjadi sebuah nilai/objek
#-----------------------------------#

# CASE APEL
# num_apel = int(input("Jumlah Apel: "))
# muatan_mobil = int(input("Muatan mobil: "))

# Simultaneous Assigment: var_1, var_2 = isi var 1, isi var 2
num_apel, muatan_mobil = int(input("Jumlah Apel: ")), int(input("Muatan mobil: "))

num_mobil = num_apel // muatan_mobil
sisa_apel = num_apel % muatan_mobil

print(f"Jumlah mobil yang dibutuhkan: {num_mobil} \nSisa apel: {sisa_apel}")

# Swap Variable
# the traditional way:
a = 5
b = 8

temp = a # membuat variabel baru yang memiliki address ke [5]
a = b # a sudah tidak berisi alaamat ke objek 5, namun menuju ke alamat objek 8
b = temp # b tidak merujuk ke alamat objek 8 namun menuju objek 5, 

# phythonic way (python only)
x = 5
y = 8

x, y = y, x

# DUA JENIS OBJECT

# 1. Object yang IMMUTABLE
# int, float, str, ...
# sekali tecipta, tidak bisa diubah

# 2. Object yang MUTABLE (bisa dimutasi, dr kata mutate)
# bisa diubah
# ex: list

# INTEGER INTERNING
# -> Interning: menyimpan objek dari awal sampe akhir, 
#               selalu hidup di memori, 
#               walapun tidak ada variabel yang merujuk ke dia, 
#               jadi kalo mau dipake tinggal merujuk ke dia lagi
# -> di python: menyimpan angka (-5) — 256


total_detik = 15467
jam = total_detik // 3600
menit = (total_detik % 3600) // 60
detik = total_detik % 60

print(f"{jam} jam {menit} menit {detik} detik")

