# Circle Spiral
# Try changing the numbers in the loop and turning degrees
import turtle

t = turtle.Pen()
# Visit http://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm for all the supported colors
colors = ["red", "green", "blue", "orange"]
turtle.bgcolor("black")
for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(95)
