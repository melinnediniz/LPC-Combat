from config import BLUE_SHOT_SPRITE, BLUE_SHOT_X_POS, BLUE_SHOT_Y_POS, GREEN_SHOT_SPRITE, GREEN_SHOT_X_POS,\
    GREEN_SHOT_Y_POS
import pygame


class BlueShot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BLUE_SHOT_SPRITE)
        self.rect = self.image.get_rect(center=(BLUE_SHOT_X_POS, BLUE_SHOT_Y_POS))


class GreenShot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(GREEN_SHOT_SPRITE)
        self.rect = self.image.get_rect(center=(GREEN_SHOT_X_POS, GREEN_SHOT_Y_POS))

