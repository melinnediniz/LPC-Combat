import random

from modules.draw import Draw
from modules.sound import Sound
from modules.tank import Tank
from modules.score import Score
from modules.obstacle import Obstacle
from modules.shot import Shot
from config import *

pygame.init()
screen = pygame.display.set_mode((Constant["WIDTH"], Constant['HEIGHT']))
pygame.display.set_caption("TANK PONG")


class Game:
    def __init__(self):
        self.shot_green = None
        self.shot_blue = None
        self.current_screen = "start"
        self.draw = Draw(screen)
        self.score = Score()
        self.sound = Sound()

        self.obstacles_sprites = pygame.sprite.Group()
        self.tanks_sprites = pygame.sprite.Group()
        self.shot_group = pygame.sprite.Group()

        self.blue_tank = Tank(POSITIONS['BLUE_TANK_X_POS'], POSITIONS['BLUE_TANK_Y_POS'], 'blue')
        self.green_tank = Tank(POSITIONS['GREEN_TANK_X_POS'], POSITIONS['GREEN_TANK_Y_POS'], 'green')
        self.tanks_sprites.add(self.green_tank)
        self.tanks_sprites.add(self.blue_tank)
        self.obstacles = pygame.sprite.Group()
        for sprite, pos in OBSTACLES.items():
            self.obstacles.add(Obstacle(sprite, pos[0], pos[1]))

        self.obstacles_sprites.add(self.obstacles)

        self.green_already_thrown = False
        self.blue_already_thrown = False
        self.green_shot_limiter = TICK_SHOT_LIMITER
        self.blue_shot_limiter = TICK_SHOT_LIMITER
        self.green_shot_group = []
        self.blue_shot_group = []

    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.current_screen = "main"
                elif event.key == pygame.K_ESCAPE:
                    exit()

        screen.fill(Color['RED'])
        self.draw.start_text()
        pygame.display.flip()

    def main(self):
        global time_count

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.USEREVENT + 1:
                time_count -= 1
                # print(time_count)
                if 0 < time_count < 11:
                    if time_count % 2 == 0:
                        self.score.color_1, self.score.color_2 = Color['RED'], Color['RED']
                    elif time_count % 2 != 0:
                        self.score.color_1, self.score.color_2 = Color['GREEN'], Color['BLUE']
                if time_count == 0:
                    screen.fill(random.choice(list_of_colors))
                    self.green_tank.lock(), self.blue_tank.lock()
                elif time_count == -6:
                    screen.fill(random.choice(list_of_colors))
                    time_count = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.green_tank.rotate_up()
                elif event.key == pygame.K_s:
                    self.green_tank.rotate_down()
                if event.key == pygame.K_UP:
                    self.blue_tank.rotate_up()
                elif event.key == pygame.K_DOWN:
                    self.blue_tank.rotate_down()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                self.green_tank.move(1)
            elif keys[pygame.K_a]:
                self.green_tank.move(-1)
            if keys[pygame.K_j]:
                self.blue_tank.move(1)
            elif keys[pygame.K_l]:
                self.blue_tank.move(-1)
            if keys[pygame.K_2]:
                self.green_tank.is_flipping = True

        if self.green_tank.is_flipping:
            self.green_tank.flip()

        if time_count > 0:
            screen.fill(Color['RED'])
            self.sound.play_move(), self.sound.play_flip()
        self.draw.score_display(POSITIONS['SCORE_1_POS'], 1, self.score.color_1)
        self.draw.score_display(POSITIONS['SCORE_2_POS'], 2, self.score.color_2)
        self.green_tank.draw(screen), self.blue_tank.draw(screen)
        self.obstacles_sprites.update(), self.shot_group.update()
        self.obstacles_sprites.draw(screen), self.shot_group.draw(screen)
        pygame.display.flip()

    def change_screen(self):
        if self.current_screen == "start":
            self.start()
        elif self.current_screen == "main":
            self.main()
