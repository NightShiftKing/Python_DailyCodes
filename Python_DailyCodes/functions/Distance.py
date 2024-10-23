import math


x1 = int(input("what is the value of x1?"))
x2 = int(input("what is the value of x2?"))
y1 = int(input("what is the value of y1?"))

y2 = int(input("what is the value of y2?"))

def Distance(x1,x2,y1,y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
    print(distance)

Distance(x1,x2,y1,y2)