import pygame
import os
from player import Player

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Images
TILE_WIDTH = 64
TILE_HEIGHT = 64

MIDDLE_TILE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', 'middle_tile.png')), (TILE_WIDTH, TILE_HEIGHT))
UP_TILE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', 'up_tile.png')), (TILE_WIDTH, TILE_HEIGHT))
DOWN_TILE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', 'down_tile.png')), (TILE_WIDTH, TILE_HEIGHT))

# Player
TILE_X_OFFSET = 32
TILE_Y_OFFSET = TILE_HEIGHT/2 + 16
RUNNING_PLAYER = pygame.sprite.Group()

# Window configs
WIDTH, HEIGHT = TILE_WIDTH * 12, TILE_HEIGHT * 8
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 4

# Set the caption of the window
pygame.display.set_caption("Line Runner")

def draw_window():
    # background
    WIN.fill(WHITE)

    # map tiles
    i = 0
    while i < WIDTH:
        WIN.blit(MIDDLE_TILE, (i, HEIGHT/2))
        i += TILE_WIDTH
    WIN.blit(MIDDLE_TILE, (WIDTH/2, HEIGHT/2))
    # WIN.blit(UP_TILE, (WIDTH/2 + TILE_WIDTH, HEIGHT/2))
    # WIN.blit(DOWN_TILE, (WIDTH/2 + TILE_WIDTH * 2, HEIGHT/2))

    # player
    RUNNING_PLAYER.draw(WIN)
    RUNNING_PLAYER.update()

    # update the display
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    player = Player(TILE_X_OFFSET, HEIGHT/2 - TILE_Y_OFFSET)
    RUNNING_PLAYER.add(player)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.load_animation()
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
