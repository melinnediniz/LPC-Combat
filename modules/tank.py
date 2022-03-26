import pygame
from math import sin, cos, radians


class Tank(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, color):
        super().__init__()
        self.angle = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        if self.color == 'green':
            self.image = pygame.image.load(f'sprites/green_tank/0.png').convert_alpha()
        elif self.color == 'blue':
            self.image = pygame.image.load(f'sprites/blue_tank/0.png').convert()
        self.rotated_img = self.image
        self.rect = self.rotated_img.get_rect(center=(x_pos, y_pos))
        self.speed = 3
        self.movement = True

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

    def move(self, back_or_foward):
        value = back_or_foward
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
                self.y_pos = self.y_pos
            elif 15 <= self.angle <= 75 or (-285 >= self.angle >= -345):
                self.x_pos -= self.speed * abs(cos(radians(self.angle))) * value
                self.y_pos -= self.speed * abs(sin(radians(self.angle))) * value
            elif self.angle == 90 or self.angle == -270:
                self.x_pos = self.x_pos
                self.y_pos -= self.speed * value
            elif 105 <= self.angle <= 165 or (-195 >= self.angle >= -255):
                self.x_pos += self.speed * abs(cos(radians(self.angle))) * value
                self.y_pos -= self.speed * abs(sin(radians(self.angle))) * value
            elif self.angle == 180 or self.angle == -180:
                self.x_pos += self.speed * value
                self.y_pos = self.y_pos
            elif 195 <= self.angle <= 255 or (-105 >= self.angle >= -165):
                self.x_pos += self.speed * abs(cos(radians(self.angle))) * value
                self.y_pos += self.speed * abs(sin(radians(self.angle))) * value
            elif self.angle == 270 or self.angle == -90:
                self.x_pos = self.x_pos
                self.y_pos += self.speed * value
            elif (285 <= self.angle <= 345) or (-15 >= self.angle >= -75):
                self.x_pos -= self.speed * abs(cos(radians(self.angle))) * value
                self.y_pos += self.speed * abs(sin(radians(self.angle))) * value

        print(f'{self.angle} -- {cos(self.angle):.3f} -- {sin(self.angle):.3f} -- {self.speed}')

    def lock(self):
        self.movement = False

    def draw(self, surf):
        if self.color == 'green':
            surf.blit(pygame.transform.rotate(self.rotated_img, self.angle), (self.x_pos, self.y_pos))
        if self.color == 'blue':
            surf.blit(pygame.transform.rotate(self.rotated_img, -self.angle), (self.x_pos, self.y_pos))
