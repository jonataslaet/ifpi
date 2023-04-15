lado = 6
angulos = 360 / lado

from turtle import *

speed(11)
shape("turtle")

for count in range(6):
    forward(100)
    right(angulos)

done()
