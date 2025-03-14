logs = [
    "INFO", "DEBUG", "WARNING", "DATA_A",
    "ERROR", "DEBUG", "INFO", "DATA_B",
    "WARNING", "ERROR", "DEBUG", "DATA_C",
    "INFO", "DEBUG", "ERROR", "DATA_D"
]

def extract(logs):
    first = logs[3:4]
    second = logs[7:8]
    third = logs[11:12]
    fourth = logs[15:]
    return first + second + third + fourth

print(extract(logs))

list = [1,2,3,4,5,6,7,8,9,10,11]
def middle_five(list):
    return list[4:9]

print(middle_five(list))

arr = [1,2,3,4,5,6,7,8,9,10,11]
def reverseList(arr):
    revArr = []
    for i in range(len(arr)-1, -1, -1):
        
        revArr.append(arr[i])
    return revArr

print(reverseList(arr))