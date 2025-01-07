from turtle import Turtle, Screen
import pandas as pd

#setting screen
screen = Screen()
screen.title("India States Game")
image = "India_map.gif"
screen.addshape(image)

#setting turtle
turtle = Turtle()
turtle.shape(image)
#setting up pandas
data = pd.read_csv("state_coor.csv")
all_states_list = data["state_name"].to_list()

guessed_states = []

while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/30 correct", prompt="What's another state's name?").lower()
    if answer_state == "exit":
        break
    else:
        if answer_state in all_states_list:
            guessed_states.append(answer_state)
            t = Turtle()
            t.hideturtle()
            t.penup()
            t.color("yellow")
            state_data = data[data["state_name"] == answer_state]
            t.goto(state_data["x"].item(), state_data["y"].item())
            t.write(answer_state, align="center", font=("Courier", 10, "bold"))



screen.exitonclick()