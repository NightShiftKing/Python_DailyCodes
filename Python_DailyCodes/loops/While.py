num = 0
while num <=20:
    print(num)
    num += 2 


WantFish = "No"
while WantFish != "yes":
    response = input("Want a fish? yes/no ") 
    if response == "yes":
        WantFish = "yes"
    
        print("Fish")
    else:
        break 


num1 = 0
while num1 != 7:
    guess = input('guess a number between 1-10 ')
    if guess != "7":
        print("nope, try again")
    else:
        print("good job!")
        break 


     

