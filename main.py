"""
    Date created: 29/07/2024
    Last modified: 30/07/2024
    Python Version: 3.12
"""

import random
import turtle as t

timmy = t.Turtle()
t.colormode(255)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86),
              (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
              (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]


def starting_point():
    timmy.penup()
    timmy.hideturtle()
    timmy.setheading(225)
    timmy.forward(325)
    timmy.setheading(0)
    timmy.speed('fastest')


def new_line(dots):
    if dots % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


def main():
    starting_point()
    dots_number = 100

    for dot_count in range(1, dots_number + 1):
        color = random.choice(color_list)
        timmy.dot(20, color)
        timmy.forward(50)
        new_line(dot_count)

    t.Screen().exitonclick()


main()
