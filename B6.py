from turtle import *

showturtle()

speed(0)


def kwadrat(size, depth):
    if depth == 0:
        return
    for i in range(4):
        kwadrat(size/3, depth-1)
        forward(size)
        left(90)



kwadrat(128, 4)
exitonclick()