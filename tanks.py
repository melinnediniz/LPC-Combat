from config import *
import pygame


class BlueTank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BLUE_TANK_SPRITE_UP)
        self.rect = self.image.get_rect(center=(BLUE_TANK_X_POS, BLUE_TANK_Y_POS))
        self.x_speed = 0
        self.previos_x_speed = -6
        self.y_speed = 0
        self.previos_y_speed = 0

    def move_up(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_UP)
        if self.x_speed - 2 == 0:
            self.previos_x_speed = self.x_speed * 3
            self.x_speed -= 2
        else:
            self.x_speed -= 2
            self.previos_x_speed = self.x_speed * 3
        self.y_speed = 0
        self.previos_y_speed = self.y_speed

    def move_down(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_DOWN)
        if self.x_speed + 2 == 0:
            self.previos_x_speed = self.x_speed * 3
            self.x_speed += 2
        else:
            self.x_speed += 2
            self.previos_x_speed = self.x_speed * 3
        self.y_speed = 0
        self.previos_y_speed = self.y_speed

    def move_right(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_RIGHT)
        self.x_speed = 0
        self.previos_x_speed = self.x_speed
        if self.y_speed - 2 == 0:
            self.previos_y_speed = self.y_speed * 3
            self.y_speed -= 2
        else:
            self.y_speed -= 2
            self.previos_y_speed = self.y_speed * 3

    def move_left(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_LEFT)
        self.x_speed = 0
        self.previos_x_speed = self.x_speed
        if self.y_speed + 2 == 0:
            self.previos_y_speed = self.y_speed * 3
            self.y_speed += 2
        else:
            self.y_speed += 2
            self.previos_y_speed = self.y_speed * 3

    def move_diagonal_top_right(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_DIAGONAL_TOP_RIGHT)
        self.x_speed += 2
        self.y_speed = 0

    def move_diagonal_top_left(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_DIAGONAL_TOP_LEFT)
        self.x_speed += 2
        self.y_speed = 0

    def move_diagonal_bottom_right(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_DIAGONAL_BOTTOM_RIGHT)
        self.x_speed += 2
        self.y_speed = 0

    def move_diagonal_bottom_left(self):
        self.image = pygame.image.load(BLUE_TANK_SPRITE_DIAGONAL_BOTTOM_LEFT)
        self.x_speed += 2
        self.y_speed = 0

    def turn_off_speed(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.rect.x += self.x_speed
        if self.x_speed != 0:
            self.previos_x_speed = self.x_speed * 3
        self.rect.y += self.y_speed
        if self.y_speed != 0:
            self.previos_y_speed = self.y_speed * 3
        self.turn_off_speed()


class GreenTank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(GREEN_TANK_SPRITE_UP)
        self.sprite = GREEN_TANK_SPRITE_UP
        self.rect = self.image.get_rect(center=(GREEN_TANK_X_POS, GREEN_TANK_Y_POS))
        self.x_speed = 0
        self.previos_x_speed = 6
        self.y_speed = 0
        self.previos_y_speed = 0

    def move_up(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_UP)
        self.sprite = GREEN_TANK_SPRITE_UP
        if self.x_speed + 2 == 0:
            self.previos_x_speed = self.x_speed * 3
            self.x_speed += 2
        else:
            self.x_speed += 2
            self.previos_x_speed = self.x_speed * 3
        self.y_speed = 0
        self.previos_y_speed = self.y_speed

    def move_down(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_DOWN)
        self.sprite = GREEN_TANK_SPRITE_DOWN
        if self.x_speed - 2 == 0:
            self.previos_x_speed = self.x_speed * 3
            self.x_speed -= 2
        else:
            self.x_speed -= 2
            self.previos_x_speed = self.x_speed * 3
        self.y_speed = 0
        self.previos_y_speed = self.y_speed

    def move_right(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_RIGHT)
        self.sprite = GREEN_TANK_SPRITE_RIGHT
        self.x_speed = 0
        self.previos_x_speed = self.x_speed
        if self.y_speed + 2 == 0:
            self.previos_y_speed = self.y_speed * 3
            self.y_speed += 2
        else:
            self.y_speed += 2
            self.previos_y_speed = self.y_speed * 3

    def move_left(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_LEFT)
        self.sprite = GREEN_TANK_SPRITE_LEFT
        self.x_speed = 0
        self.previos_x_speed = self.x_speed
        if self.y_speed - 2 == 0:
            self.previos_y_speed = self.y_speed * 3
            self.y_speed -= 2
        else:
            self.y_speed -= 2
            self.previos_y_speed = self.y_speed * 3

    def move_diagonal_top_right(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_DIAGONAL_TOP_RIGHT)
        self.x_speed += 2
        self.previos_x_speed = self.x_speed
        self.y_speed += 2

    def move_diagonal_top_left(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_DIAGONAL_TOP_LEFT)
        self.x_speed += 2
        self.previos_x_speed = self.x_speed
        self.y_speed -= 2

    def move_diagonal_bottom_right(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_DIAGONAL_BOTTOM_RIGHT)
        self.x_speed -= 2
        self.y_speed += 2

    def move_diagonal_bottom_left(self):
        self.image = pygame.image.load(GREEN_TANK_SPRITE_DIAGONAL_BOTTOM_LEFT)
        self.x_speed -= 2
        self.y_speed -= 2

    def turn_off_speed(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.rect.x += self.x_speed
        if self.x_speed != 0:
            self.previos_x_speed = self.x_speed * 3
        self.rect.y += self.y_speed
        if self.y_speed != 0:
            self.previos_y_speed = self.y_speed * 3
        self.turn_off_speed()
