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
y_awal = -(3 * TINGGI_LAPISAN) / 2

# --- Menggambar LAPISAN 1 (Paling Bawah) ---
lebar_1 = LEBAR_DASAR
x_1 = -lebar_1 / 2
y_1 = y_awal
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
lebar_2 = LEBAR_DASAR - FAKTOR_PENGECIL
x_2 = -lebar_2 / 2
y_2 = y_awal + TINGGI_LAPISAN
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
lebar_3 = LEBAR_DASAR - (2 * FAKTOR_PENGECIL)
x_3 = -lebar_3 / 2
y_3 = y_awal + (2 * TINGGI_LAPISAN)
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