import game
import pygame
from config import Constant, Boolean


class Main:
    def __init__(self):
        self.game_clock = pygame.time.Clock()
        self.game = game.Game()

    def mainloop(self):
        while Boolean['game_loop']:
            self.game.change_screen()
            self.game_clock.tick(Constant['CLOCK'])


main = Main()
if __name__ == '__main__':
    main.mainloop()
