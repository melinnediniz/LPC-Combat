import pygame
from config import *
from modules.score import Score

pygame.init()
font = pygame.font.Font(Constant['FONT'], 60)
font_start = pygame.font.Font(Constant['FONT'], 120)
font_msg = pygame.font.Font(Constant['FONT_2'], 22)

class Draw:
    def __init__(self, surf):
        self.score = Score()
        self.surf = surf 

    
    def score_display(self, position, score, color):
        if score == 1:
            score = self.score.score_1
        elif score == 2:
            score = self.score.score_2
        score_surf = font.render(f'{score}', True, color)
        score_rect = score_surf.get_rect(topleft=position)
        self.surf.blit(score_surf, score_rect)
