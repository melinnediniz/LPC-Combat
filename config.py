import pygame

pygame.init()
game_loop = True

Color = {
    "BLACK": (0, 0, 0),
    "RED": (154, 47, 14),
    "YELLOW": (220, 176, 73),
    "GREEN": (149, 203, 89),
    "BLUE": (90, 100, 224),
    "AQUA": (45, 140, 110),
    "PINK": (229, 123, 219),
    "WHITE": (234, 234, 234),
    "DARK_RED": (112, 16, 15),
    "DARK_GREEN": (10, 121, 0),
    "CLAY": (181, 146, 90)
}

list_of_colors = [Color['AQUA'], Color['PINK'], Color['DARK_RED'], Color['DARK_GREEN'], Color['CLAY']]

Constant = {
    "FONT": "fonts/Megafont.ttf", 
    "FONT_2": "fonts/G7StarForce.ttf", 
    "SCREEN_DIMENSION": (1022, 738), 
    "CLOCK": 60,
    "SCORE_1_POS": (250, 5),
    "SCORE_2_POS": (780, 5),
    "GAME_TIME": 41
}


TICK_SHOT_LIMITER = 15

BLUE_TANK_SPRITE_SHEET = []
for i in range(0, 360, 15):
    BLUE_TANK_SPRITE_SHEET.append(pygame.image.load(f'sprites/blue_tank/{i}.png'))
BLUE_TANK_X_POS = 932
BLUE_TANK_Y_POS = 396

GREEN_TANK_SPRITE_SHEET = []
for i in range(0, 360, 15):
    GREEN_TANK_SPRITE_SHEET.append(pygame.image.load(f'sprites/green_tank/{i}.png'))
GREEN_TANK_X_POS = 90
GREEN_TANK_Y_POS = 396

BLUE_SHOT_SPRITE = 'sprites/blue_shot.png'
BLUE_SHOT_X_POS = 872
BLUE_SHOT_Y_POS = 396
GREEN_SHOT_SPRITE = 'sprites/green_shot.png'
GREEN_SHOT_X_POS = 150
GREEN_SHOT_Y_POS = 396

# obstacle image file path: obstacle (x, y) positions
OBSTACLES = {'sprites/right_block.png': (740, 396), 'sprites/left_block.png': (276, 396),
             'sprites/top_block.png': (509, 116), 'sprites/bottom_block.png': (509, 680),
             'sprites/top_right_rectangle.png': (831, 186), 'sprites/top_left_rectangle.png': (189, 186),
             'sprites/bottom_right_rectangle.png': (831, 613), 'sprites/bottom_left_rectangle.png': (189, 613),
             'sprites/top_right_stick.png': (614, 250), 'sprites/bottom_right_stick.png': (614, 549),
             'sprites/top_left_stick.png': (400, 250), 'sprites/bottom_left_stick.png': (400, 549),
             'sprites/right_goal.png': (856, 396), 'sprites/left_goal.png': (164, 396),
             'sprites/top_wall.png': (510, 73), 'sprites/bottom_wall.png': (510, 723),
             'sprites/right_wall.png': (20, 410), 'sprites/left_wall.png': (1002, 410)}

# time event
time_count = Constant['GAME_TIME']
time_color_count = 0
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
