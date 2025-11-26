import random as r
import time

# DEFAULT SETTINGS FOR REPRODUCIBILITY
# MOHON JANGAN DIUBAH HINGGA BATAS CODE
# =============================================================================
r.seed(42)

all_fish = {
    "common": {"Sunfish", "Catfish", "Bass", "Bream", "Sardine"},
    "rare": {"Trout", "Sturgeon", "Carp", "Flounder", "Eel", "Red Snapper", "Pike"},
    "epic": {"Tuna", "Chub", "Dorado", "Albacore", "Bullhead", "Gurame"},
    "legendary": {"Angler", "Crimsonfish", "Glacierfish", "Radioactive carp"},
}

fish_habitat = {
    "danau": {
        "Sunfish",
        "Pike",
        "Catfish",
        "Bream",
        "Bass",
        "Gurame",
        "Trout",
        "Sturgeon",
        "Carp",
        "Eel",
        "Radioactive carp",
        "Glacierfish",
    },
    "laut": {
        "Sardine",
        "Red Snapper",
        "Flounder",
        "Tuna",
        "Dorado",
        "Albacore",
        "Bullhead",
        "Angler",
        "Crimsonfish",
        "Glacierfish",
        "Radioactive carp",
        "Eel",
        "Carp",
    },
}

# Fungsi untuk mencetak ASCII art
# =============================================================================

def cetak_ascii_menu():
    print(r'''
  _____           _ _            _ _            
 |  __ \         (_) |          | | |           
 | |__) |_ _  ___ _| |_   ____ _| | | ___ _   _ 
 |  ___/ _` |/ __| | \ \ / / _` | | |/ _ \ | | |
 | |  | (_| | (__| | |\ V / (_| | | |  __/ |_| |
 |_|   \__,_|\___|_|_| \_/ \__,_|_|_|\___|\__, |
                                           __/ |
                                          |___/ ''')
    print("Selamat datanmg di PacilValley!")


# ascii art from: 
# https://www.asciiart.eu/animals/fish
# https://ascii.co.uk/art/fishing

def cetak_ascii_mancing():
    print(r"""
      /`-.
    /    `-.
  O/        `-.
  |            `-.
  /\              `-.
  \_\_               `-.
########~~~~~~~~~~~~~~~~`@(((<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

def cetak_ascii_ikan_tertangkap():
    print(r"""
                         ////\\\
                        /////\\\\
                       //__   __\\
                      -| (o \ o) |-
                     |d|   c_\   |b|
                      -\((\___/))/-                       ___
                        \ \___/ /                      ||////
                         \_____/                       | uuu
                         |     |                      /\ _/
                         /\ ) /\                     /  V |
                 _______/\ \ / /\_______            /  /  |
                /         \/V\/         \          /\ /  /V\
               /           |o|           \        /\ V  |  o\
              /            | |            \      /  \/\ //###|
             /             |o|             \    /   /o/ |####|>
            /              | |              \  /   / / <|####|>
           /               |o|   _____       \/    \/    \##/
          /                | |   |   |             /     |##|
         /       /         |o|   |   |  \         /     /_/\_\
        /       /|         | |   |___|  |\       /
       /       / |         |o|          | \_____/

    """)

def cetak_ascii_pindah_lokasi():
    print(r"""
                     v  ~.      v
            v           /|
                       / |          v
                v     /__|__
                   \--------/
~~~~~~~~~~~~~~~~~~~~`~~~~~~'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Berpindah lokasi....""")

def cetak_ascii_aquarium():
    print(r"""
    ⢰⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⣶⡆    
     ⣿                  ⣿     
   ⢀⡾⠁⣀⣠⣤⣤⣤⣤⣤⣀⡀         ⠈⢷⡀   
  ⢠⡟ ⣈⡉⠉    ⠈⠉⠛⠻⠶⣦⣤⣤⣤⣴⡶⠶⠶ ⢻⡄  
  ⣿⠁⣸⣿⠁             ⣴⣶⣦   ⠈⣿  
 ⢸⡏ ⣿⠇              ⠈⠛⠋    ⢹⡇ 
 ⢸⡇ ⣿                 ⢠⣤⡀  ⢸⡇ 
 ⢸⣇ ⣿   ⠠⣤⣀  ⣀⣤⣴⣾⣿⣿⠷⣦⣄⠈⠛⠁  ⣸⡇ 
  ⢿⡄⢹⡇   ⣿⡿⠗⠿⢿⣿⣿⣿⣿⣿⣷⣿⣿⠇   ⢠⡿  
  ⠈⢷⡀⠹⡀ ⠈⠁    ⠈⠙⠛⠿⠿⠟⠋⠁   ⢀⡾⠃  
   ⠈⢷⣄                  ⣠⡾⠁   
     ⠙⢷⣄⡀            ⢀⣠⡾⠋     
       ⠈⠙⠳⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠞⠋⠁     
""")

def cetak_progress_bar():
    def print_progress_bar(progress, end):
        print("[{0}{1}] {2}%".format("█" * progress, "-" * (end - progress), progress), end="\r")
        if progress == end:
            print()

    for i in range(0,101):
        print_progress_bar(i,100)
        time.sleep(0.01)

# BATAS AKHIR DEFAULT SETTINGS
# =============================================================================


# Seluruh code template di bawah hanya sebagai panduan, boleh diubah sesuai kebutuhan

caught_fish = set()


def roll_rarity():
    # TODO: Lengkapi fungsi roll_rarity
    # Digunakan untuk menentukan tingkat kelangkaan (rarity) ikan yang akan didapat setiap kali melakukan aksi mancing().
    random_int = r.random()

    rarity = ""
    if random_int < 0.60:
        return "common"
    elif random_int < 0.85:
        return "rare"
    elif random_int < 0.95:
        return "epic"
    else:
        return "legendary"
    pass


def mancing(lokasi):
    cetak_ascii_mancing()
    cetak_progress_bar()
    cetak_ascii_ikan_tertangkap()
    # TODO: Lengkapi fungsi mancing
    rarity = roll_rarity()

    fish_in_habitat = fish_habitat[lokasi]
    fish_rarity = all_fish[rarity]
    fish_in_habitat_rarity = fish_in_habitat.intersection(fish_rarity)

    fish = r.choice(sorted(fish_in_habitat_rarity))
    print(f"Ikan {fish} tertangkap! Rarity = {rarity}")

    if fish in caught_fish:
        print("Kamu sudah pernah menangkap ikan ini sebelumnya")
    else:
        caught_fish.add(fish)
        print("Ikan baru! Ditambahkan ke koleksi")
    pass


def aquarium():
    cetak_ascii_aquarium()
    # TODO: Gunakan operasi set pada set dibawah ini agar berfungsi sesuai tujuan

    semua_ikan = fish_habitat["danau"].union(fish_habitat["laut"])
    belum_ditangkap = semua_ikan.difference(caught_fish)
    ikan_danau_saja = fish_habitat["danau"]
    ikan_rare_danau_belum = ikan_danau_saja.intersection(all_fish["rare"]) - caught_fish

    print("\n=== LAPORAN IKAN ===")
    print("Ikan yang sudah ditangkap:\n", "\n-".join(caught_fish) if caught_fish else "Belum ada ikan yang kamu tangkap", sep="-")
    print()
    print("Ikan yang belum ditangkap:\n", "\n-".join(belum_ditangkap), sep="-")
    print()
    print(
        "Ikan rare yang hanya hidup di danau dan belum ditangkap:\n",
        "\n-".join(ikan_rare_danau_belum), sep="-"
    )


def ubah_lokasi():
    cetak_ascii_pindah_lokasi()
    print("\n=== Ubah Lokasi ===")
    # TODO: Implementasikan fungsi ubah_lokasi
    print("1. Laut")
    print("2. Danau")
    menu = input("Pilih menu (1-2): ")
    if menu == 1:
        lokasi = "danau"
        print("Lokasi saat ini: danau")
    elif menu == 2:
        lokasi = "laut"
        print("Lokasi saat ini: laut")
    else:
        print("Input tidak valid, pilih antara (1-2)")



def tampilkan_menu():
    print("\n=== MENU MANCING ===")
    print("1. Mancing")
    print("2. Lihat Aquarium")
    print("3. Pindah lokasi pemancingan")
    print("4. Keluar")


def main():
    lokasi = "danau"
    # TODO: Lengkapi fungsi main menu
    while True:
        tampilkan_menu()
        choice = int(input("Pilih menu: "))
        if choice == 1:
            mancing(lokasi)
            continue
        elif choice == 2:
            aquarium()
            continue
        elif choice == 3:
            ubah_lokasi()
            continue
        elif choice == 4:
            break
        else:
            print("Input tidak valid! pilih antara (1-4)")



if __name__ == "__main__":
    main()