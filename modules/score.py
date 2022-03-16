import pygame
from config import Color, Constant

pygame.init()
font = pygame.font.Font(Constant['FONT'], 60)
font_start = pygame.font.Font(Constant['FONT'], 120)
font_msg = pygame.font.Font(Constant['FONT_2'], 22)

class Score:
    def __init__(self, surf):
        self.surf = surf
        self.score_1 = 0
        self.score_2 = 0
        self.color_1 = Color['GREEN']
        self.color_2 = Color['BLUE']

    def display(self, position, score, color):
        if score == 1:
            score = self.score_1
        elif score == 2:
            score = self.score_2
        score_surf = font.render(f'{score}', True, color)
        score_rect = score_surf.get_rect(topleft=position)
        self.surf.blit(score_surf, score_rect)


    def update(self, score):
        if score == 1:
                self.score_1 +=1
        elif score == 2:
                self.score_2 += 1

    def reset(self):
        self.score_1 = 0
        self.score_2 = 0
