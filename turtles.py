import turtle


def polygon(location, color, length, number):
    """This function creates a turtle and makes it draw a shape according to the parameters in a window."""
    turt = turtle.Turtle()
    wn = turtle.Screen()
    turt.penup()
    turt.goto(location)
    turt.pendown()
    turt.color(color)
    for i in range(number):
        turt.forward(length)
        turt.left(360/number)
    wn.exitonclick()


def main():
    locationStart = (0, 0)
    turtColor = "blue"
    sideLength = 10
    sideNumber = 50

    polygon(locationStart, turtColor, sideLength, sideNumber)


if __name__ == "__main__":
    main()
