from turtle import *


showturtle()
right(60)
speed(0)


def fraktal(n, length):
    if n == 0:
        return  # Warunek stopu: na poziomie 0 nic nie rysujemy

    for i in range(3):
        forward(length)
        if n > 0:
            fraktal(n - 1, length / 2)


        right(120)


fraktal(4, 128)


exitonclick()