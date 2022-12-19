from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwords():
    tim.forward(10)

def move_backwords():
     tim.backward(10)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwords, "w")
screen.onkey(move_backwords,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear_screen,"c")

screen.exitonclick()


#drew what ever you want by using the keys W,S,A,D,C
#when you click the screen to exit 