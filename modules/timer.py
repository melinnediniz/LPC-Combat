import pygame
from config import Constant


class Timer:
    def __init__(self):
        self.time_count = Constant['GAME_TIME']
        self.time_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.time_event, 1000)

    def count(self):
        return pygame.time.set_timer(self.time_event, 1000)
