import turtle

t=turtle.Turtle()
t.speed()
t.pensize(3)
turtle.bgcolor('black')

def func():
    for i in range(200):
        t.right(1)
        t.forward(1)
t.color('red','pink')
t.begin_fill()

t.left(140)
t.forward(111.25)
func()
t.left(120)
func()
t.forward(111.25)

t.end_fill()
t.hideturtle()
turtle.done()