def Factorial(n):
    if n == 0 and 1:
        return 1
    else:
        return n*Factorial(n-1) 
    
print(Factorial(5)) 


def paldrone(i, left, right):
    if left == right:
        return True
    
    if i[left] != i[right]:
        return False
    
    return paldrone(i, left + 1, right - 1)

print(paldrone("amanaplanacanalpanama", 0, len("amanaplanacanalpanama") - 1))
print(paldrone("hello", 0, len("hello") - 1))


def print_pattern(n):
        if n < 1:
             return 0
        
        for i in range(n):
             print('*', end="")
        print('\n')

        print_pattern(n-1)

print(print_pattern(5))