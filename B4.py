from turtle import *

showturtle()

speed(0)


def kwadrat(size, depth):
    if depth == 0:
        return
    for i in range(4):
        forward(size)
        if i % 2 == 0:
            left(90)
            kwadrat(size/2, depth - 1)
            right(90)
        right(90)



kwadrat(128, 4)
exitonclick()