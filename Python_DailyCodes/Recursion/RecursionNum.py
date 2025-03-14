

def reverse_number(num):
    if num == 0:
        return 0
    else:
        return (num % 10)* 10**str(num).count(str(num)) + reverse_number(int(num/10)) 
        

print(reverse_number(1234))