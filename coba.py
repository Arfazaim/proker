import turtle

# Inisialisasi pena dan layar
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(0, -200)
pen.pendown()

# Buat mawar pertama
for i in range(360):
    pen.forward(2)
    pen.right(1)

# Buat mawar kedua
pen.penup()
pen.goto(0, -150)
pen.pendown()
pen.color("red")
pen.left(40)

for i in range(360):
    pen.forward(3)
    pen.right(1)

# Tampilkan hasilnya
turtle.done()