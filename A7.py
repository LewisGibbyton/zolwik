from turtle import *

showturtle()

speed(0)


def fraktal(n, length):
    if n == 0:
        return  # Warunek stopu: na poziomie 0 nic nie rysujemy
    for i in range(3):
        forward(length/4)
        right(60)
        fraktal(n-1, length/2)
        left(60)
        forward(3 * length / 4)
        left(120)



fraktal(4, 256)


exitonclick()