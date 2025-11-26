import random as r

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
        "Bass",
        "Bream",
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
    pass


def mancing(lokasi):
    cetak_ascii_mancing()
    cetak_progress_bar()
    cetak_ascii_ikan_tertangkap()
    # TODO: Lengkapi fungsi mancing
    # fish = random.[TODO](sorted( [TODO: set()] ))
    

    pass


def aquarium():
    cetak_ascii_aquarium()
    # TODO: Gunakan operasi set pada set dibawah ini agar berfungsi sesuai tujuan

    #semua_ikan = 
    #belum_ditangkap = 
    #ikan_danau_saja = 
    #ikan_rare_danau_belum = 

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


def tampilkan_menu():
    print("\n=== MENU MANCING ===")
    print("1. Mancing")
    print("2. Lihat Aquarium")
    print("3. Pindah lokasi pemancingan")
    print("4. Keluar")


def main():
    lokasi = "danau"
    # TODO: Lengkapi fungsi main menu


if __name__ == "__main__":
    main()