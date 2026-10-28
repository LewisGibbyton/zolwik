from turtle import *

showturtle()

speed(0)


def kwadrat(depth, size):
    if depth == 0:
        return
    for i in range(4):
        if i % 2 == 0:
            forward(size)
        else:
            forward(size/4)
            right(90)
            kwadrat(depth-1, size/2)
            left(90)
            forward(3*size/4)
        left(90)

kwadrat(4, 256)
exitonclick()