import turtle

# Función para dibujar la mano de Papá Noel
def draw_hand():
    turtle.color("white")
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10, -180)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.circle(10, -180)
    turtle.end_fill()
    turtle.penup()

# Configuración inicial
turtle.speed(2)
turtle.bgcolor("white")
turtle.color("red")

# Cuerpo de Papá Noel
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# Cabeza de Papá Noel
turtle.color("white")
turtle.penup()
turtle.goto(0, 100)
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

# Ojos de Papá Noel
turtle.color("black")
turtle.penup()
turtle.goto(-20, 120)
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(20, 120)
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

# Nariz de Papá Noel
turtle.penup()
turtle.goto(0, 90)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

# Boca de Papá Noel
turtle.penup()
turtle.goto(-15, 60)
turtle.pendown()
turtle.right(90)
turtle.circle(15, 180)

# Sombrero de Papá Noel
turtle.penup()
turtle.goto(-40, 160)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.forward(80)
turtle.left(120)
turtle.forward(80)
turtle.left(120)
turtle.forward(80)
turtle.end_fill()

# Movimiento de la mano
turtle.penup()
turtle.goto(-10, 80)
turtle.setheading(90)

for _ in range(3):
    draw_hand()
    turtle.right(30)

# Mensaje de saludo
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.color("black")
turtle.write("¡Ho Ho Ho! Feliz Navidad", align="center", font=("Arial", 16, "normal"))

# Ocultar la tortuga al finalizar
turtle.hideturtle()

# Mantener la ventana abierta
turtle.mainloop()


# Ocultar la tortuga al finalizar
turtle.hideturtle()

# Mantener la ventana abierta
turtle.mainloop()
