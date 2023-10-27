import turtle

# Inisialisasi layar Turtle
wn = turtle.Screen()
wn.bgcolor("white")

# Membuat objek Turtle
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("red")

# Menggambar bunga
for _ in range(36):
    flower.forward(100)
    flower.right(45)
    flower.forward(100)
    flower.right(135)
    flower.forward(100)
    flower.right(45)
    flower.forward(100)
    flower.right(170)

# Menutup jendela saat selesai
wn.exitonclick()
