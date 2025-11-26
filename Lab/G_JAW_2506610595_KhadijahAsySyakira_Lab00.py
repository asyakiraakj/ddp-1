import turtle


screen = turtle.Screen()
screen.title("Piramida Dasar")
screen.setup(width=600, height=500)
screen.bgcolor("skyblue")

pena = turtle.Turtle()
pena.speed(3)


LEBAR_DASAR = 240
TINGGI_LAPISAN = 30
FAKTOR_PENGECIL = 60 # keruncingan piramida

# --- 3. Logika Menggambar ---
# Hitung posisi awal agar piramida di tengah
y_awal = -(4 * TINGGI_LAPISAN) / 2
# biar di tengah, pertama hitung tinggi totalnya dulu:
# tinggi per lapis dikali jumlah lapisan (4)
# kemudian dibagi 2 dan diberi tanda - agar koordinat bergerak ke bawah

# Lapisan 0 (lapisan tambahan keempat)
lebar_0 = LEBAR_DASAR
x_0 = -lebar_0 / 2
y_0 = y_awal
pena.penup()
pena.goto(x_0, y_0)
pena.pendown()
pena.color("red")
pena.begin_fill()
pena.forward(lebar_0)
pena.left(90)
pena.forward(TINGGI_LAPISAN)
pena.left(90)
pena.forward(lebar_0)
pena.left(90)
pena.forward(TINGGI_LAPISAN)
pena.left(90)
pena.end_fill()

# Lapisan 1
lebar_1 = lebar_0 - FAKTOR_PENGECIL
x_1 = -lebar_1 / 2
y_1 = y_awal + TINGGI_LAPISAN # lapisan 1 (lapisan kedua) = lapisan 0 (lapisan pertama) + tinggi lapisan
pena.penup()
pena.goto(x_1, y_1)
pena.pendown()
pena.color("purple")
pena.begin_fill()
pena.forward(lebar_1)
pena.left(90)
pena.forward(TINGGI_LAPISAN)
pena.left(90)
pena.forward(lebar_1)
pena.left(90)
pena.forward(TINGGI_LAPISAN)
pena.left(90)
pena.end_fill()

# Lapisan 2 (tengah)
lebar_2 = LEBAR_DASAR - ( 2 * FAKTOR_PENGECIL )
x_2 = -lebar_2 / 2
y_2 = y_awal + (2 * TINGGI_LAPISAN) # lapisan 2 (lapisan ketiga) = lapisan 0 (lapisan pertama) + (2 * tinggi lapisan)
pena.penup()
pena.goto(x_2, y_2)
pena.pendown()
pena.color("green")
pena.begin_fill()
pena.forward(lebar_2)
pena.left(90)
pena.forward(TINGGI_LAPISAN)
pena.left(90)
pena.forward(lebar_2)
pena.left(90)
pena.forward(TINGGI_LAPISAN)
pena.left(90)
pena.end_fill()

# lapisan 3 (puncak)
lebar_3 = LEBAR_DASAR - (3 * FAKTOR_PENGECIL)
x_3 = -lebar_3 / 2
y_3 = y_awal + (3 * TINGGI_LAPISAN) # lapisan 3 (lapisan keempat) = lapisan 0 (lapisan pertama) + (3 * tinggi lapisan)
pena.penup()
pena.goto(x_3, y_3)
pena.pendown()
pena.color("yellow")
pena.begin_fill()
pena.forward(lebar_3)
pena.left(90)
pena.forward(TINGGI_LAPISAN)
pena.left(90)
pena.forward(lebar_3)
pena.left(90)
pena.forward(TINGGI_LAPISAN)
pena.left(90)
pena.end_fill()

pena.hideturtle()
screen.exitonclick()