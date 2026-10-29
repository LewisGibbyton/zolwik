from turtle import *
import math

speed(0)
showturtle()



def b7(n, length):
    if n == 0:
        return
    for i in range(6):
        forward(length)
        left(60)
        if i % 2 == 0:
            b7(n - 1, length / 2)


b7(4, 128)