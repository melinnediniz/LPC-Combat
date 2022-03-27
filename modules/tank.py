import pygame
from math import sin, cos, radians
from random import randint
from config import Images
from modules.shot import Shot


class Tank(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, color):
        super().__init__()
        self.angle = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        if self.color == 'green':
            self.image = Images['GREEN_TANK'].convert()
        elif self.color == 'blue':
            self.image = Images['BLUE_TANK'].convert()
        self.rotated_img = self.image
        self.rect = self.rotated_img.get_rect(center=(x_pos, y_pos))
        self.speed = 3
        #self.center_x = self.image.get_width()/2
        self.is_flipping = False

    def create_shot(self):
        if self.color == "green":
            return Shot(Images['BLUE_SHOT_SPRITE'], self.x_pos, self.y_pos)
        elif self.color == "blue":
            return Shot(Images['GREEN_SHOT_SPRITE'], self.x_pos, self.y_pos)

    def flip(self):
        if self.angle < 360:
            self.angle += 20
            self.rotated_img = pygame.transform.rotate(self.image, self.angle)
        else:
            self.randomize()

    def rotate_up(self):
        if self.angle < 360:
            self.angle += 15
        elif self.angle >= 360:
            self.angle = 0

        print(f'ANGLE {self.angle}')

    def rotate_down(self):
        if self.angle >= -360:
            self.angle -= 15
        elif self.angle <= -360:
            self.angle = 0

        print(f'ANGLE {self.angle}')

    def move(self, back_or_forward):
        value = back_or_forward
        if self.color == 'green':
            if self.angle == 0 or self.angle == 360:
                self.x_pos += self.speed * value
                self.y_pos = self.y_pos
            elif 15 <= self.angle <= 75 or (-285 >= self.angle >= -345):
                self.x_pos += self.speed * abs(cos(radians(self.angle))) * value
                self.y_pos -= self.speed * abs(sin(radians(self.angle))) * value
            elif self.angle == 90 or self.angle == -270:
                self.x_pos = self.x_pos
                self.y_pos -= self.speed * value
            elif 105 <= self.angle <= 165 or (-195 >= self.angle >= -255):
                self.x_pos -= self.speed * abs(cos(radians(self.angle))) * value
                self.y_pos -= self.speed * abs(sin(radians(self.angle))) * value
            elif self.angle == 180 or self.angle == -180:
                self.x_pos -= self.speed * value
                self.y_pos = self.y_pos
            elif 195 <= self.angle <= 255 or (-105 >= self.angle >= -165):
                self.x_pos -= self.speed * abs(cos(radians(self.angle))) * value
                self.y_pos += self.speed * abs(sin(radians(self.angle))) * value
            elif self.angle == 270 or self.angle == -90:
                self.x_pos = self.x_pos
                self.y_pos += self.speed * value
            elif (285 <= self.angle <= 345) or (-15 >= self.angle >= -75):
                self.x_pos += self.speed * abs(cos(radians(self.angle))) * value
                self.y_pos += self.speed * abs(sin(radians(self.angle))) * value

        if self.color == 'blue':
            if self.angle == 0 or self.angle == 360:
                self.x_pos -= self.speed * value
            elif 15 <= self.angle <= 75 or (-285 >= self.angle >= -345):
                self.x_pos -= self.speed * abs(cos(radians(self.angle))) * value
                self.y_pos -= self.speed * abs(sin(radians(self.angle))) * value
            elif self.angle == 90 or self.angle == -270:
                self.y_pos -= self.speed * value
            elif 105 <= self.angle <= 165 or (-195 >= self.angle >= -255):
                self.x_pos += self.speed * abs(cos(radians(self.angle))) * value
                self.y_pos -= self.speed * abs(sin(radians(self.angle))) * value
            elif self.angle == 180 or self.angle == -180:
                self.x_pos += self.speed * value
            elif 195 <= self.angle <= 255 or (-105 >= self.angle >= -165):
                self.x_pos += self.speed * abs(cos(radians(self.angle))) * value
                self.y_pos += self.speed * abs(sin(radians(self.angle))) * value
            elif self.angle == 270 or self.angle == -90:
                self.y_pos += self.speed * value
            elif (285 <= self.angle <= 345) or (-15 >= self.angle >= -75):
                self.x_pos -= self.speed * abs(cos(radians(self.angle))) * value
                self.y_pos += self.speed * abs(sin(radians(self.angle))) * value

        # print(f'{self.angle} -- {cos(self.angle):.3f} -- {sin(self.angle):.3f} -- {self.speed}')

    def randomize(self):
        pygame.time.delay(60)
        self.x_pos = randint(200, 600)
        self.y_pos = randint(200, 600)
        self.is_flipping = False
        self.rotated_img = Images['GREEN_TANK']
        self.angle = 0

    def lock(self):
        self.movement = False

    def draw(self, surf):
        if self.color == 'green':
            surf.blit(pygame.transform.rotate(self.rotated_img, self.angle), (self.x_pos, self.y_pos))
        if self.color == 'blue':
            surf.blit(pygame.transform.rotate(self.rotated_img, -self.angle), (self.x_pos, self.y_pos))
