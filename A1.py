from turtle import *

showturtle()

speed(0)


def fraktal(n, length):
    if n == 0:
        return  # Warunek stopu: na poziomie 0 nic nie rysujemy
    for i in range(4):
        forward(length / 2)
        right(90)
        fraktal(n - 1, length / 2)
        left(90)
        forward(length / 2)
        left(90)


fraktal(4, 64)


exitonclick()