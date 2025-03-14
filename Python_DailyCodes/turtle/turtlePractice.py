import turtle
screen = turtle.Screen()
screen.bgcolor("blue") 
donatello = turtle.Turtle() #donatello is mo's favorite TMNT

def triangle(x, y):
    donatello.pensize(5)
    donatello.pencolor("purple")
    donatello.penup()
    donatello.goto(x,y)
    donatello.pendown()
    # for i in range(3):
    donatello.tilt(30)
    donatello.stamp
    donatello.fd(10)



def square(x, y):
    donatello.pensize(5)
    donatello.pencolor("red")
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    for i in range(4): 
        donatello.forward(50) 
        donatello.right(90)

def circle(cx, cy, radius):
    donatello.pensize(8)
    donatello.pencolor("turquoise")
    donatello.fillcolor("yellow")
    donatello.penup()
    donatello.goto(cx, cy)
    donatello.pendown()
    donatello.begin_fill()
    donatello.circle(radius)
    donatello.end_fill()
    
#call functions
# square(30, 40)
# square(10, 50)
# square (100, 200)
# circle(-200, 200, 80)
triangle(300,300)

turtle.done() 