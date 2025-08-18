import turtle

def draw_petal(t, r, a):
    for _ in range(2):
        t.circle(r, a)
        t.left(180 - a)

def generate_color(i, total):
    # Create a smooth color transition from red → green → blue → red
    phase = (i / total) * 3  # Divide transition into 3 phases
    if phase < 1:
        r = int(255 * (1 - phase))
        g = int(255 * phase)
        b = 0
    elif phase < 2:
        phase -= 1
        g = int(255 * (1 - phase))    
        b = int(255 * phase)
        r = 0
    else:
        phase -= 2
        b = int(255 * (1 - phase))
        r = int(255 * phase)
        g = 0
    return (r, g, b)

def draw_flower(petals):
    turtle.colormode(255)
    t = turtle.Turtle()
    t.speed('fastest')
    for i in range(petals):
        t.color(generate_color(i, petals))
        draw_petal(t, 100, 60)
        t.left(360 / petals)
    t.hideturtle()
    turtle.done()

n = turtle.numinput("NO.", "Enter the no. of petals", default=5, minval=5)
draw_flower(int(n))
turtle.exitonclick()