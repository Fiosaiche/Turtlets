#!/usr/bin/python

import turtle
import random
random.seed()

screen = turtle.getscreen()
t0 = turtle.Turtle()
t1 = t0.clone()
t2 = t0.clone()
t3 = t0.clone()
t4 = t0.clone()

for turtle in screen.turtles():
    turtle.penup()
    turtle.ht()
    turtle.right(random.randrange(361))
    turtle.shape("turtle")
    turtle.resizemode("user")
    n = random.uniform(0.5,1)
    turtle.shapesize(n,n,n)
    turtle.st()

def caught(x,y):
    for turtle in screen.turtles():
        turtle.reset()
        turtle.penup()

while 1: 
    for turtle in screen.turtles():
        turtle.fd(2)
        turtle.right(33 - random.randrange(64))
        turtle.onclick(caught)
        
