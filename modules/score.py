from config import Color, Constant
import pygame

pygame.init()
font = pygame.font.Font(Constant['FONT'], 60)


class Score:
    def __init__(self, surf):
        self.score_1 = 0
        self.score_2 = 0
        self.surf = surf
        self.color_1 = Color['GREEN']
        self.color_2 = Color['BLUE']


    def score_display(self, position, score, color):
        if score == 1:
            score = self.score_1
        elif score == 2:
            score = self.score_2
        score_surf = font.render(f'{score}', True, color)
        score_rect = score_surf.get_rect(topleft=position)
        self.surf.blit(score_surf, score_rect)

    def update(self, sc):
        if sc == 1:
            self.score_1 += 1
        elif sc == 2:
            self.score_2 += 1

    def reset(self):
        self.score_1 = 0
        self.score_2 = 0
