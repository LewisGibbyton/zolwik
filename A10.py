from turtle import *

showturtle()

speed(0)


def spirala(length):
    while length == 0:
        return
    forward(length)
    left(60)
    spirala(length - 5)



spirala(145)


exitonclick()