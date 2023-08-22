import pygame

RUNNING = "running"
IDLE = "idle"

class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.state = RUNNING

        self.load_running_animation()

        # character sprite
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        # character position
        self.rect = self.image.get_rect()
        self.rect.topleft = [x_pos, y_pos]


    def x_pos(self):
        return self.x_pos
    
    def y_pos(self):
        return self.y_pos

    def set_state(self, state):
        if self.state != state:
            self.state = state

    def load_animation(self):
        if self.state == RUNNING:
            self.load_running_animation()
        elif self.state == IDLE:
            self.load_idle_animation()

        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        
        self.image = self.sprites[self.current_sprite]

    def load_running_animation(self):
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/running_1.png'))
        self.sprites.append(pygame.image.load('Assets/running_2.png'))

    def load_idle_animation(self):
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/running_1.png'))
        self.sprites.append(pygame.image.load('Assets/running_2.png'))

