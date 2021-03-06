import pygame

import random
from modules.screen import Screen
from modules.sound import Sound
from modules.tank import Tank
from modules.score import Score
from modules.obstacle import Obstacle
from modules.shot import Shot
from modules.timer import Timer
from config import Config

pygame.init()
pygame.display.set_caption("TANK PONG")


class Game:
    def __init__(self):
        self.surface = Screen().surface()
        self.current_screen = "start"
        self.score = Score()
        self.sound = Sound()
        self.screen = Screen()
        self.timer = Timer()

        self.all_sprites = pygame.sprite.Group()
        self.blue_tank = Tank(Config.BLUE_TANK_SPRITE_SHEET, Config.POSITION['BLUE_TANK_X_POS'],Config.POSITION['BLUE_TANK_Y_POS'], 'red')
        self.green_tank = Tank(Config.GREEN_TANK_SPRITE_SHEET, Config.POSITION['GREEN_TANK_X_POS'], Config.POSITION['GREEN_TANK_Y_POS'],
                               'green')
        self.obstacles = pygame.sprite.Group()
        for s, p in Config.OBSTACLES.items():
            self.obstacles.add(Obstacle(s, p[0], p[1]))
        self.all_sprites.add(self.blue_tank)
        self.all_sprites.add(self.green_tank)
        self.all_sprites.add(self.obstacles)

        self.green_shot_limiter = Config.CONSTANT['TICK_SHOT_LIMITER']
        self.blue_shot_limiter = Config.CONSTANT['TICK_SHOT_LIMITER']

        self.green_tank_angle = 0
        self.blue_tank_angle = 0

    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.current_screen = "main"
                elif event.key == pygame.K_ESCAPE:
                    exit()

        self.surface.fill(Config.COLOR['RED'])
        self.screen.start_text()
        pygame.display.update()

    def main(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == self.timer.time_event:
                self.timer.time_count -= 1
                print(self.timer.time_count)
                if 0 < self.timer.time_count < 11:
                    if self.timer.time_count % 2 == 0:
                        self.score.color_1, self.score.color_2 = Config.COLOR['RED'], Config.COLOR['RED']
                    elif self.timer.time_count % 2 != 0:
                        self.score.color_1, self.score.color_2 = Config.COLOR['GREEN'], Config.COLOR['BLUE']
                if self.timer.time_count == 0:
                    Config.BOOLEAN['is_game_over'] = True
                    self.surface.fill(random.choice(Config.list_of_colors))
                    for gs in self.green_tank.shots:
                        self.all_sprites.remove(gs)
                    for bs in self.blue_tank.shots:
                        self.all_sprites.remove(bs)
                    self.green_tank.lock(), self.blue_tank.lock()
                    Config.BOOLEAN['can_shot'] = False
                elif self.timer.time_count == -6:
                    for gs in self.green_tank.shots:
                        self.all_sprites.remove(gs)
                    for bs in self.blue_tank.shots:
                        self.all_sprites.remove(bs)
                    self.surface.fill(random.choice(Config.list_of_colors))
                    self.timer.time_count = 0
                    Config.BOOLEAN['can_shot'] = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.current_screen = "start"
                    self.timer.time_count = Config.CONSTANT['GAME_TIME']
                    self.green_tank.initial(), self.blue_tank.initial()
                    self.score.reset()
                    for gs in self.green_tank.shots:
                        self.all_sprites.add(gs)
                    for bs in self.blue_tank.shots:
                        self.all_sprites.add(bs)
                elif event.key == pygame.K_ESCAPE:
                    exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.green_tank.move_up(self.green_tank_angle, Config.BOOLEAN['is_game_over'])
        if keys[pygame.K_a]:
            self.green_tank.move_down(self.green_tank_angle, Config.BOOLEAN['is_game_over'])
        if keys[pygame.K_w] and self.green_tank.movement:
            if self.green_tank.sprite_change_limiter == 5:
                if self.green_tank_angle == 0:
                    self.green_tank_angle = 22
                else:
                    self.green_tank_angle -= 1
                self.green_tank.move_left(self.green_tank_angle, Config.BOOLEAN['is_game_over'])
                self.green_tank.sprite_change_limiter = 0
            self.green_tank.sprite_change_limiter += 1
        if keys[pygame.K_s] and self.green_tank.movement:
            if self.green_tank.sprite_change_limiter == 5:
                if self.green_tank_angle == 23:
                    self.green_tank_angle = 1
                else:
                    self.green_tank_angle += 1
                self.green_tank.move_right(self.green_tank_angle, Config.BOOLEAN['is_game_over'])
                self.green_tank.sprite_change_limiter = 0
            self.green_tank.sprite_change_limiter += 1
        if keys[pygame.K_LEFT]:
            self.blue_tank.move_up(self.blue_tank_angle, Config.BOOLEAN['is_game_over'])
        if keys[pygame.K_RIGHT]:
            self.blue_tank.move_down(self.blue_tank_angle, Config.BOOLEAN['is_game_over'])
        if keys[pygame.K_UP] and self.blue_tank.movement:
            if self.blue_tank.sprite_change_limiter == 5:
                if self.blue_tank_angle == 23:
                    self.blue_tank_angle = 1
                else:
                    self.blue_tank_angle += 1
                self.blue_tank.move_right(self.blue_tank_angle, Config.BOOLEAN['is_game_over'])
                self.blue_tank.sprite_change_limiter = 0
            self.blue_tank.sprite_change_limiter += 1
        if keys[pygame.K_DOWN] and self.blue_tank.movement:
            if self.blue_tank.sprite_change_limiter == 5:
                if self.blue_tank_angle == 0:
                    self.blue_tank_angle = 22
                else:
                    self.blue_tank_angle -= 1
                self.blue_tank.move_left(self.blue_tank_angle, Config.BOOLEAN['is_game_over'])
                self.blue_tank.sprite_change_limiter = 0
            self.blue_tank.sprite_change_limiter += 1
        if keys[pygame.K_g] and not self.green_tank.already_thrown and Config.BOOLEAN['can_shot']:
            self.all_sprites.add(self.green_tank.create_new_shot(Config.GREEN_SHOT_SPRITE))
            self.green_shot_limiter = 0
            self.green_tank.already_thrown = True
        if keys[pygame.K_l] and not self.blue_tank.already_thrown and Config.BOOLEAN['can_shot']:
            self.all_sprites.add(self.blue_tank.create_new_shot(Config.BLUE_SHOT_SPRITE))
            self.blue_shot_limiter = 0
            self.blue_tank.already_thrown = True

        if pygame.sprite.collide_mask(self.green_tank, self.blue_tank):
            self.green_tank.lock()
            self.blue_tank.lock()

        for gs in self.green_tank.shots:
            if pygame.sprite.collide_mask(gs, self.blue_tank):
                gs.kill()
                self.green_tank.shots.remove(gs)
                self.score.update(1)
                self.sound.play_kill()
                self.blue_tank.randomize()

            for o in self.obstacles:
                if pygame.sprite.collide_mask(gs, o):
                    gs.collision_with_obstacle()

        for bs in self.blue_tank.shots:
            if pygame.sprite.collide_mask(bs, self.green_tank):
                bs.kill()
                self.blue_tank.shots.remove(bs)
                self.score.update(2)
                self.sound.play_kill()
                self.green_tank.randomize()

            for o in self.obstacles:
                if pygame.sprite.collide_mask(bs, o):

                    bs.collision_with_obstacle()

        for o in self.obstacles:
            if pygame.sprite.collide_mask(self.green_tank, o):
                self.green_tank.collide_with_obstacle()
            if pygame.sprite.collide_mask(self.blue_tank, o):
                self.blue_tank.collide_with_obstaclej()

        self.score.display(Config.POSITION['SCORE_1_POS'], 1, self.score.color_1)
        self.score.display(Config.POSITION['SCORE_2_POS'], 2, self.score.color_2)
        self.all_sprites.update()
        self.all_sprites.draw(self.surface)
        pygame.display.update()

        if self.timer.time_count > 0:
            self.surface.fill(Config.COLOR['RED'])
            self.sound.call_sound()
        if self.green_shot_limiter == Config.CONSTANT['TICK_SHOT_LIMITER']:
            self.green_tank.already_thrown = False
        if self.blue_shot_limiter == Config.CONSTANT['TICK_SHOT_LIMITER']:
            self.blue_tank.already_thrown = False
        self.green_shot_limiter += 1
        self.blue_shot_limiter += 1

    def change_screen(self):
        if self.current_screen == "start":
            self.start()
        elif self.current_screen == "main":
            self.main()
