nama_file = input("Nama file = ")

with open(nama_file, "r") as f:
    unique_items = set(f.read().split())
    for x in unique_items:
        print(x)