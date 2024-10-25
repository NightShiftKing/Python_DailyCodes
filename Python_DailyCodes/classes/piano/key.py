import pygame

class Key():
    def __init__(self, xpos, ypos, audio):
        self.xpos = xpos
        self.ypos = ypos
        self.audio = audio
        self.Width = 100
        self.Height = 300
        k1 = pygame.mixer.Sound('key01.mp3')
        k3 = pygame.mixer.Sound('key03.mp3')
        k5 = pygame.mixer.Sound('key05.mp3')
        k7 = pygame.mixer.Sound('key07.mp3')
        k9 = pygame.mixer.Sound('key09.mp3')
        k11 = pygame.mixer.Sound('key11.mp3')
        k13 = pygame.mixer.Sound('key13.mp3')
        k15 = pygame.mixer.Sound('key15.mp3')


    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), (self.xpos, self.ypos, self.Width, self.Height), 2)

    def PlaySound(self, MousePosX, MousePosY, press):
        if MousePosX > self.xpos and MousePosX < self.Width and MousePosY > self.ypos and press:
            pygame.mixer.Sound.play(self.audio)
            print('playsound')
