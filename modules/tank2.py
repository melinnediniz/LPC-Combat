from cmath import sqrt
from tkinter import N
from turtle import speed
import pygame
import math

class Tank(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, color):
        super().__init__()
        self.angle = 0
        self.xpos = x_pos
        self.ypos = y_pos
        self.color = color
        if self.color == 'green':
            self.image = pygame.image.load(f'sprites/green_tank/0.png')
            self.shot_x_speed = 6
            self.signal = 1
        else:
            self.shot_x_speed = -6
            self.signal = -1
            self.image = pygame.image.load(f'sprites/blue_tank/0.png')
            self.shot_x_speed = 6
        self.rotade_img = self.image
        self.rect = self.rotade_img.get_rect(center=(x_pos, y_pos))
        self.speed = math.hypot(self.rect.width, self.rect.height)
        self.shot_y_speed = 0
        self.previous_direction = 'up'

    def rotate(self):
        if self.color == "blue":
            print('blue')
        else:
            if self.angle < 180:
                self.angle += 15
            else:
                self.angle = 180 
            rotade_img = pygame.transform.rotate(self.image, self.angle)
            
            print(f'ANGLE {self.angle}')
            return rotade_img

    def move_up(self):
        if self.color == 'green':
            if self.angle == 90:
                self.xpos += 0
            else:
                self.xpos += abs(math.cos(self.angle)) * 3

            if self.angle == 135:
                self.ypos -= 1
            if self.angle == 0:
                self.ypos += 0
            else:
                self.ypos -= abs(math.sin(self.angle)) * 3
            print(f'{self.angle} --- {math.cos(self.angle)} -- {self.speed}')
        else:
            print("blue")

    def lock(self):
        self.movement = False

    def draw(self, surf):
        surf.blit(pygame.transform.rotate(self.rotade_img, self.angle), (self.xpos, self.ypos))