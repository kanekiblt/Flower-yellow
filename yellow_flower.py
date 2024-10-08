from turtle import *
import colorsys
import math

speed(0)
bgcolor("black")

h = 0

for i in range(16):
    for j in range(18):
        c= colorsys.hsv_to_rgb(0.125 , 1, 1)
        color(c)
        h+=0.005
        rt(90)
        circle(150-j*6, 90)
        lt(90)
        circle(150-j*6, 90)
        rt(180)
    circle(40, 24)

color("black") 
shape("turtle")
fillcolor("brown")
phi = 137.508 * (math.pi/ 180.0)

for i in range (200):
    r = 4 * math.sqrt(i)
    theta = i*phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()

penup()
goto(0, 0)
color("purple")
write("Feliz dia de la amistad", align="center", font=("Arial", 20, "normal"))    


done()
