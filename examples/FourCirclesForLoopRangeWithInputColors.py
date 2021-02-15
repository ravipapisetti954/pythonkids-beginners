# circle no loops

import turtle
t = turtle.Pen()
turtle.bgcolor("black")

# Ask the user for the number of circles in their play, default to 6

number_of_circles = int(turtle.numinput("Number of circles", "How many circles in your play?", 6))
for x in range(number_of_circles):
    t.pencolor("red")
    t.circle(50)
    t.pencolor("orange")
    t.circle(100)
    t.left(360/number_of_circles)
