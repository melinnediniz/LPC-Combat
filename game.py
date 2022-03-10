import pygame
from config import Colors, Constants, display_score, update_score
from tanks import *

pygame.init()
screen = pygame.display.set_mode(Constants.SCREEN_DIMENSIONS)
pygame.display.set_caption("TANK PONG")

all_sprites = pygame.sprite.Group()
blue_tank = BlueTank()
green_tank = GreenTank()
all_sprites.add(blue_tank)
all_sprites.add(green_tank)


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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            green_tank.move_up()
        if keys[pygame.K_a]:
            green_tank.move_down()
        if keys[pygame.K_w]:
            green_tank.move_left()
        if keys[pygame.K_s]:
            green_tank.move_right()
        if keys[pygame.K_LEFT]:
            blue_tank.move_up()
        if keys[pygame.K_RIGHT]:
            blue_tank.move_down()
        if keys[pygame.K_UP]:
            blue_tank.move_right()
        if keys[pygame.K_DOWN]:
            blue_tank.move_left()
        if keys[pygame.K_d] and keys[pygame.K_w]:
            green_tank.move_diagonal_top_right()
        if keys[pygame.K_d] and keys[pygame.K_s]:
            green_tank.move_diagonal_top_left()
        if keys[pygame.K_a] and keys[pygame.K_w]:
            green_tank.move_diagonal_bottom_right()
        if keys[pygame.K_a] and keys[pygame.K_s]:
            green_tank.move_diagonal_bottom_left()
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            blue_tank.move_diagonal_top_right()
        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            blue_tank.move_diagonal_top_left()
        if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            blue_tank.move_diagonal_bottom_right()
        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            blue_tank.move_diagonal_bottom_left()

        screen.fill(Colors.RED)
        display_score(screen, Constants.SCORE_1_POS, 1)
        display_score(screen, Constants.SCORE_2_POS, 2)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.update()

    def change_screen(self):
        if self.current_screen == "start":
            self.start()
        elif self.current_screen == "main":
            self.main()