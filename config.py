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

BLUE_TANK_SPRITE_UP = 'sprites/blue_tank_up.png'
BLUE_TANK_SPRITE_DOWN = 'sprites/blue_tank_down.png'
BLUE_TANK_SPRITE_RIGHT = 'sprites/blue_tank_right.png'
BLUE_TANK_SPRITE_LEFT = 'sprites/blue_tank_left.png'
BLUE_TANK_SPRITE_DIAGONAL_TOP_RIGHT = 'sprites/blue_tank_diagonal_top_right.png'
BLUE_TANK_SPRITE_DIAGONAL_TOP_LEFT = 'sprites/blue_tank_diagonal_top_left.png'
BLUE_TANK_SPRITE_DIAGONAL_BOTTOM_RIGHT = 'sprites/blue_tank_diagonal_bottom_right.png'
BLUE_TANK_SPRITE_DIAGONAL_BOTTOM_LEFT = 'sprites/blue_tank_diagonal_bottom_left.png'
BLUE_TANK_X_POS = 932
BLUE_TANK_Y_POS = 396

GREEN_TANK_SPRITE_UP = 'sprites/green_tank_up.png'
GREEN_TANK_SPRITE_DOWN = 'sprites/green_tank_down.png'
GREEN_TANK_SPRITE_RIGHT = 'sprites/green_tank_right.png'
GREEN_TANK_SPRITE_LEFT = 'sprites/green_tank_left.png'
GREEN_TANK_SPRITE_DIAGONAL_TOP_RIGHT = 'sprites/green_tank_diagonal_top_right.png'
GREEN_TANK_SPRITE_DIAGONAL_TOP_LEFT = 'sprites/green_tank_diagonal_top_left.png'
GREEN_TANK_SPRITE_DIAGONAL_BOTTOM_RIGHT = 'sprites/green_tank_diagonal_bottom_right.png'
GREEN_TANK_SPRITE_DIAGONAL_BOTTOM_LEFT = 'sprites/green_tank_diagonal_bottom_left.png'
GREEN_TANK_X_POS = 90
GREEN_TANK_Y_POS = 396

BLUE_SHOT_SPRITE = 'sprites/blue_shot.png'
BLUE_SHOT_X_POS = 872
BLUE_SHOT_Y_POS = 396
GREEN_SHOT_SPRITE = 'sprites/green_shot.png'
GREEN_SHOT_X_POS = 150
GREEN_SHOT_Y_POS = 396

TIME_SHOT = 2


'''BLUE_SHOT_SPRITE = 'sprites/blue_shot.png'
BLUE_SHOT_X_POS = 
BLUE_SHOT_Y_POS = 
GREEN_SHOT_SPRITE = 'sprites/green_shot.png'
GREEN_SHOT_X_POS = 
GREEN_SHOT_Y_POS = '''

CENTER_BLOCK_SPRITE = 'sprites/center_block.png'
CENTER_RIGHT_BLOCK_X_POS = 740
CENTER_RIGHT_BLOCK_Y_POS = 396
CENTER_LEFT_BLOCK_X_POS = 276
CENTER_LEFT_BLOCK_Y_POS = 396
CENTER_TOP_BLOCK_X_POS = 509
CENTER_TOP_BLOCK_Y_POS = 116
CENTER_BOTTOM_BLOCK_X_POS = 509
CENTER_BOTTOM_BLOCK_Y_POS = 680

BLOCK_SPRITE = 'sprites/block.png'
BLOCK_TOP_RIGHT_X_POS = 831
BLOCK_TOP_RIGHT_Y_POS = 186
BLOCK_TOP_LEFT_X_POS = 189
BLOCK_TOP_LEFT_Y_POS = 186
BLOCK_BOTTOM_RIGHT_X_POS = 831
BLOCK_BOTTOM_RIGHT_Y_POS = 613
BLOCK_BOTTOM_LEFT_X_POS = 189
BLOCK_BOTTOM_LEFT_Y_POS = 613

RIGHT_UP_RECTANGLE_SPRITE = 'sprites/right_up_rectangle.png'
RIGHT_UP_RECTANGLE_X_POS = 614
RIGHT_UP_RECTANGLE_Y_POS = 250

RIGHT_DOWN_RECTANGLE_SPRITE = 'sprites/right_down_rectangle.png'
RIGHT_DOWN_RECTANGLE_X_POS = 614
RIGHT_DOWN_RECTANGLE_Y_POS = 549

LEFT_UP_RECTANGLE_SPRITE = 'sprites/left_up_rectangle.png'
LEFT_UP_RECTANGLE_X_POS = 400
LEFT_UP_RECTANGLE_Y_POS = 250

LEFT_DOWN_RECTANGLE_SPRITE = 'sprites/left_down_rectangle.png'
LEFT_DOWN_RECTANGLE_X_POS = 400
LEFT_DOWN_RECTANGLE_Y_POS = 549

RIGHT_GOAL_SPRITE = 'sprites/right_goal.png'
RIGHT_GOAL_X_POS = 856
RIGHT_GOAL_Y_POS = 396

LEFT_GOAL_SPRITE = 'sprites/left_goal.png'
LEFT_GOAL_X_POS = 164
LEFT_GOAL_Y_POS = 396

pygame.init()
class Sounds:
    throw_ball = pygame.mixer.Sound('sound/shot.ogg')
    move_tank = pygame.mixer.Sound("sound/move.ogg")
    flip_tank = pygame.mixer.Sound("sound/flip.wav")
    kill = pygame.mixer.Sound("sound/kill.wav")



class Constant:
    FONT = "fonts/Megafont.ttf"
    SCREEN_DIMENSIONS = (1022, 738)
    CLOCK = 60
    SCORE_1_POS = (280, 5)
    SCORE_2_POS = (800, 5)
    GAME_TIME = 300
    MIN_LIVES = 0
    icon = pygame.image.load('sprites/icon.png')


class Color:
    BLACK = (0, 0, 0)
    RED = (154, 47, 14) # base
    YELLOW = (220, 176, 73) # obstacles
    GREEN = (149, 203, 89) # left player
    BLUE = (90, 100, 224) # right player
    AQUA = (45, 140, 110) # base start screen
    PINK = (229, 123, 219) #left player start screen
    WHITE = (234, 234, 234) # right player start screen

    DARK_RED = (112, 16, 15)
    DARK_GREEN = (10, 121, 0)
    CLAY = (181, 146, 90)


list_colors = [Color.AQUA, Color.PINK, Color.DARK_RED, Color.DARK_GREEN, Color.CLAY]

# ------ GLOBAL VARIABLES
game_loop = True
score_1 = 0
score_2 = 0
color_1 = Color.GREEN
color_2 = Color.BLUE

# ------- GLOBAL FUNCTIONS
font = pygame.font.Font(Constant.FONT, 60)

# time event
time_count = 0
time_color_count = 0
timer = pygame.USEREVENT
pygame.time.set_timer(timer, 1000)


pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 512)
green_tank_channel = pygame.mixer.Channel(0)
blue_tank_channel = pygame.mixer.Channel(1)
kill_channel = pygame.mixer.Channel(2)


def move_tanks_sound():
    global green_tank_channel, blue_tank_channel
    blue_tank_channel.set_volume(0.5)
    key = pygame.key.get_pressed()
    if not green_tank_channel.get_busy():
        if key[pygame.K_d]:
            green_tank_channel.play(Sounds.move_tank)
        if key[pygame.K_s]:
            green_tank_channel.play(Sounds.move_tank)
        if key[pygame.K_a]:
            green_tank_channel.play(Sounds.move_tank)
        if key[pygame.K_w]:
            green_tank_channel.play(Sounds.move_tank)
    elif green_tank_channel.get_busy():
        if not key[pygame.K_d] and (not key[pygame.K_s]) and (not key[pygame.K_a]) and (not key[pygame.K_w]):
            green_tank_channel.stop()

    if not blue_tank_channel.get_busy():
        if key[pygame.K_LEFT]:
            blue_tank_channel.play(Sounds.move_tank)
        if key[pygame.K_RIGHT]:
            blue_tank_channel.play(Sounds.move_tank)
        if key[pygame.K_UP]:
            blue_tank_channel.play(Sounds.move_tank)
        if key[pygame.K_DOWN]:
            blue_tank_channel.play(Sounds.move_tank)
    elif blue_tank_channel.get_busy():
        if not key[pygame.K_LEFT] and (not key[pygame.K_RIGHT]) and (not key[pygame.K_UP]) and (not key[pygame.K_DOWN]):
            blue_tank_channel.stop()

def kill_sound():
    global kill_channel
    kill_channel.set_volume(0.3)
    
    if not kill_channel.get_busy():
        kill_channel.play(Sounds.kill)
    elif kill_channel.get_busy():
        kill_channel.stop()

                
def display_score(surf, position, score, color):
    global score_1, score_2
    if score == 1:
        score = score_1
    elif score == 2:
        score = score_2
    score_surf = font.render(f'{score}', True, color)
    score_rect = score_surf.get_rect(topleft=position)
    surf.blit(score_surf, score_rect)


def update_score(score):
    global score_1, score_2
    if score == 1:
            score_1 +=1
    elif score == 2:
            score_2 += 1

def reset_score():
    global score_1, score_2
    score_1 = 0
    score_2 = 0

