
array = [1,4,7,2]

def circleCircumference(r):
    return r*2*3.14



def isEven(num):
    if num %2 == 0:
        return True
    else:
        return False
    
def frog(num):
    for i in range(num):
        print("ribbit ", end="")

for i in range(len(array)):
    print(circleCircumference(array[i]))
    print(isEven(array[i]))
    print(frog(array[i]))