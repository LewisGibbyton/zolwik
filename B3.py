from turtle import *

showturtle()

speed(0)


def szesciokat(size, depth):
    if depth == 0:
        return
    for i in range(6):
        if i % 2 == 0:
            forward(size/4)
            right(120)
            szesciokat(size/2, depth-1)
            left(120)
            forward(3 * size / 4)
        else:
            forward(size)
        left(60)



szesciokat(64, 3)
exitonclick()