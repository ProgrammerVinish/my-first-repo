import turtle

# Set up turtle screen
wn = turtle.Screen()
wn.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.pensize(3)
pen.color("red")
pen.begin_fill()
pen.speed(1)

# Start drawing heart
pen.fillcolor("red")
pen.begin_fill()

pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)

pen.end_fill()
pen.hideturtle()

# Optional: Write message
pen.penup()
pen.goto(0, -40)
pen.color("white")
pen.write("Made with ❤️ in Python", align="center", font=("Arial", 16, "bold"))

turtle.done()
