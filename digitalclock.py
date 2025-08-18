import turtle
import time
from datetime import datetime
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Day, Date and Time")
pen = turtle.Turtle()
pen.hideturtle()
pen.color("cyan")
pen.penup()
pen.goto(0, 0)

while True:
    pen.clear()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d-%m-%Y")
    current_day = now.strftime("%A")
    pen.write(f"Day   : {current_day}\nDate  : {current_date}\nTime  : {current_time}",
        align="center", font=("Arial", 20, "bold"))
    time.sleep(1)
