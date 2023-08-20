import pygame
import os
from player import Player

# Window configs
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 24

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Images
MIDDLE_TILE = pygame.image.load(os.path.join('Assets', 'Tiles', 'middle_tile.png'))
UP_TILE = pygame.image.load(os.path.join('Assets', 'Tiles', 'up_tile.png'))
DOWN_TILE = pygame.image.load(os.path.join('Assets', 'Tiles', 'down_tile.png'))

# Player
RUNNING_PLAYER = pygame.sprite.Group()

# Set the caption of the window
pygame.display.set_caption("Line Runner")

def draw_window():
    # background
    WIN.fill(WHITE)

    # map tiles
    WIN.blit(MIDDLE_TILE, (WIDTH/2, HEIGHT/2))
    WIN.blit(MIDDLE_TILE, (WIDTH/2, HEIGHT/2))

    # player
    RUNNING_PLAYER.draw(WIN)
    RUNNING_PLAYER.update()

    # update the display
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    player = Player(100, 100)
    RUNNING_PLAYER.add(player)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
