from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
is_race = False
your_turtle = screen.textinput(title="make your bet", prompt="select your turtle color")
colors = ["red","pink","blue","green","orange","violet"]
pos = [-120,-80,-30,20,70,120]
turtles = []
if your_turtle:
    is_race=True
for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230,y=pos[i])
    turtles.append(t)


while is_race:
    for i in turtles:
        if i.xcor()>220:
            is_race = False
            winner_color = i.pencolor()
            if winner_color == your_turtle:
                print(f"You've won! The {winner_color} turtle is the winner")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner")
        i.forward(random.randint(0,10))




screen.exitonclick()