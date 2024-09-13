import pygame
pygame.init()
pygame.display.set_caption("graphical for loops")
screen = pygame.display.set_mode((800,800))

gameover = False

while not gameover:
    screen.fill((0,0,0))

    for i in range(20):
        pygame.draw.rect(screen, (200,0,0), (125*i, 50, 50,50))
        pygame.draw.rect(screen, (0,0,200), (50*i, 100, 20,20))
        pygame.draw.rect(screen, (200,200,0), (50*i, 150, 20,20))
        pygame.draw.rect(screen, (0,200,0), (50*i, 200, 20,20))

    pygame.display.flip()

pygame.quit()