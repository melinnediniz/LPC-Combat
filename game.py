import random
from modules.score import Score
from modules.sound import Sound
from modules.tank import Tank
from modules.obstacle import Obstacle
from modules.shot import Shot
from config import *

pygame.init()
screen = pygame.display.set_mode(Constant['SCREEN_DIMENSION'])
pygame.display.set_caption("TANK PONG")

score = Score(screen)
sound = Sound()

all_sprites = pygame.sprite.Group()
blue_tank = Tank(BLUE_TANK_SPRITE_SHEET, BLUE_TANK_X_POS, BLUE_TANK_Y_POS, 'red')
green_tank = Tank(GREEN_TANK_SPRITE_SHEET, GREEN_TANK_X_POS, GREEN_TANK_Y_POS, 'green')
obstacles = []
for sprite, pos in OBSTACLES.items():
    obstacles.append(Obstacle(sprite, pos[0], pos[1]))
all_sprites.add(blue_tank)
all_sprites.add(green_tank)
all_sprites.add(obstacles)

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

        screen.fill(Color['RED'])
        pygame.display.flip()

    def main(self):
        global green_already_thrown, blue_already_thrown, green_shot_limiter, blue_shot_limiter, green_tank_angle, \
            blue_tank_angle, green_tank_sprite_change_limiter, blue_tank_sprite_change_limiter, \
            timer_event, time_color_count, time_count

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == timer_event:
                time_count += 1
                time_color_count += 1
                print(f"T {time_count}")
                if time_count > Constant['GAME_TIME']:
                    if time_count == Constant['GAME_TIME'] + 5:
                        screen.fill(random.choice(list_of_colors))
                    elif time_count > Constant['GAME_TIME'] + 10:
                        screen.fill(random.choice(list_of_colors))
                        time_count = Constant['GAME_TIME'] + 5
                
                if time_color_count > Constant['GAME_TIME'] - 14:
                        if time_color_count == Constant['GAME_TIME'] - 13:
                            score.color_1, score.color_2 = Color['GREEN'], Color['BLUE']
                        elif time_color_count == Constant['GAME_TIME'] - 11: 
                            score.color_1, score.color_2 = Color['RED'], Color['RED']  
                            time_color_count = Constant['GAME_TIME'] - 14
                if time_count > Constant['GAME_TIME'] - 1:
                    green_tank.lock(), blue_tank.lock()
                    blue_already_thrown, green_already_thrown = True, True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.current_screen = "start"
                elif event.key == pygame.K_ESCAPE:
                    exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            green_tank.move_up(green_tank_angle)
        if keys[pygame.K_a]:
            green_tank.move_down(green_tank_angle)
        if keys[pygame.K_w]:
            if green_tank_sprite_change_limiter == 5:
                if green_tank_angle == 0:
                    green_tank_angle = 22
                else:
                    green_tank_angle -= 1
                green_tank.move_left(green_tank_angle)
                green_tank_sprite_change_limiter = 0
            green_tank_sprite_change_limiter += 1
        if keys[pygame.K_s]:
            if green_tank_sprite_change_limiter == 5:
                if green_tank_angle == 23:
                    green_tank_angle = 1
                else:
                    green_tank_angle += 1
                green_tank.move_right(green_tank_angle)
                green_tank_sprite_change_limiter = 0
            green_tank_sprite_change_limiter += 1
        if keys[pygame.K_LEFT]:
            blue_tank.move_up(blue_tank_angle)
        if keys[pygame.K_RIGHT]:
            blue_tank.move_down(blue_tank_angle)
        if keys[pygame.K_UP]:
            if blue_tank_sprite_change_limiter == 5:
                if blue_tank_angle == 23:
                    blue_tank_angle = 1
                else:
                    blue_tank_angle += 1
                blue_tank.move_right(blue_tank_angle)
                blue_tank_sprite_change_limiter = 0
            blue_tank_sprite_change_limiter += 1
        if keys[pygame.K_DOWN]:
            if blue_tank_sprite_change_limiter == 5:
                if blue_tank_angle == 0:
                    blue_tank_angle = 22
                else:
                    blue_tank_angle -= 1
                blue_tank.move_left(blue_tank_angle)
                blue_tank_sprite_change_limiter = 0
            blue_tank_sprite_change_limiter += 1
        if keys[pygame.K_g] and not green_already_thrown:
            new_green_shot = Shot(GREEN_SHOT_SPRITE, green_tank.rect.center, green_tank.shot_x_speed,
                                  green_tank.shot_y_speed)
            all_sprites.add(new_green_shot)
            green_shot_limiter = 0
            green_already_thrown = True
        if keys[pygame.K_l] and not blue_already_thrown:
            new_blue_shot = Shot(BLUE_SHOT_SPRITE, blue_tank.rect.center, blue_tank.shot_x_speed,
                                 blue_tank.shot_y_speed)
            all_sprites.add(new_blue_shot)
            blue_shot_limiter = 0
            blue_already_thrown = True

        if time_count < Constant['GAME_TIME']:
            screen.fill(Color['RED'])
            sound.play_move(), sound.play_shot()
        score.display(Constant['SCORE_1_POS'], 1, score.color_1)
        score.display(Constant['SCORE_2_POS'], 2, score.color_2)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.update()
        if green_shot_limiter == TICK_SHOT_LIMITER:
            green_already_thrown = False
        if blue_shot_limiter == TICK_SHOT_LIMITER:
            blue_already_thrown = False
        green_shot_limiter += 1
        blue_shot_limiter += 1

    def change_screen(self):
        if self.current_screen == "start":
            self.start()
        elif self.current_screen == "main":
            self.main()
