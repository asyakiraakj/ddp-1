# #Soal 1
# m = int(input("m = "))
# n = int(input("n = "))

# if m == n:
#     print(2*(m+n))
# else:
#     print(m + n)
# #Soal 1 (alternative solution)
# m = int(input("m = "))
# n = int(input("n = "))

# jumlah = m + n

# if m == n:
#     print(2*(m+n))


# #Soal 2
# n = int(input("n = "))

# for i in range (1, n):
#     if n % i == 0:
#         print(i)

# # Soal 3
# velocity = int(input("Kecepatan = "))
# is_birthday = input("Apakah anda ulang tahun? (ya/tidak) ")

# if is_birthday == "ya":
#     velocity -= 5

# if is_birthday == "tidak":
#     if velocity > 80:
#         print("tilang besar")
#     elif velocity > 60:
#         print("tilang kecil")
#     else:
#         print("tidak kena tilang")
    

# # Soal 4
# str = input("sebuah string = ")

# count_char = 0
# for char in str:
#     if char == "a":
#         count_char += 1
# print(f"ada {count_char} buah karakter a")

# # Soal 5
# n = int(input("n = "))

# for i in range (1, n+1):
#     space = n - i
#     stars = i
#     print(" "*space + "*"*stars)
# for j in range (n, 0, -1):
#     space = n - j
#     stars = j
#     print(" "*space + "*"*stars)

# # Soal 6
# str = input("sebuah string = ")

# hasil = ""
# for char in str:
#     if char == "":
#         hasil = hasil + str



# Soal 7
n = int(input("n = "))
angka = 0

for i in range (9, 0):
    m = n % 10
    angka += + 10
    n // 10
print(angka)



# Soal 8
# n = int(input("n = "))

# binary = 0
# for i in range(n):
#     b = n % 2
#     print(b)