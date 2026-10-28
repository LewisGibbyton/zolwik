from turtle import *

showturtle()

speed(0)

def szesciokat(size, depth):
    if depth == 0:
        return
    for i in range(6):
        forward(size/4)
        right(120)
        szesciokat(size/2, depth-1)
        left(120)
        forward(3*size/4)
        left(60)






szesciokat(128, 3)

exitonclick()