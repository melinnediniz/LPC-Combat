from itertools import count
import random
from tanks import *
from scenario import *
from shots import *
from config import *
from config import Color, Constant, display_score, update_score, reset_score
from config import timer, time_count, list_colors, time_color_count, color_1, color_2

pygame.init()
screen = pygame.display.set_mode(Constant.SCREEN_DIMENSIONS)
pygame.display.set_icon(Constant.icon)
pygame.display.set_caption("TANK PONG")

all_sprites = pygame.sprite.Group()
blue_tank = BlueTank()
green_tank = GreenTank()
center_right_block = CenterBlock(CENTER_RIGHT_BLOCK_X_POS, CENTER_RIGHT_BLOCK_Y_POS)
center_left_block = CenterBlock(CENTER_LEFT_BLOCK_X_POS, CENTER_LEFT_BLOCK_Y_POS)
center_top_block = CenterBlock(CENTER_TOP_BLOCK_X_POS, CENTER_TOP_BLOCK_Y_POS)
center_bottom_block = CenterBlock(CENTER_BOTTOM_BLOCK_X_POS, CENTER_BOTTOM_BLOCK_Y_POS)
top_right_block = Block(BLOCK_TOP_RIGHT_X_POS, BLOCK_TOP_RIGHT_Y_POS)
top_left_block = Block(BLOCK_TOP_LEFT_X_POS, BLOCK_TOP_LEFT_Y_POS)
bottom_right_block = Block(BLOCK_BOTTOM_RIGHT_X_POS, BLOCK_BOTTOM_RIGHT_Y_POS)
bottom_left_block = Block(BLOCK_BOTTOM_LEFT_X_POS, BLOCK_BOTTOM_LEFT_Y_POS)
right_up_rectangle = RightUpRectangle(RIGHT_UP_RECTANGLE_X_POS, RIGHT_UP_RECTANGLE_Y_POS)
right_down_rectangle = RightDownRectangle(RIGHT_DOWN_RECTANGLE_X_POS, RIGHT_DOWN_RECTANGLE_Y_POS)
left_up_rectangle = LeftUpRectangle(LEFT_UP_RECTANGLE_X_POS, LEFT_UP_RECTANGLE_Y_POS)
left_down_rectangle = LeftDownRectangle(LEFT_DOWN_RECTANGLE_X_POS, LEFT_DOWN_RECTANGLE_Y_POS)
right_goal = RightGoal(RIGHT_GOAL_X_POS, RIGHT_GOAL_Y_POS)
left_goal = LeftGoal(LEFT_GOAL_X_POS, LEFT_GOAL_Y_POS)
top_rect = pygame.Rect(TOP_AND_BOTTOM_RECT_X_POS, TOP_RECT_Y_POS, TOP_AND_BOTTOM_RECT_WIDTH, TOP_AND_BOTTOM_RECT_HEIGHT)
bottom_rect = pygame.Rect(TOP_AND_BOTTOM_RECT_X_POS, BOTTOM_RECT_Y_POS, TOP_AND_BOTTOM_RECT_WIDTH,
                          TOP_AND_BOTTOM_RECT_HEIGHT)
right_rect = pygame.Rect(RIGHT_RECT_X_POS, RIGHT_AND_LEFT_RECT_Y_POS, RIGHT_AND_LEFT_RECT_WIDTH,
                         RIGHT_AND_LEFT_RECT_HEIGHT)
left_rect = pygame.Rect(LEFT_RECT_X_POS, RIGHT_AND_LEFT_RECT_Y_POS, RIGHT_AND_LEFT_RECT_WIDTH,
                        RIGHT_AND_LEFT_RECT_HEIGHT)
all_sprites.add(blue_tank)
all_sprites.add(green_tank)
all_sprites.add(center_right_block)
all_sprites.add(center_left_block)
all_sprites.add(center_top_block)
all_sprites.add(center_bottom_block)
all_sprites.add(top_right_block)
all_sprites.add(top_left_block)
all_sprites.add(bottom_right_block)
all_sprites.add(bottom_left_block)
all_sprites.add(right_up_rectangle)
all_sprites.add(right_down_rectangle)
all_sprites.add(left_up_rectangle)
all_sprites.add(left_down_rectangle)
all_sprites.add(right_goal)
all_sprites.add(left_goal)

green_already_thrown = False
blue_already_thrown = False
green_shot_limiter = TICK_SHOT_LIMITER
blue_shot_limiter = TICK_SHOT_LIMITER


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

        screen.fill(Color.GREEN)
        pygame.display.flip()


    def main(self):
        global green_already_thrown, blue_already_thrown, green_shot_limiter, blue_shot_limiter
        global time_color_count, color_1, color_2, time_count, score_1, score_2
        for event in pygame.event.get():
            if event.type == timer:
                time_count += 1
                time_color_count += 1
                print(f"T {time_count}")
                if time_count > Constant.GAME_TIME:
                    if time_count == Constant.GAME_TIME + 5:
                        screen.fill(random.choice(list_colors))
                    elif time_count > Constant.GAME_TIME + 10:
                        screen.fill(random.choice(list_colors))
                        time_count = Constant.GAME_TIME + 5
                elif time_count < Constant.GAME_TIME:
                    if time_color_count > Constant.GAME_TIME - 13:
                        if time_color_count == Constant.GAME_TIME - 13:
                            color_1, color_2 = Color.GREEN, Color.BLUE
                        elif time_color_count == Constant.GAME_TIME - 11: 
                            color_1, color_2 = Color.RED, Color.RED  
                            time_color_count = Constant.GAME_TIME - 13
            if time_count > Constant.GAME_TIME - 1:
                blue_tank.lock(), green_tank.lock()


            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif event.key == pygame.K_r:
                    reset_score()
                    time_color_count = 0
                    time_count = 0
                    blue_tank.reset(), green_tank.reset()
                    print(blue_tank.movement)
                    self.current_screen = "start"

        keys = pygame.key.get_pressed()
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
        if keys[pygame.K_g] and not green_already_thrown:
            new_green_shot = GreenShot(green_tank.rect.x + 22, green_tank.rect.y + 22,
                                       green_tank.previous_x_speed, green_tank.previous_y_speed)
            all_sprites.add(new_green_shot)
            green_shot_limiter = 0
            green_already_thrown = True
        if keys[pygame.K_l] and not blue_already_thrown:
            new_blue_shot = BlueShot(blue_tank.rect.x + 22, blue_tank.rect.y + 22,
                                     blue_tank.previous_x_speed, blue_tank.previous_y_speed)
            all_sprites.add(new_blue_shot)
            blue_shot_limiter = 0
            blue_already_thrown = True

        if time_count < Constant.GAME_TIME:
            screen.fill(Color.RED)
        display_score(screen, Constant.SCORE_1_POS, 1, color_1)
        display_score(screen, Constant.SCORE_2_POS, 2, color_2)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.draw.rect(screen, Color().YELLOW, top_rect)
        pygame.draw.rect(screen, Color().YELLOW, bottom_rect)
        pygame.draw.rect(screen, Color().YELLOW, right_rect)
        pygame.draw.rect(screen, Color().YELLOW, left_rect)
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