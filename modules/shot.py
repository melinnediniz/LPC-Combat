import pygame


class Shot(pygame.sprite.Sprite):
    def __init__(self, sprite, x_pos, y_pos):
        # adicionar parametro de valor negativo pro shot do azul
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.x_pos += 5
