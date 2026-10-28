from turtle import *

showturtle()

speed(0)


def trojkat(size, depth):
    if depth == 0:
        return
    for i in range(3):
        trojkat(size/3, depth-1)
        forward(size)
        left(120)



trojkat(128, 4)
exitonclick()