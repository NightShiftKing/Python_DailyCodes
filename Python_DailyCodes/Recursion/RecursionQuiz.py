# def Fibonacci(num):
#     Fibonacci_Sequence = [] 
#     if num < 1: 
#         return 0
#     else:
        
#         return Fibonacci(num)
        
    


# def ForLoop(num2):
#     for i in range(num2):
#         print(i+(i+1))

# print(ForLoop(10))


def Fibonacci(num):
    if num < 1:
        return 0
    else:
       print( Fibonacci(num-1) + Fibonacci(num-2) )
       Fibonacci(num-1)

UserInput = int(input("Pick a Number "))

print(Fibonacci(UserInput))