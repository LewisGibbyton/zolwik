from turtle import *
import math

speed(0)
showturtle()

def c5(n, length):
    if n == 0:
        return
    for i in range(4):
        c5(n - 1, length / 3)
        forward(length / 3)
        c5(n - 1, length / 3)
        forward(2 * length / 3)
        left(90)

c5(4, 162)