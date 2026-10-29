from turtle import *
import math

speed(0)
showturtle()

def c6(n, length):
    if n == 0:
        return
    for i in range(4):
        c6(n - 1, length / 3)
        forward(2 * length / 3)
        c6(n - 1, length / 3)
        backward(2 * length / 3)
        left(90)

c6(4, 162)