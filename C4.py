from turtle import *
import math

speed(0)
showturtle()

def c4(n, length):
    if n == 0:
        return
    for i in range(4):
        forward(length)
        left(90)
    left(90)
    forward(length)
    right(45)
    
    s = length / math.sqrt(2)
    c4(n - 1, s)
    forward(s)
    right(90)
    c4(n - 1, s)
    
    left(90)
    backward(s)
    left(45)
    backward(length)
    right(90)

c4(7, 64)