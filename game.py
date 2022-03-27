import random
from modules.draw import Draw
from modules.sound import Sound
from modules.tank import Tank
from modules.score import Score
from modules.obstacle import Obstacle
from modules.shot import Shot
from config import *

pygame.init()
screen = pygame.display.set_mode(Constant['SCREEN_DIMENSION'])
pygame.display.set_caption("TANK PONG")

all_sprites = pygame.sprite.Group()
blue_tank = Tank(BLUE_TANK_SPRITE_SHEET, BLUE_TANK_X_POS, BLUE_TANK_Y_POS, 'red')
green_tank = Tank(GREEN_TANK_SPRITE_SHEET, GREEN_TANK_X_POS, GREEN_TANK_Y_POS, 'green')
obstacles = pygame.sprite.Group()
for sprite, pos in OBSTACLES.items():
    obstacles.add(Obstacle(sprite, pos[0], pos[1]))
all_sprites.add(blue_tank)
all_sprites.add(green_tank)
all_sprites.add(obstacles)
green_shots_group = []
blue_shots_group = []

green_already_thrown = False
blue_already_thrown = False
green_shot_limiter = TICK_SHOT_LIMITER
blue_shot_limiter = TICK_SHOT_LIMITER

green_tank_angle = 0
blue_tank_angle = 0
green_tank_sprite_change_limiter = 5
blue_tank_sprite_change_limiter = 5

class Game:
    def __init__(self):
        self.new_blue_shot = None
        self.new_green_shot = None
        self.current_screen = "start"
        self.draw = Draw(screen)
        self.score = Score()
        self.sound = Sound()

        self.all_sprites = pygame.sprite.Group()
        self.blue_tank = Tank(BLUE_TANK_SPRITE_SHEET, BLUE_TANK_X_POS, BLUE_TANK_Y_POS, 'red')
        self.green_tank = Tank(GREEN_TANK_SPRITE_SHEET, GREEN_TANK_X_POS, GREEN_TANK_Y_POS, 'green')
        self.obstacles = []
        for s, p in OBSTACLES.items():
            self.obstacles.append(Obstacle(s, p[0], p[1]))
        self.all_sprites.add(self.blue_tank)
        self.all_sprites.add(self.green_tank)
        self.all_sprites.add(self.obstacles)

        self.green_already_thrown = False
        self.blue_already_thrown = False
        self.green_shot_limiter = TICK_SHOT_LIMITER
        self.blue_shot_limiter = TICK_SHOT_LIMITER

        self.green_tank_angle = 0
        self.blue_tank_angle = 0
        self.green_tank_sprite_change_limiter = 5
        self.blue_tank_sprite_change_limiter = 5

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
        global green_already_thrown, blue_already_thrown, green_shot_limiter, blue_shot_limiter, green_tank_angle, \
            blue_tank_angle, green_tank_sprite_change_limiter, blue_tank_sprite_change_limiter, time_count

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.USEREVENT + 1:
                time_count -= 1
                print(time_count)
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
                if event.key == pygame.K_r:
                    self.current_screen = "start"
                    time_count = Constant['GAME_TIME']
                elif event.key == pygame.K_ESCAPE:
                    exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.green_tank.move_up(self.green_tank_angle)
        if keys[pygame.K_a]:
            self.green_tank.move_down(self.green_tank_angle)
        if keys[pygame.K_w]:
            if self.green_tank_sprite_change_limiter == 5:
                if self.green_tank_angle == 0:
                    self.green_tank_angle = 22
                else:
                    self.green_tank_angle -= 1
                self.green_tank.move_left(self.green_tank_angle)
                self.green_tank_sprite_change_limiter = 0
            self.green_tank_sprite_change_limiter += 1
        if keys[pygame.K_s]:
            if self.green_tank_sprite_change_limiter == 5:
                if self.green_tank_angle == 23:
                    self.green_tank_angle = 1
                else:
                    self.green_tank_angle += 1
                self.green_tank.move_right(self.green_tank_angle)
                self.green_tank_sprite_change_limiter = 0
            self.green_tank_sprite_change_limiter += 1
        if keys[pygame.K_LEFT]:
            self.blue_tank.move_up(self.blue_tank_angle)
        if keys[pygame.K_RIGHT]:
            self.blue_tank.move_down(self.blue_tank_angle)
        if keys[pygame.K_UP]:
            if self.blue_tank_sprite_change_limiter == 5:
                if self.blue_tank_angle == 23:
                    self.blue_tank_angle = 1
                else:
                    self.blue_tank_angle += 1
                self.blue_tank.move_right(self.blue_tank_angle)
                self.blue_tank_sprite_change_limiter = 0
            self.blue_tank_sprite_change_limiter += 1
        if keys[pygame.K_DOWN]:
            if self.blue_tank_sprite_change_limiter == 5:
                if self.blue_tank_angle == 0:
                    self.blue_tank_angle = 22
                else:
                    self.blue_tank_angle -= 1
                self.blue_tank.move_left(self.blue_tank_angle)
                self.blue_tank_sprite_change_limiter = 0
            self.blue_tank_sprite_change_limiter += 1
        if keys[pygame.K_g] and not self.green_already_thrown:
            new_green_shot = Shot(GREEN_SHOT_SPRITE, green_tank.rect.center, green_tank.shot_x_speed,
                                  green_tank.shot_y_speed)
            all_sprites.add(new_green_shot)
            green_shots_group.append(new_green_shot)
            green_shot_limiter = 0
            green_already_thrown = True
        if keys[pygame.K_l] and not self.blue_already_thrown:
            new_blue_shot = Shot(BLUE_SHOT_SPRITE, blue_tank.rect.center, blue_tank.shot_x_speed,
                                 blue_tank.shot_y_speed)
            all_sprites.add(new_blue_shot)
            blue_shots_group.append(new_blue_shot)
            blue_shot_limiter = 0
            blue_already_thrown = True

        for gs in green_shots_group:
            if pygame.sprite.collide_mask(gs, blue_tank):
                gs.kill()
                green_shots_group.remove(gs)
                self.score.update(1)
            for o in obstacles:
                if pygame.sprite.collide_mask(gs, o):
                    gs.collision_with_obstacle()

        for bs in blue_shots_group:
            if pygame.sprite.collide_mask(bs, green_tank):
                bs.kill()
                blue_shots_group.remove(bs)
                self.score.update(2)
            for o in obstacles:
                if pygame.sprite.collide_mask(bs, o):
                    bs.collision_with_obstacle()

        if time_count > 0:
            screen.fill(Color['RED'])
            self.sound.play_move(), self.sound.play_shot()
        self.draw.score_display(Constant['SCORE_1_POS'], 1, self.score.color_1)
        self.draw.score_display(Constant['SCORE_2_POS'], 2, self.score.color_2)
        self.all_sprites.update()
        self.all_sprites.draw(screen)

        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.update()
        if self.green_shot_limiter == TICK_SHOT_LIMITER:
            self.green_already_thrown = False
        if self.blue_shot_limiter == TICK_SHOT_LIMITER:
            self.blue_already_thrown = False
        self.green_shot_limiter += 1
        self.blue_shot_limiter += 1

    def change_screen(self):
        if self.current_screen == "start":
            self.start()
        elif self.current_screen == "main":
            self.main()
