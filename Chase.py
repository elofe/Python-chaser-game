from turtle import *
import random
import math

wn = Screen()
wn.bgcolor("black")
wn.setup(width=1.0,height=1.0)

rnd1 = random.randrange(1, 5)
rnd2 = random.randrange(1, 5)

#for people taking turn
turn = 0

#to draw the environment
square = Turtle()
square.color("white")
square.speed(0)
square.penup()
square.setx(-200)
square.sety(-200)
square.pendown()
square.ht()


#player1
p1 = Turtle()
p1.color("red")
p1.shape("circle")
p1.speed(0)
p1.penup()
p1.setx(200)
p1.sety(-200)

#player2
p2 = Turtle()
p2.color("blue")
p2.shape("circle")
p2.speed(0)
p2.penup()
p2.setx(-200)
p2.sety(200)
p2.right(180)

#draw the environment
def drawing():
    square.forward(40)
    square.left(90)
    square.forward(2)
    square.backward(2)
    square.right(90)
    
def switchturn(t):
    if t == 1:
        return 2
    else:
        return 1
def taketurn(t):
    listen()
    if t == 1:
        onkey(go1a, "Right")
        onkey(go1b, "Up")
        onkey(fire1, "Return")
        onkey(nothing, "d")
        onkey(nothing, "w")
    if t == 2:
        onkey(nothing, "Right")
        onkey(nothing, "Up")
        onkey(fire2, "space")
        onkey(go2a, "d")
        onkey(go2b, "w")

#when player gets hit it takes damage and moves slower for one round
def slow(damage, speed):
    return speed - damage
       
def win1():
    turt = Turtle()
    turt.pendown()
    turt.ht()
    turt.color("red")
    turt.write("RED WINS", True, "center", ("Arial", 24, "normal"))
def win2():
    turt = Turtle()
    turt.pendown()
    turt.ht()
    turt.color("blue")
    turt.write("BLUE WINS", True, "center", ("Arial", 24, "normal"))
        
def step1():
    p1.left(90)
    p1.forward(20)
    if p1.xcor() == p2.xcor() and p1.ycor() == p2.ycor():
        win1()
def step2():
    p2.left(90)
    p2.forward(20)
    if p1.xcor() == p2.xcor() and p1.ycor() == p2.ycor():
        win2()
    
def go1a():
    global turn
    global rnd1
    #if it gets hit slow it down
    hit = fire1()
    speed = slow(hit, rnd1)
    #make p1 move
    for i in range (2*speed):
        #if p1 is in the corners
        if abs(p1.xcor()) == 200 and abs(p1.ycor()) == 200:
            step1()
        else:
            p1.forward(20)
            if p1.xcor() == p2.xcor() and p1.ycor() == p2.ycor():
                win1()
    #switch to p2
    turn = switchturn(turn)
    taketurn(turn)
    
def go1b():
    global turn
    global rnd1
    #if it gets hit slow it down
    hit = fire1()
    speed = slow(hit, rnd1) + 1
    #make p1 move but it's faster
    for i in range (2*(speed)):
        #if p1 is in the corners
        if abs(p1.xcor()) == 200 and abs(p1.ycor()) == 200:
            step1()
        else:
            p1.forward(20)
            if p1.xcor() == p2.xcor() and p1.ycor() == p2.ycor():
                win1()
    #switch to p2
    turn = switchturn(turn)
    taketurn(turn)
    
def go2a():
    global turn
    global rnd2
    #if it gets hit slow it down
    hit = fire2()
    speed = slow(hit, rnd2)
    #make p2 move
    for i in range (2*speed):
        #if p2 is in the corners
        if abs(p2.xcor()) == 200 and abs(p2.ycor()) == 200:
            step2()
        else:
            p2.forward(20)
            if p1.xcor() == p2.xcor() and p1.ycor() == p2.ycor():
                win2()
    #switch to p1
    turn = switchturn(turn)
    taketurn(turn)
    
def go2b():
    global turn
    global rnd2
    #if it gets hit slow it down
    hit = fire2()
    speed = slow(hit, rnd2) + 1
    #make p2 move but faster
    for i in range (2*speed):
        #if p2 is in the corners
        if abs(p2.xcor()) == 200 and abs(p2.ycor()) == 200:
            step2()
        else:
            p2.forward(20)
            if p1.xcor() == p2.xcor() and p1.ycor() == p2.ycor():
                win2()
    #switch to p1
    turn = switchturn(turn)
    taketurn(turn)
#a function that does nothing
def nothing():
    pass

def fire1():
    #create a fireball
    ball = Turtle()
    ball.speed(0)
    ball.penup()
    ball.ht()
    ball.shape("circle")
    ball.shapesize(0.5)
    ball.color("yellow")
    ball.setx(p2.xcor())
    ball.sety(p2.ycor())
    ball.speed(1)
    #if p2 is in the reach throw a fireball
    if p1.xcor() == p2.xcor() or p1.ycor() == p2.ycor():
        ball.st()
        ball.goto(p1.xcor(), p1.ycor())
        ball.ht()
        return 1
    else:
        ball.ht()
        return 0

def fire2():
    #create a fireball
    ball = Turtle()
    ball.speed(0)
    ball.penup()
    ball.ht()
    ball.shape("circle")
    ball.shapesize(0.5)
    ball.color("yellow")
    ball.setx(p1.xcor())
    ball.sety(p1.ycor())
    ball.speed(1)
    #if p1 is in the reach throw a fireball
    if p1.xcor() == p2.xcor() or p1.ycor() == p2.ycor():
        ball.st()
        ball.goto(p2.xcor(), p2.ycor())
        ball.ht()
        return 1
    else:
        ball.ht()
        return 0
    
#actually draw the environment
for i in range (37):
    drawing()
    if abs(square.xcor()) == 200 and abs(square.ycor()) == 200:
        square.left(90)
        drawing()
        
turn = switchturn(turn)
taketurn(turn)

wn.mainloop()
