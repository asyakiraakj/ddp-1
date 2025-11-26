# # BINARY
# # buatlah program ang menerima sebuah bilangan bulat positif

 
# num = int(input("angka = "))

# # cara 1
# binary = ""
# if num >= 1:
#     while (num // 2) != 0:
#         binary = str(num % 2) + binary
#         num // 2 
# print(binary)

# # cara 2
# if num >= 1:
#     while (num // 2) != 0:
#         binary += str(num % 2)
#         num // 2 
# print(binary[::-1])

# # cara 3
# ans = ""
# if num >= 1:
#     while (num // 2) != 0:
#         if num % 2:
#             ans = "1" + ans
#         else:
#             ans = "0" + ans # 4 baris if ini bisa diganti jadi: ans str(num % 2) + ans
# print(ans)

str_input = input("string = ")

same_char = 0
for char in str_input:
    if (char in str_input):
        same_char += 1


if same_char > 1:
    print("karakter tidak unik")
else:
    print("karakter unik")