# nilai = int(input("Masukkan nilai: "))

# # ver 2
# if nilai >= 90:
#     print("A") 
# elif 80 <= nilai < 90:
#     print("B") 
# elif 70 <= nilai < 80:
#     print("C") 
# elif 60 <= nilai < 70:
#     print("D") 
# else:
#     print("E")

# # ver 3
# if nilai < 60:
#     print("E") 
# elif nilai < 70:
#     print("D") 
# elif nilai < 80:
#     print("C") 
# elif nilai < 90:
#     print("B") 
# else:
#     print("A")
# # 👑

# # ver 4
# if nilai >= 90:
#     print("A") 
# elif nilai >= 80:
#     print("B") 
# elif nilai >= 70:
#     print("C") 
# elif nilai >= 60:
#     print("D") 
# else:
#     print("E")
# # 👑

# Problem 3
# Ver 1
i = int(input("Masukkan angka: "))
j = int(input("Masukkan angka: "))
k = int(input("Masukkan angka: "))

if i >= j >= k: # if i >= j and j >= k, bukan i > j dan i > k
    print(i)
elif j >= k >= i:
    print(j)
else:
    print(k)
# TIDAK TEPAT*: 

# Ver 2
i = int(input("Masukkan angka: "))
j = int(input("Masukkan angka: "))
k = int(input("Masukkan angka: "))

if i >= j:
    if i >= k:
        print(i)
    else:
        print(k)
else:
    if i >= k:
        print(j)
    else:
        print(k)