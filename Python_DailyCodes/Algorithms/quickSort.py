arr = [12, 11, 13, 5, 6]
def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivet = arr[0]
#fancy PCEP code lol
    left = [x for x in arr[1:] if x < pivet]

    middle = [x for x in arr if x == pivet]

    right = [x for x in arr[1:] if x > pivet]

    return QuickSort(left) + middle + QuickSort(right)


print(arr)

sortedArray = QuickSort(arr)


print(sortedArray)






