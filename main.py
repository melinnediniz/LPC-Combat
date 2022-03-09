import game
import pygame
from config import Constants, game_loop

game_clock = pygame.time.Clock()
game = game.Game()

while game_loop:
    game.change_screen()
    game_clock.tick(Constants.CLOCK)