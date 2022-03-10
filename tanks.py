from config import BLUE_TANK_SPRITE_UP, BLUE_TANK_X_POS, BLUE_TANK_Y_POS, GREEN_TANK_SPRITE_UP, GREEN_TANK_X_POS,\
    GREEN_TANK_Y_POS
import pygame


class BlueTank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BLUE_TANK_SPRITE_UP)
        self.rect = self.image.get_rect(center=(BLUE_TANK_X_POS, BLUE_TANK_Y_POS))
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_right(self):
        pass

    def move_left(self):
        pass

    def update(self):
        pass


class GreenTank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(GREEN_TANK_SPRITE_UP)
        self.rect = self.image.get_rect(center=(GREEN_TANK_X_POS, GREEN_TANK_Y_POS))
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_right(self):
        pass

    def move_left(self):
        pass

    def update(self):
        pass