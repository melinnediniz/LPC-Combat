import pygame
from modules.tank import Tank
from config import *


class Collision:
    def __init__(self, sprite1, *args):
        self.sprite_1 = sprite1

