from turtle import *

showturtle()

speed(0)


def sierpinski(depth, size):
    if depth == 0:
        return
    for i in range(3):
        forward(size)
        left(120)
        sierpinski(depth-1, size/2)


sierpinski(5, 256)
exitonclick()