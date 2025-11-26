N_row = int(input("Jumlah baris: "))
C_column = int(input("Jumlah kolom: "))
data_per_page = N_row * C_column #menghitung jumlah entri per halaman

input_X = int(input("Masukkan entri: "))

halaman =  ((input_X - 1) // data_per_page) + 1
row = (((input_X - 1) % data_per_page) // C_column) + 1
column = ((input_X - 1) % C_column) + 1

print(f"halaman {halaman}, baris {row}, kolom {column}")


