#main.py
import turtle
bob = turtle.Turtle()

bob.speed(500)

bob.color("blue")

for times in range(150):
    print (times,times * 10)
    bob.forward(times * 10)
    bob.left(121)

bob.color("white")

bob.goto(-10,0)

bob.speed(500)

bob.color("red")

for times in range(150):
    print (times,times * 10)
    bob.forward(times * 10)
    bob.left(91)

bob.color("white")

bob.goto(-10,0)

bob.speed(500)

bob.color("yellow")

for times in range(150):
    print (times,times * 10)
    bob.forward(times * 10)
    bob.left(95)

