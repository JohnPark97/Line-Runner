import json
import pygame
import os
import enum
from player import Player

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Images
TILE_WIDTH = 64
TILE_HEIGHT = 64
TILE_SPEED = 5
scroll_x = 0

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
FPS = 12

# Set the caption of the window
pygame.display.set_caption("Line Runner")

def load_map(level: int = 1):
    WIN.fill(WHITE)

    with open(os.path.join('Assets', 'Maps', f'{level}.json')) as file:
        data = json.load(file)

    tiles = data['tiles']

    i = 0
    for tile in tiles:
        y = HEIGHT/2
        if tile == 0:
            WIN.blit(MIDDLE_TILE, (i - scroll_x, y))
        elif tile == 1:
            WIN.blit(UP_TILE, (i - scroll_x, y))
        elif tile == 2:
            WIN.blit(DOWN_TILE, (i - scroll_x, y))
        i += TILE_WIDTH

def draw_window(is_map_loaded: bool):
    if is_map_loaded == False:
        load_map()
        is_map_loaded = True  
    
    # scroll the map to the left
    global scroll_x
    scroll_x += TILE_SPEED

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
    frame = 0

    is_map_loaded = False
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        frame += 1
        draw_window(is_map_loaded)

        player.load_animation()

    pygame.quit()


if __name__ == "__main__":
    main()
