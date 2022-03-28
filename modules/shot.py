from random import randint
import pygame


class Shot(pygame.sprite.Sprite):
    def __init__(self, sprite, tank_center, x_speed, y_speed):
        super().__init__()
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect(center=(tank_center[0], tank_center[1]))
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def collision_with_obstacle(self):
        self.x_speed *= -1
        self.y_speed = randint(-6, 6)
