print("="*5 + "Pacil Edu" + "="*5)

print("1. Buat Laporan\n2. Tambah Data\n3. Keluar\n")

choice = input("Pilih [1-3]: ")
file_name = input("Masukkan nama file: ")

with open(file_name, "r") as file_in,\
     open("laporan.txt", "w") as file_out:
    lines = file_in.readlines()

    try:
        if choice == "1":
            for line in lines[1:]:
                property = line.split(',')
                name = property[0]
                tugas = int(property[1])
                UTS = int(property[2])
                UAS = int(property[3].strip())
                nilai_akhir = round((tugas*0.30) + (UTS*0.35) + (UAS*0.35))

                if nilai_akhir >= 85:
                    grade = "A"
                elif nilai_akhir >= 70:
                    grade = "B"
                elif nilai_akhir >= 55:
                    grade = "C"
                elif nilai_akhir >= 40:
                    grade = "D"
                else:
                    grade = "E"

                file_out.write(f"{name} mendapatkan nilai akhir sebesar {nilai_akhir} dan memperoleh grade {grade}\n")

        elif choice == "2":
            with open("nilai.csv", 'a+') as file_in:
                new_name = input("Masukkan nama mahasiswa: ")
                new_tugas = int(input("Masukkan nilai tugas: "))
                new_UTS = int(input("Masukkan nilai uts: "))
                new_UAS = int(input("Masukkan nilai uas: "))

                new_line = (f"{new_name},{new_tugas},{new_UTS},{new_UAS}")
                
                if new_tugas <= 100 and new_UTS <= 100 and new_UAS <= 100:
                    file_in.write(new_line)
                else:
                    ("Nilai di luar jangkauan")                            

        else:
            print("")
        
    except FileNotFoundError:
        print("File tidak ada di direktori")