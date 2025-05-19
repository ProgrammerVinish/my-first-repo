import turtle

t=turtle.Turtle()
t.speed(5)
turtle.bgcolor('black')
t.pensize(3)

def func():
    for i in range(200):
        t.right(1)
        t.forward(1)
t.color('red','pink') #pen,fill color
t.begin_fill()

t.left(140)
t.forward(111.65)
func()
t.left(120)
func()
t.forward(111.65)
t.end_fill()
t.hideturtle()
turtle.done()

'''
import turtle
import colorsys

# Setup screen and turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

# Setup color settings
h = 0
n = 36  # number of shapes

# Drawing the pattern
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 1/n
    t.color(c)
    t.forward(i * 3 / n + i)
    t.left(59)
    t.circle(i * 0.1)

# Hide turtle and complete
t.hideturtle()
turtle.done()
'''