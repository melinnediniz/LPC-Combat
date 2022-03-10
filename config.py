import pygame

class Sounds:
    throw_ball = ""


class Constants:
    FONT = "fonts/PoppkornRegular.ttf"
    SCREEN_DIMENSIONS = (1100, 720)
    CLOCK = 60
    SCORE_1_POS = (280, 5)
    SCORE_2_POS = (800, 5)


class Colors:
    BLACK = (0, 0, 0)
    RED = (154, 47, 14) # base
    YELLOW = (220, 176, 73) # obstacles
    GREEN = (149, 203, 89) # left player
    BLUE = (90, 100, 224) # right player
    AQUA = (45, 140, 110) # base start screen
    PINK = (229, 123, 219) #left player start screen
    WHITE = (234, 234, 234) # right player start screen


# ------ GLOBAL VARIABLES
game_loop = True
score_1 = 0
score_2 = 0


# ------- GLOBAL FUNCTIONS
pygame.init()
font = pygame.font.Font(Constants.FONT, 60)

def play_sound(file, vol):
    sound = pygame.mixer.Sound(file)
    sound.set_volume(vol)
    sound.play()


def display_score(surf, position, score):
    global score_1, score_2
    color = Colors.GREEN
    if score == 1:
        score = score_1
    elif score == 2:
        score = score_2
        color = Colors.BLUE
    score_surf = font.render(f'{score}', True, color)
    score_rect = score_surf.get_rect(topleft=position)
    surf.blit(score_surf, score_rect)


def update_score(score):
    global score_1, score_2
    if score == 1:
            score_1 +=1
    elif score == 2:
            score_2 += 1


def winner():
    winner = ''
    global score_1, score_2
    if score_2 > score_1:
        winner = 'PLAYER 2 WON'
    elif score_2 == score_1:
        winner = 'EMPATE'
    else:
        winner = 'PLAYER 1 WON'
    
    return winner


# time event
time_count = 0
timer = pygame.USEREVENT
pygame.time.set_timer(timer, 1000)
