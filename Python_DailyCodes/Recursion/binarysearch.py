
import math


def binarySearch(arr, low, high, x):
    if high >= low:
        
        middle = (high + low)//2

        if arr[middle] == x:
            print(middle)
        
        elif x < middle:
            binarySearch(arr, low, middle, x)
        elif x > middle:
            
            binarySearch(arr, middle, high, x)
        else:
            print("not in arr")



arr = [2,3,4,10,40]
x = 12 

result = binarySearch(arr, 0, len(arr)-1, x)

