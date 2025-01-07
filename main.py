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



screen.mainloop()