import pygame
from config import Color, Constant
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

    def start_text(self):
        combat_surf = font_start.render('COMBAT', True, Color['YELLOW'])
        combat_rect = combat_surf.get_rect(topleft=(215, 245))
        bg_surf = font_start.render('COMBAT', True, Color['BLACK'])
        bg_rect = bg_surf.get_rect(topleft=(220, 250))
        self.surf.blit(bg_surf, bg_rect)
        self.surf.blit(combat_surf, combat_rect)

        press_surf = font_msg.render('PRESS "SPACE" TO PLAY', True, Color['BLACK'])
        press_rect = press_surf.get_rect(topleft=(295, 560))
        self.surf.blit(press_surf, press_rect)
