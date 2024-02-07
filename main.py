# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 50)
#
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_colors)

import turtle
import random


color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141),
              (254, 194, 0)]

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.setx(-350)
tim.sety(-300)
tim.speed(0)
turtle.colormode(255)
x_count = 0

for _ in range(100):
    tim.dot(30, random.choice(color_list))
    x_count += 1
    if x_count == 10:
        tim.sety(tim.ycor() + 70)
        tim.setx(-350)
        x_count = 0
    else:
        tim.setx(tim.xcor() + 70)

screen = turtle.Screen()
screen.exitonclick()

