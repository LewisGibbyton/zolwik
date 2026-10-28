from turtle import *

showturtle()

speed(0)


def spirala(length):
    while length == 0:
        return
    forward(length)
    left(120)
    spirala(length - 3)



spirala(210)


exitonclick()