import random
import turtle

# tess = turtle.Turtle()
# tess.color("red")
# tess.pensize(3)
# tess.left(90)
# tess.forward(200)
# tess.left(90)
# tess.forward(100)
# tess.left(90)
# tess.forward(200)
# tess.left(90)
# tess.forward(100)
#


# for i in range(1000):
#     print("We like Python's turtles!")

# for i in range(10):
#     print(random.randint(25,36), end=" ")

window = turtle.Screen()
# window.delay(50)

# triangle = turtle.Turtle()
# triangle.color("blue")
# triangle.pensize(2)
# triangle.penup()
# triangle.goto(-300,100)
# triangle.pendown()
# for i in range(3):
#     triangle.forward(200)
#     triangle.left(120)
# triangle.hideturtle()
#
# square = turtle.Turtle()
# square.color("red")
# square.pensize(2)
# square.penup()
# square.goto(100,100)
# square.pendown()
# for i in range(4):
#     square.forward(200)
#     square.left(90)
# square.hideturtle()
#
# hexagon = turtle.Turtle()
# hexagon.color("green")
# hexagon.pensize(2)
# hexagon.penup()
# hexagon.goto(-200,-200)
# hexagon.pendown()
# for i in range(6):
#     hexagon.forward(100)
#     hexagon.left(60)
# hexagon.hideturtle()
#
# octagon = turtle.Turtle()
# octagon.color("brown")
# octagon.pensize(2)
# octagon.penup()
# octagon.goto(200,-200)
# octagon.pendown()
# for i in range(8):
#     octagon.forward(100)
#     octagon.left(45)
# octagon.hideturtle()

turtle.bgcolor("red")
star = turtle.Turtle()
star.pensize(2)
star.pencolor("yellow")
star.fillcolor("yellow")
star.begin_fill()
star.penup()
star.goto(200,50)
star.pendown()
for i in range(5):
    star.right(144)
    star.forward(400)
star.end_fill()
star.hideturtle()

window.exitonclick()