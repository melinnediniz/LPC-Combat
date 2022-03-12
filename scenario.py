from config import *
import pygame


class CenterBlock(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(CENTER_BLOCK_SPRITE)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class Block(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(BLOCK_SPRITE)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class RightUpRectangle(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(RIGHT_UP_RECTANGLE_SPRITE)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class LeftUpRectangle(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(LEFT_UP_RECTANGLE_SPRITE)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class RightDownRectangle(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(RIGHT_DOWN_RECTANGLE_SPRITE)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class LeftDownRectangle(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(LEFT_DOWN_RECTANGLE_SPRITE)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class RightGoal(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(RIGHT_GOAL_SPRITE)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class LeftGoal(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(LEFT_GOAL_SPRITE)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))