import turtle


turtle.bgcolor("gray")
turtle.title("Drawing by Artur Z.")

s = turtle.getscreen()
t = turtle.Turtle()

t.right(90)
t.forward(100)

# Set the fill color to red
t.fillcolor("red")
t.begin_fill()

# Draw the circle with a radius of 100 pixels
t.circle(100)

# End the fill and stop drawing
t.end_fill()
t.hideturtle()

# Wait until user exits
turtle.done()
