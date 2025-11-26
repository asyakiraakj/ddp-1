# total_detik = 15467
# jam = total_detik // 3600
# menit = (total_detik % 3600) // 60
# detik = total_detik % 60

# print(f"{jam} jam {menit} menit {detik} detik")

# total_detik = 15467
# jam = total_detik // 3600
# menit = (total_detik % 3600) // 60
# detik = total_detik % 60

# print(f"{jam} jam {menit} menit {detik} detik")


bilangan = int(input("Masukkan angka: "))
ribuan = bilangan // 1000 # = 1
ratusan = (bilangan - ribuan) // 100
puluhan = (bilangan - (ribuan + ratusan)) // 10
satuan = puluhan % 10

jumlah = ribuan + ratusan + puluhan + satuan

print(f"{ribuan} + {ratusan} + {puluhan} + {satuan} = {jumlah}")

