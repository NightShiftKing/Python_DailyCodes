# import math
# def calculate_circumference(radius):
#     return 2*3.14*radius

# print(calculate_circumference(2))


# def zigzag_pattern(n):
#     for i in range(1, n, 2):
#         print(i, end='')
#     for j in range(n-3, 0, -2):
#         print(j, end='')

# zigzag_pattern(10)
# zigzag_pattern(15) 
# zigzag_pattern(20)


def sumOf3sAnd5s(n):
    sum = 0
    for i in range(n+1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum

print(sumOf3sAnd5s(15))
print(sumOf3sAnd5s(5))
print(sumOf3sAnd5s(10))
