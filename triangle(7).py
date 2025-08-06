import turtle
k = turtle.Turtle()
screen = turtle.Screen()
a = turtle.numinput("Number", "Enter the number of triangles:", default=1, minval=1)
for j in range(int(a)):
    n = turtle.numinput("Size", "Enter the size of the side:", default=100, minval=50) 
    k.begin_fill()  
    for i in range(3):
        k.forward(n)
        k.left(120) 
    k.penup()
    k.forward(n + 20)
    k.pendown()
k.hideturtle()
turtle.exitonclick()