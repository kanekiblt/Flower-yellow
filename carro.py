import turtle

screen = turtle.Screen()
screen.bgcolor("black") 

t = turtle.Turtle()
t.speed(3)
t.color("white")

def draw_rectangle(color, width, height):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_circle(color, radius):
    t.begin_fill()
    t.fillcolor(color)
    t.circle(radius)
    t.end_fill()

t.penup()
t.goto(-100, 0)
t.pendown()
draw_rectangle("blue", 200, 50)

t.penup()
t.goto(-70, 50)
t.pendown()
draw_rectangle("lightblue", 140, 40)

t.penup()
t.goto(-60, 55)
t.pendown()
draw_rectangle("white", 30, 30)

t.penup()
t.goto(0, 55)
t.pendown()
draw_rectangle("white", 30, 30)

t.penup()
t.goto(-75, -20)
t.pendown()
draw_circle("black", 20)

t.penup()
t.goto(50, -20)
t.pendown()
draw_circle("black", 20)

t.hideturtle()
turtle.done()
