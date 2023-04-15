lados = 8
angulo = 360 / lados

from turtle import *

speed(11)
shape("turtle")
pensize(6)
color("red")

for count in range(36):
    forward(100)
    left(angulo)


done()
