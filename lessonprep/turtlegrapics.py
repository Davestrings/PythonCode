import turtle as t


def setup():
    t.Screen()
    t.screensize(1000)
    t.bgcolor('blue')
    t.speed(0)
    t.hideturtle()


def body():
    t.penup()
    t.goto(0, 250)
    t.pendown()
    t.circle(120)
    t.fillcolor('white')
    t.penup()
    t.goto(0, -10)
    t.pendown()
    t.circle(80)
    t.penup()
    t.goto(0, 150)
    t.pendown()
    t.circle()


def hands():
    t.penup()
    t.goto(-90, 150)
    t.pendown()
    t.forward(30)
    t.right(15)
    t.forward(100)
    t.penup()
    t.goto(90, 150)
    t.pendown()
    t.forward(30)
    t.right(15)
    t.forward(100)


def main():
    setup()
    body()
    hands()


main()
