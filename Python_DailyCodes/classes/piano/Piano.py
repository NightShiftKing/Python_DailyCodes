
import pygame
from key import Key
pygame.init()#initializes Pygame
pygame.display.set_caption("python piano program")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
press = False


#audio stuff!
pygame.mixer.init()
k1 = pygame.mixer.Sound('key01.mp3')
k3 = pygame.mixer.Sound('key03.mp3')
k5 = pygame.mixer.Sound('key05.mp3')
k7 = pygame.mixer.Sound('key07.mp3')
k9 = pygame.mixer.Sound('key09.mp3')
k11 = pygame.mixer.Sound('key11.mp3')
k13 = pygame.mixer.Sound('key13.mp3')
k15 = pygame.mixer.Sound('key15.mp3')

#this holds onto what key the user has pressed

audio = [k1,k3,k5,k7,k9,k11,k13,k15]

KeyBoard = []

for i in range(8):
    KeyBoard.append(Key(i*100, 500, audio[i])) 

for i in range(len(KeyBoard)):
    print(KeyBoard[i].xpos)


#gameloop###################################################
while True:

    
    #event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()
    
    #update/timer section---------------------------------------    

    
    #input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        press = True

    if event.type == pygame.MOUSEBUTTONUP:
        press = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos


    #render section---------------------------------------------
    for i in range(len(KeyBoard)):
        KeyBoard[i].draw(screen)

    #the keys 
   
    
    #if a key is pressed, highlight in grey and play the sound:
    for i in range(len(KeyBoard)):
        KeyBoard[i].PlaySound(mousePos[0],mousePos[1], press)

    
    pygame.display.flip() #always needed at the end of every game loop!
    

#end game loop##############################################

pygame.quit()
