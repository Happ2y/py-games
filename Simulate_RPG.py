# import dependencies
import pygame

# initialize pygame modules
pygame.init()

# create and display game window
panel = 150
(width, height) = (800, 400 + panel)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Battle")

# define background & panel images
background_image = pygame.image.load(
    "assets/background/background.png").convert_alpha()
panel_image = pygame.image.load(
    "assets/icons/panel.png").convert_alpha()


def draw_bg():
    # draw background
    screen.blit(background_image, (0, 0))


def draw_panel():
    # draw panel background
    screen.blit(panel_image, (0, height - panel))


# keep the game window on
play = True
while play:
    draw_bg()
    draw_panel()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    pygame.display.update()
pygame.quit()
