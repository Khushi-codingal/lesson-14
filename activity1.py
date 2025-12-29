import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
sides = 7
sides_length = 70
angle = 360.0/sides
for i in range(sides):
    polygon.forward(sides_length)
    polygon.right(angle)
turtle.done()