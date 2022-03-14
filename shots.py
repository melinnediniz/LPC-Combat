from config import BLUE_SHOT_SPRITE, GREEN_SHOT_SPRITE
import pygame


class BlueShot(pygame.sprite.Sprite):
    def __init__(self, tank_center, x_speed, y_speed):
        super().__init__()
        self.image = pygame.image.load(BLUE_SHOT_SPRITE)
        self.rect = self.image.get_rect(center=(tank_center[0], tank_center[1]))
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed


class GreenShot(pygame.sprite.Sprite):
    def __init__(self, tank_center, x_speed, y_speed):
        super().__init__()
        self.image = pygame.image.load(GREEN_SHOT_SPRITE)
        self.rect = self.image.get_rect(center=(tank_center[0], tank_center[1]))
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
