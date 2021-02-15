# SpiralMyName_Loops.py

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]

# Ask the user's name using tutle's textinput pop-up window
your_name = turtle.textinput("Enter your name", "what is your name?")

# Draw a spiral of the name of the screen, written 100 times
for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font = ("Arial", int((x+4)/4), "bold"))
    t.left(92)
    
