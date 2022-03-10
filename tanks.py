from config import *
import pygame


class BlueTank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BLUE_TANK_SPRITE_UP)
        self.rect = self.image.get_rect(center=(BLUE_TANK_X_POS, BLUE_TANK_Y_POS))
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_UP)

    def move_down(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_DOWN)

    def move_right(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_RIGHT)

    def move_left(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_LEFT)

    def move_diagonal_top_right(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_DIAGONAL_TOP_RIGHT)

    def move_diagonal_top_left(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_DIAGONAL_TOP_LEFT)

    def move_diagonal_bottom_right(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_DIAGONAL_BOTTOM_RIGHT)

    def move_diagonal_bottom_left(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_DIAGONAL_BOTTOM_LEFT)


class GreenTank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(GREEN_TANK_SPRITE_UP)
        self.rect = self.image.get_rect(center=(GREEN_TANK_X_POS, GREEN_TANK_Y_POS))
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_UP)

    def move_down(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_DOWN)

    def move_right(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_RIGHT)

    def move_left(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_LEFT)

    def move_diagonal_top_right(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_DIAGONAL_TOP_RIGHT)

    def move_diagonal_top_left(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_DIAGONAL_TOP_LEFT)

    def move_diagonal_bottom_right(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_DIAGONAL_BOTTOM_RIGHT)

    def move_diagonal_bottom_left(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_DIAGONAL_BOTTOM_LEFT)
