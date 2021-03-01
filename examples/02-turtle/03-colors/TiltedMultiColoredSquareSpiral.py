# Drawing square
# Try changing the range value
# Try changing the degrees
import turtle

t = turtle.Pen()
# Visit http://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm for all the supported 03-colors
colors = ["red", "green", "blue", "orange"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(92)

