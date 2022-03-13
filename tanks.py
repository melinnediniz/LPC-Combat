from config import *
import pygame


class BlueTank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite_sheet = BLUE_TANK_SPRITE_SHEET
        self.image = self.sprite_sheet[0]
        self.rect = self.image.get_rect(center=(BLUE_TANK_X_POS, BLUE_TANK_Y_POS))
        self.x_speed = 0
        self.previous_x_speed = -6
        self.y_speed = 0
        self.previous_y_speed = 0

    def move_up(self, angle):
        self.image = self.sprite_sheet[angle]
        if self.x_speed - 2 == 0:
            self.previous_x_speed = self.x_speed * 3
            self.x_speed -= 2
        else:
            self.x_speed -= 2
            self.previous_x_speed = self.x_speed * 3
        self.y_speed = 0
        self.previous_y_speed = self.y_speed

    def move_down(self, angle):
        self.image = self.sprite_sheet[angle]
        if self.x_speed + 2 == 0:
            self.previous_x_speed = self.x_speed * 3
            self.x_speed += 2
        else:
            self.x_speed += 2
            self.previous_x_speed = self.x_speed * 3
        self.y_speed = 0
        self.previous_y_speed = self.y_speed

    def move_right(self, angle):
        self.image = self.sprite_sheet[angle]
        '''self.x_speed = 0
        self.previous_x_speed = self.x_speed
        if self.y_speed - 2 == 0:
            self.previous_y_speed = self.y_speed * 3
            self.y_speed -= 2
        else:
            self.y_speed -= 2
            self.previous_y_speed = self.y_speed * 3'''

    def move_left(self, angle):
        self.image = self.sprite_sheet[angle]
        '''self.x_speed = 0
        self.previous_x_speed = self.x_speed
        if self.y_speed + 2 == 0:
            self.previous_y_speed = self.y_speed * 3
            self.y_speed += 2
        else:
            self.y_speed += 2
            self.previous_y_speed = self.y_speed * 3'''

    def turn_off_speed(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.rect.x += self.x_speed
        if self.x_speed != 0:
            self.previous_x_speed = self.x_speed * 3
        self.rect.y += self.y_speed
        if self.y_speed != 0:
            self.previous_y_speed = self.y_speed * 3
        self.turn_off_speed()


class GreenTank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite_sheet = GREEN_TANK_SPRITE_SHEET
        self.image = self.sprite_sheet[0]
        self.rect = self.image.get_rect(center=(GREEN_TANK_X_POS, GREEN_TANK_Y_POS))
        self.x_speed = 0
        self.previous_x_speed = 6
        self.y_speed = 0
        self.previous_y_speed = 0

    def move_up(self, angle):
        self.image = self.sprite_sheet[angle]
        if self.x_speed + 2 == 0:
            self.previous_x_speed = self.x_speed * 3
            self.x_speed += 2
        else:
            self.x_speed += 2
            self.previous_x_speed = self.x_speed * 3
        self.y_speed = 0
        self.previous_y_speed = self.y_speed

    def move_down(self, angle):
        self.image = self.sprite_sheet[angle]
        if self.x_speed - 2 == 0:
            self.previous_x_speed = self.x_speed * 3
            self.x_speed -= 2
        else:
            self.x_speed -= 2
            self.previous_x_speed = self.x_speed * 3
        self.y_speed = 0
        self.previous_y_speed = self.y_speed

    def move_right(self, angle):
        self.image = self.sprite_sheet[angle]
        '''self.x_speed = 0
        self.previous_x_speed = self.x_speed
        if self.y_speed + 2 == 0:
            self.previous_y_speed = self.y_speed * 3
            self.y_speed += 2
        else:
            self.y_speed += 2
            self.previous_y_speed = self.y_speed * 3'''

    def move_left(self, angle):
        self.image = self.sprite_sheet[angle]
        '''self.x_speed = 0
        self.previous_x_speed = self.x_speed
        if self.y_speed - 2 == 0:
            self.previous_y_speed = self.y_speed * 3
            self.y_speed -= 2
        else:
            self.y_speed -= 2
            self.previous_y_speed = self.y_speed * 3'''

    def turn_off_speed(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.rect.x += self.x_speed
        if self.x_speed != 0:
            self.previous_x_speed = self.x_speed * 3
        self.rect.y += self.y_speed
        if self.y_speed != 0:
            self.previous_y_speed = self.y_speed * 3
        self.turn_off_speed()
