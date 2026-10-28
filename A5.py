from turtle import *

showturtle()

speed(0)


def fraktal(n, length):
    if n == 0:
        return  # Warunek stopu: na poziomie 0 nic nie rysujemy
    for i in range(4):
        forward(length)
        right(90)
        fraktal(n-1, length/2)
        left(180)



fraktal(5, 64)


exitonclick()