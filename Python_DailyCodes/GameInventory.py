import random


Menu = ["Show Inventory", "Add a Game", "Delete a Game", "Generate Sale Bundle", "Check Game Availability", "Quit"]
Games = ["7 Days to Die","Baldur's Gate 3","Brawlhalla","CyberPunk 2077","Destiny 2",
         "Elden Ring","Skyrim","Enshrouded","Fallout 76","Lethal Company","Overwatch",
         "Palworld","Satisfactory","Sons Of The Forest","Valheim","Wasteland 3"]
gameLoop = True

def Print_Menu():
    for i in range(len(Menu)):
        print(i+1, Menu[i])
    print("\n")

def Show_Catalog(UserResponse):
    if UserResponse == '1':
        print(Games, "\n")
def Add_Game(UserResponse):
    if UserResponse == '2':
        Add_Game = input("Enter the game you would like to add to the inventory ")
        Games.append(Add_Game)
        Games.sort()

def Remove_Game(UserResponse):
    if UserResponse == '3':
        Remove_Game = input("Enter the game you would like to remove ")
        if Remove_Game in Games:
            Games.remove(Remove_Game)
            Games.sort

def Random_Sale(UserResponse):
    if UserResponse == '4':
        Random_Sale = random.randint(0, len(Games))
        print("Today's Sale Includes: ", Games[Random_Sale:Random_Sale+2])

def Game_Availibility(UserResponse):
    if UserResponse == '5':
        Game_Availibilty = input("Enter the game you would like to check ")
        if Game_Availibilty in Games:
            print(Game_Availibilty, " Is in our catalog")
        else:
            print(Game_Availibilty, " Is not in our catalog")


while gameLoop:
    Print_Menu()

    UserResponse = input("Enter Your Choice: ")
    
    Show_Catalog(UserResponse)
    Add_Game(UserResponse)
    Remove_Game(UserResponse)
    Random_Sale(UserResponse)
    Game_Availibility(UserResponse)

    if UserResponse == '6':
        print("Come Back Soon!!")
        break









