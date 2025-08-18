import turtle
def draw_petal(t, r, a):
    for _ in range(2):
        t.circle(r, a)
        t.left(180 - a)
def draw_flower(petals):
    t = turtle.Turtle()
    t.color("magenta")
    for _ in range(petals):
        draw_petal(t, 100, 60)
        t.left(360 / petals)
    t.hideturtle()
    turtle.done()
n=turtle.numinput("NO.","Enter the no0. of petals",default=5,minval=5)
draw_flower(int (n))
turtle.exitonclick()