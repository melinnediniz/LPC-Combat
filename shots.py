from config import BLUE_SHOT_SPRITE, GREEN_SHOT_SPRITE, TIME_SHOT
import pygame


class BlueShot(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, x_speed, y_speed):
        super().__init__()
        self.image = pygame.image.load(BLUE_SHOT_SPRITE)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.shot = False
        self.time = 0

    def update(self):
        if self.shot == True:
            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
            if self.time == TIME_SHOT:
                self.shot = False
                self.time = 0
                self.kill()

    def action_shoot(self, x_pos, y_pos, x_speed, y_speed, shot):
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.shot = shot

    def update_time(self, time):
        if self.shot == True:
            self.time += time
    

class GreenShot(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, x_speed, y_speed):
        super().__init__()
        self.image = pygame.image.load(GREEN_SHOT_SPRITE)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.shot = False
        self.time = 0

    def update(self):
        if self.shot == True:
            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
            if self.time == TIME_SHOT:
                self.shot = False
                self.time = 0
                self.kill()

    def action_shoot(self, x_pos, y_pos, x_speed, y_speed, shot):
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.shot = shot

    def update_time(self, time):
        if self.shot == True:
            self.time += time
