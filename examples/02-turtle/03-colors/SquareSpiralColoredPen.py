# Drawing square
# Try changing the range value
# Try changing the degrees
import turtle

t = turtle.Pen()
t.pencolor("red")
t.pencolor("azure1")
# Visit http://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm for all the supported 03-colors

for x in range(100):
    t.forward(x)
    t.left(90)

