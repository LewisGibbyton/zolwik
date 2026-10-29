from turtle import *
import math

speed(0)
showturtle()


def c2(length):
    if length <= 0:
        return
    forward(length)
    right(144)
    c2(length - 6)

c2(180)