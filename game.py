import random
from modules.score import Score
from modules.sound import Sound
from modules.tank2 import Tank
from modules.obstacle import Obstacle
from modules.shot import Shot
from config import *

pygame.init()
screen = pygame.display.set_mode(Constant['SCREEN_DIMENSION'])
pygame.display.set_caption("TANK PONG")


class Game:
    def __init__(self):
        self.new_blue_shot = None
        self.new_green_shot = None
        self.current_screen = "start"
        self.score = Score(screen)
        self.sound = Sound()

        self.all_sprites = pygame.sprite.Group()
        
        self.blue_tank = Tank(BLUE_TANK_X_POS, BLUE_TANK_Y_POS, 'blue')
        self.green_tank = Tank(GREEN_TANK_X_POS, GREEN_TANK_Y_POS, 'green')
        
        self.obstacles = []
        for sprite, pos in OBSTACLES.items():
            self.obstacles.append(Obstacle(sprite, pos[0], pos[1]))
        #self.all_sprites.add(self.blue_tank)
        #self.all_sprites.add(self.green_tank)
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
        pygame.display.flip()

    def main(self):
        global time_count

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
                if event.key == pygame.K_w:
                    self.green_tank.rotate()
                if event.key == pygame.K_UP:
                    self.blue_tank.rotate()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                self.green_tank.move_up()
            if keys[pygame.K_LEFT]:
                self.blue_tank.move_up()

        
        if time_count > 0:
            screen.fill(Color['RED'])
            self.sound.play_move(), self.sound.play_shot()
        self.score.display(Constant['SCORE_1_POS'], 1, self.score.color_1)
        self.score.display(Constant['SCORE_2_POS'], 2, self.score.color_2)
        self.all_sprites.update()
        self.all_sprites.draw(screen)
        self.green_tank.draw(screen), self.blue_tank.draw(screen)

        pygame.display.flip()

    def change_screen(self):
        if self.current_screen == "start":
            self.start()
        elif self.current_screen == "main":
            self.main()
