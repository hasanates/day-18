import random
import turtle
from turtle import  Turtle, Screen


tt_turtle_obj = Turtle()
turtle.colormode(255)
tt_turtle_obj.pensize(2)
tt_turtle_obj.speed("fastest")
directions = [0, 90, 180, 270, 360]

def random_color():
    my_color = []
    r = random.choice(range(255))
    g = random.choice(range(255))
    b = random.choice(range(255))
    my_color.append(r)
    my_color.append(g)
    my_color.append(b)
    my_color = tuple(my_color)
    return  my_color


heading = tt_turtle_obj.heading()
while heading < 360 :

    tt_turtle_obj.circle(100)
    tt_turtle_obj.pencolor(random_color())
    tt_turtle_obj.setheading(heading)
    heading += 3
















screen = Screen()
screen.exitonclick()