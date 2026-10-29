from turtle import *
import math

speed(0)
showturtle()

def c3(length):
    if length <= 0:
        return
    forward(length)
    left(95)
    c3(length - 2.5)

c3(180)