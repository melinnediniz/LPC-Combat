import pygame, sys
from config import GREEN_TANK_SPRITE_UP


class Tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(GREEN_TANK_SPRITE_UP)
        self.rect = self.image.get_rect(center=(250, 250))


pygame.init()
clock = pygame.time.Clock()
FPS = 60
pygame.display.set_caption('Rotation Test')
screen = pygame.display.set_mode((500, 500), 0, 23)
angle = 0
tank = Tank()
scr_half_width = int(screen.get_width() / 2)
scr_half_height = int(screen.get_height() / 2)
tank_half_widht = int(tank.image.get_width() / 2)
tank_half_height = int(tank.image.get_height() / 2)


def blit_rotate(image, pos, origin_pos, angl):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - origin_pos[0], pos[1] - origin_pos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angl)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angl)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    return rotated_image, rotated_image_rect


while True:

    screen.fill((0, 0, 0))

    tank_image = tank.image
    tank_rect = tank.rect
    w, h = tank_image.get_size()
    pos = (screen.get_width()/2, screen.get_height()/2)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        angle -= 3
        tank_image, tank_rect = blit_rotate(tank_image, pos, (w/2, h/2), angle)
    screen.blit(tank_image, tank_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(FPS)
