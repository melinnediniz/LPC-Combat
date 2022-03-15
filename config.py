import pygame

TICK_SHOT_LIMITER = 15

TOP_AND_BOTTOM_RECT_WIDTH = 1022
TOP_AND_BOTTOM_RECT_HEIGHT = 40
RIGHT_AND_LEFT_RECT_WIDTH = 40
RIGHT_AND_LEFT_RECT_HEIGHT = 700
TOP_AND_BOTTOM_RECT_X_POS = 0
TOP_RECT_Y_POS = 55
BOTTOM_RECT_Y_POS = 698
RIGHT_RECT_X_POS = 0
LEFT_RECT_X_POS = 982
RIGHT_AND_LEFT_RECT_Y_POS = 55

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
             'sprites/right_goal.png': (856, 396), 'sprites/left_goal.png': (164, 396)}


class Sounds:
    throw_ball = ""
    move_tank = "sound/move_tank.wav"
    flip_tank = "sound/flip_tank.wav"


class Constant:
    FONT = "fonts/PoppkornRegular.ttf"
    SCREEN_DIMENSIONS = (1022, 738)
    CLOCK = 60
    SCORE_1_POS = (280, 5)
    SCORE_2_POS = (800, 5)


class Color:
    BLACK = (0, 0, 0)
    RED = (154, 47, 14)  # base
    YELLOW = (220, 176, 73)  # obstacles
    GREEN = (149, 203, 89)  # left player
    BLUE = (90, 100, 224)  # right player
    AQUA = (45, 140, 110)  # base start screen
    PINK = (229, 123, 219)  # left player start screen
    WHITE = (234, 234, 234)  # right player start screen


# ------ GLOBAL VARIABLES
game_loop = True
score_1 = 0
score_2 = 0

# ------- GLOBAL FUNCTIONS
pygame.init()
font = pygame.font.Font(Constant.FONT, 60)


def play_sound(file, vol):
    sound = pygame.mixer.Sound(file)
    sound.set_volume(vol)
    sound.play()


def display_score(surf, position, score):
    global score_1, score_2
    color = Color.GREEN
    if score == 1:
        score = score_1
    elif score == 2:
        score = score_2
        color = Color.BLUE
    score_surf = font.render(f'{score}', True, color)
    score_rect = score_surf.get_rect(topleft=position)
    surf.blit(score_surf, score_rect)


def update_score(score):
    global score_1, score_2
    if score == 1:
        score_1 += 1
    elif score == 2:
        score_2 += 1


def winner():
    global score_1, score_2
    if score_2 > score_1:
        winner = 'PLAYER 2 WON'
    elif score_2 == score_1:
        winner = 'DRAW'
    else:
        winner = 'PLAYER 1 WON'

    return winner
