# print("programming.about.i.o.t.devies.inshAllaha")
# print("elon musk and mr beast")
# "when add the the two number"
# "x'y"
# print("x'y""when add the the two number")
# print("usama maher and brother ""end")
# print("end""tehseen maher.")
# print("usama maher and brother tehseen maher ")
# print("@usama!||%&maher %%175 m wala")
# def greet(name):
#     print("Hello", name)

# greet("Usama")
# greet("Ali")
# print("usama and ahmad")
# print("fizan and ahmad")
# import turtle
# screen = turtle.Screen()
# screen.title("Simple Car")
# screen.bgcolor("lightblue")
# car = turtle.Turtle()
# car.shape("square")
# car.color("red")
# car.shapesize(stretch_wid=1, stretch_len=2)
# car.penup()
# wheel1 = turtle.Turtle()
# wheel1.shape("circle")
# wheel1.color("black")
# wheel1.penup()
# wheel1.goto(-15, -15)

# wheel2 = turtle.Turtle()
# wheel2.shape("circle")
# wheel2.color("black")
# wheel2.penup()
# wheel2.goto(15, -15)
# def move_forward():
#     car.forward(10)
#     wheel1.forward(10)
#     wheel2.forward(10)

# def move_backward():
#     car.backward(10)
#     wheel1.backward(10)
#     wheel2.backward(10)
# screen.listen()
# screen.onkey(move_forward, "Up")
# screen.onkey(move_backward, "Down")

# screen.mainloop()
import turtle

# Screen
screen = turtle.Screen()
screen.bgcolor("white")

# Car body
car = turtle.Turtle()
car.speed(3)
car.color("red")
car.begin_fill()
car.forward(120)
car.left(90)
car.forward(40)
car.left(90)
car.forward(120)
car.left(90)
car.forward(40)
car.left(90)
car.end_fill()

# Wheel 1
car.penup()
car.goto(25, -10)
car.pendown()
car.color("black")
car.begin_fill()
car.circle(10)
car.end_fill()

# Wheel 2
car.penup()
car.goto(95, -10)
car.pendown()
car.begin_fill()
car.circle(10)
car.end_fill()

turtle.done()
            