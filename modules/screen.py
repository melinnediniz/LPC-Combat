import pygame
from config import Color, Constant

pygame.init()
font_start = pygame.font.Font(Constant['FONT'], 120)
font_msg = pygame.font.Font(Constant['FONT_2'], 22)
font = pygame.font.Font(Constant['FONT'], 60)


class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode(Constant['SCREEN_DIMENSION'])

    def surface(self):
        return self.screen

    def start_text(self):
        combat_surf = font_start.render('COMBAT', True, Color['YELLOW'])
        combat_rect = combat_surf.get_rect(topleft=(215, 245))
        bg_surf = font_start.render('COMBAT', True, Color['BLACK'])
        bg_rect = bg_surf.get_rect(topleft=(220, 250))
        self.screen.blit(bg_surf, bg_rect)
        self.screen.blit(combat_surf, combat_rect)

        press_surf = font_msg.render('PRESS "SPACE" TO PLAY', True, Color['BLACK'])
        press_rect = press_surf.get_rect(topleft=(295, 560))
        self.screen.blit(press_surf, press_rect)

