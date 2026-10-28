from turtle import *

showturtle()

speed(0)
left(90)

def brokul(depth, length):
    if depth == 0:
        return
    forward(length)
    left(45)
    brokul(depth-1, length * 0.65)
    right(90)
    brokul(depth-1, length * 0.65)
    left(45)
    backward(length)

brokul(10, 128)


exitonclick()