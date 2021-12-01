# import turtle
from turtle import Turtle, Screen
# tim =  turtle.Turtle()
tim = Turtle()

my_screen = Screen()
print(my_screen.canvheight)
tim.shape('turtle')
tim.color('green')
tim.forward(100)
my_screen.exitonclick()
