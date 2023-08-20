import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/running_1.png'))
        self.sprites.append(pygame.image.load('Assets/running_2.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x_pos, y_pos]

    def x_pos(self):
        return self.x_pos
    
    def y_pos(self):
        return self.y_pos


    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        
        self.image = self.sprites[self.current_sprite]