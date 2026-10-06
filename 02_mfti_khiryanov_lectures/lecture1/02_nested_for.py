import turtle

def turtle_t():
    for step in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(50)
            turtle.left(360 / 3)
        turtle.end_fill()

        turtle.forward(50)
        turtle.right(60)

turtle.shape("turtle")
turtle.shapesize(3)
turtle.color("green", "yellow")
turtle.speed(6)

turtle.hideturtle()
turtle_t()
turtle.backward(300)
turtle_t()