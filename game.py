import pygame
from config import Colors, Constants, display_score, update_score

pygame.init()
screen = pygame.display.set_mode(Constants.SCREEN_DIMENSIONS)
pygame.display.set_caption("TANK PONG")


class Game:
    def __init__(self):
        self.current_screen = "start"

    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.current_screen = "main"
                elif event.key == pygame.K_ESCAPE:
                    exit()

        screen.fill(Colors.GREEN)
        pygame.display.flip()


    def main(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.current_screen = "start"
                elif event.key == pygame.K_ESCAPE:
                    exit()


        screen.fill(Colors.RED)
        display_score(screen, Constants.SCORE_1_POS, 1)
        display_score(screen, Constants.SCORE_2_POS, 2)
        pygame.display.flip()


    def change_screen(self):
        if self.current_screen == "start":
            self.start()
        elif self.current_screen == "main":
            self.main()