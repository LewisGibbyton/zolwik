from turtle import *
import math

speed(0)
showturtle()

left(90)

def b8(n, length):
    if n == 0:
        return
    left(45)
    for i in range(3):
        forward(length)
        b8(n - 1, length / 2)
        backward(length)
        if i < 2:
            right(45)
    left(45)

b8(5, 128)