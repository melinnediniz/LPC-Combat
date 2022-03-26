import pygame
from config import *


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, sprite, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))



