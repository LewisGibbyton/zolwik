from turtle import *
import math

speed(0)
showturtle()

def c1(length):
    if length <= 0:
        return
    forward(length)
    left(123)
    c1(length - 1.5)

c1(180)