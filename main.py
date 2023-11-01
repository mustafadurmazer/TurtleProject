import turtle
'''
colors_turtle = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle_instance = turtle.Turtle()
#t = turtle.Pen()
turtle.bgcolor('black')

for i in range(360):
    turtle_instance.pencolor(colors_turtle[i % 6])
    turtle_instance.width(i // 100 + 1)
    turtle_instance.forward(i+25)
    turtle_instance.left(60)

turtle.done()
#turtle.mainloop()
'''

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("PYTHON TURTLE")

turtle.instance = turtle.Turtle()

def turtle_forward():
    turtle.instance.forward(100)

def turtle_right():
    turtle.instance.right(20)

def turtle_left():
    turtle.instance.left(20)

def clear_instance():
    turtle.instance.clear()

def turtle_return_home():
    turtle.instance.home()

def turtle_pen_up():
    turtle.instance.penup()

def turtle_pen_down():
    turtle.instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=turtle_right, key="Down")
drawing_board.onkey(fun=turtle_left, key="Up")
drawing_board.onkey(fun=clear_instance, key="c")
drawing_board.onkey(fun=turtle_return_home, key="h")
drawing_board.onkey(fun=turtle_pen_up, key="x")
drawing_board.onkey(fun=turtle_pen_down, key="z")
turtle.mainloop()
