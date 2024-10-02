import pygame
import math

pygame.init()  # initializes Pygame
pygame.display.set_caption("Spiral Pumpkins!")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # create game screen
screen.fill((0, 0, 0))  # paint background black

# Set up some colors
PUMPKIN_ORANGE = (255, 165, 0)
GREEN = (0, 150, 0)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# Function to draw a pumpkin recursively in a spiral with full arcs
def draw_pumpkin_spiral(x, y, width, height, depth, angle):
    if depth == 0:
        return  # Base case: stop recursion when depth is 0
   
    # Draw pumpkin body (ellipse)
    pygame.draw.ellipse(screen, PUMPKIN_ORANGE, (x, y, width, height))
   
    # Draw black outline around the pumpkin
    pygame.draw.ellipse(screen, BLACK, (x, y, width, height), 2)  # width of 2 for outline

   
    # Draw pumpkin stem (rectangle)
    stem_width = width // 5
    stem_height = height // 5
    pygame.draw.rect(screen, GREEN, (x + (width // 2 - stem_width // 2), y - stem_height, stem_width, stem_height))
   
    # Draw black outline for the stem
    pygame.draw.rect(screen, BLACK, (x + (width // 2 - stem_width // 2), y - stem_height, stem_width, stem_height), 2)

    # Add ellipses to simulate the pumpkin's ridges/curves on both sides
    pygame.draw.ellipse(screen, BLACK, (x + width * 0.1, y, width * 0.8, height), 2)  # outermost ellipse
    pygame.draw.ellipse(screen, BLACK, (x + width * 0.2, y, width * 0.6, height), 2)

    # Calculate the next position using trigonometry to create a spiral
    new_width = width * 1.15  # Shrink pumpkin width by 15%
    new_height = height * 1.15  # Shrink pumpkin height by 15%
    radius = width * 0.7  # Adjust how far the next pumpkin is from the current one


    new_x = x + radius * math.cos(angle)  # Calculate new x position in a spiral
    new_y = y + radius * math.sin(angle)  # Calculate new y position in a spiral
    
    new_angle = angle + math.pi / 8  # Increase the angle for the spiral effect 

    # Recursive call to draw the next pumpkin in the spiral
    draw_pumpkin_spiral(new_x, new_y, new_width, new_height, depth - 1, new_angle)

# Initial pumpkin size and position
initial_x = 400
initial_y = 400
initial_width = 35
initial_height = 30
recursion_depth = 20  # Number of recursive pumpkins to draw
initial_angle = 0  # Start angle

# Call the recursive function
draw_pumpkin_spiral(initial_x, initial_y, initial_width, initial_height, recursion_depth, initial_angle)


pygame.display.flip()  # Flips all the shapes onto the game screen (needed for every game)

# Keep the window open until the user closes it
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()