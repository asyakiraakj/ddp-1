# #Case: Akronim
# masukan = input("Input: ")

# words = masukan.split() # kalimat yang per katanya udah dipisah, *list (tipe data: list)* kata kata dari sebuah kalimat, bukan single kata

# akronim = "" #jika disuruh membuat/modifikasi sesuatu, build up dari sesuatu yang kosong
# for char in words:
#     akronim += char[0].capitalize()

# print(f"Output: {akronim}")

# Case: reverse string
# rule: no slicing. hint: use indexing

str_input = input("Input string: ")
str_length = len(str_input)

str_reversed = ""
for char in range(str_length, 0, -1):
    str_reversed += str(char)
print(str_reversed)

# solution:
str_input = input("Input string: ")
str_length = len(str_input)

str_reversed = ""
for char in str_input:
    str_reversed = char + str_reversed
print(str_reversed)