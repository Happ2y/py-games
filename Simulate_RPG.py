# import dependencies
import pygame

# initialize pygame modules
pygame.init()

# create and display game window
(width, height) = (800, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Battle")

# keep the game window on
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
pygame.quit()
