import random
import turtle
import keyboard
import time
tis = turtle.Turtle()
apple = turtle.Turtle()
tis.shape('turtle')
color1 = 'green'
tis.penup()
apple.penup()
apple.shapesize(3)
size = 1
rand = random.randint(-450, 450)
rand2 = random.randint(-400, 400)
apple.goto(rand, rand2)
while True:
    time.sleep(0.1)
    if keyboard.is_pressed("d"):
        tis.seth(0)
        tis.forward(10)
        time.sleep(0.1)
    elif keyboard.is_pressed("space"):
        tis.goto(rand, rand2)
        time.sleep(0.1)
    elif keyboard.is_pressed("s"):
        tis.seth(270)
        tis.forward(10)
        time.sleep(0.1)
    elif keyboard.is_pressed("w"):
        tis.seth(90)
        tis.forward(10)
        time.sleep(0.1)
    elif keyboard.is_pressed("a"):
        tis.seth(180)
        tis.forward(10)
        time.sleep(0.1)
    # elif round(tis.pos()) == round(apple.pos()):
    elif tis.pos()[0] == apple.pos()[0] :
        rand = random.randint(-450, 450)
        rand2 = random.randint(-400, 400)
        apple.goto(rand, rand2)
        size = size + 1
        tis.shapesize(size)
    elif size == 10:


        size = size + 10
        tis.shapesize(size)
        time.sleep(0.1)
        size = size - 10
        tis.shapesize(size)
        time.sleep(0.1)




turtle.done()
# pip3 install keyboard