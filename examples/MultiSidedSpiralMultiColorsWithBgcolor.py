# Circle Spiral
# Try changing the numbers in the loop and turning degrees
import turtle

t = turtle.Pen()
# Visit http://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm for all the supported colors
colors = ["red", "green", "blue", "orange", "purple", "yellow"]
sides = 6
turtle.bgcolor("black")
for x in range(360):
    t.pencolor(colors[x%4])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)
    
