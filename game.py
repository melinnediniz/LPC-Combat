import pygame
import random
from config import Colors, Constants, display_score, reset, update_score
from config import timer, time_count, list_colors

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
        global time_count
        for event in pygame.event.get():
            if event.type == timer:
                time_count += 1
                print(f"TIMER {time_count}")
                if time_count > Constants.GAME_TIME:
                    if time_count == Constants.GAME_TIME + 5:
                        screen.fill(random.choice(list_colors))
                    elif time_count > Constants.GAME_TIME + 10:
                        screen.fill(random.choice(list_colors))
                        time_count = Constants.GAME_TIME + 5             

            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif event.key == pygame.K_1:
                    update_score(1)
                elif event.key == pygame.K_2:
                    update_score(2)
                elif event.key == pygame.K_r:
                    reset()
                    time_count = 0
                    self.current_screen = "start"

        if time_count < Constants.GAME_TIME:
            screen.fill(Colors.RED)
        display_score(screen, Constants.SCORE_1_POS, 1)
        display_score(screen, Constants.SCORE_2_POS, 2)
        pygame.display.flip()


    def change_screen(self):
        if self.current_screen == "start":
            self.start()
        elif self.current_screen == "main":
            self.main()        