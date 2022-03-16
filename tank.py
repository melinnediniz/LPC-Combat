import pygame


class Tank(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x_pos, y_pos, color):
        super().__init__()
        self.sprite_sheet = sprite_sheet
        self.image = self.sprite_sheet[0]
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.x_speed = 0
        self.y_speed = 0
        self.color = color
        if self.color == 'green':
            self.shot_x_speed = 6
        else:
            self.shot_x_speed = -6
        self.shot_y_speed = 0
        self.previous_direction = 'up'

    def move_up(self, angle):
        self.previous_direction = 'up'
        if self.color == 'green':
            if angle == 0:
                self.rect.x += 3
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = 0
            elif angle == 1:
                self.rect.x += 3
                self.rect.y += 1
                self.shot_y_speed = 1 * 2
                self.shot_x_speed = 3 * 2
            elif angle == 2:
                self.rect.x += 3
                self.rect.y += 2
                self.shot_y_speed = 2 * 2
                self.shot_x_speed = 3 * 2
            elif angle == 3:
                self.rect.x += 3
                self.rect.y += 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = 3 * 2
            elif angle == 4:
                self.rect.x += 2
                self.rect.y += 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = 2 * 2
            elif angle == 5:
                self.rect.x += 1
                self.rect.y += 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = 1 * 2
            elif angle == 6:
                self.rect.y += 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = 0
            elif angle == 7:
                self.rect.x -= 1
                self.rect.y += 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = -1 * 2
            elif angle == 8:
                self.rect.x -= 2
                self.rect.y += 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = -2 * 2
            elif angle == 9:
                self.rect.x -= 3
                self.rect.y += 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = -3 * 2
            elif angle == 10:
                self.rect.x -= 3
                self.rect.y += 2
                self.shot_y_speed = 2 * 2
                self.shot_x_speed = -3 * 2
            elif angle == 11:
                self.rect.x -= 3
                self.rect.y += 1
                self.shot_y_speed = 1 * 2
                self.shot_x_speed = -3 * 2
            elif angle == 12:
                self.rect.x -= 3
                self.shot_y_speed = 0
                self.shot_x_speed -= 3 * 2
            elif angle == 13:
                self.rect.x -= 3
                self.rect.y -= 1
                self.shot_y_speed = -1 * 2
                self.shot_x_speed = -3 * 2
            elif angle == 14:
                self.rect.x -= 3
                self.rect.y -= 2
                self.shot_y_speed = -2 * 2
                self.shot_x_speed = -3 * 2
            elif angle == 15:
                self.rect.x -= 3
                self.rect.y -= 3
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = -3 * 2
            elif angle == 16:
                self.rect.x -= 2
                self.rect.y -= 3
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = -2 * 2
            elif angle == 17:
                self.rect.x -= 1
                self.rect.y -= 3
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = -1 * 2
            elif angle == 18:
                self.rect.y -= 3
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = 0
            elif angle == 19:
                self.rect.y -= 3
                self.rect.x += 1
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = 1 * 2
            elif angle == 20:
                self.rect.y -= 3
                self.rect.x += 2
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = 2 * 2
            elif angle == 21:
                self.rect.y -= 3
                self.rect.x += 3
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = 3 * 2
            elif angle == 22:
                self.rect.y -= 2
                self.rect.x += 3
                self.shot_y_speed = -2 * 2
                self.shot_x_speed = 3 * 2
            elif angle == 23:
                self.rect.y -= 1
                self.rect.x += 3
                self.shot_y_speed = -1 * 2
                self.shot_x_speed = 3 * 2
        else:
            if angle == 0:
                self.rect.x -= 3
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = 0
            elif angle == 1:
                self.rect.x -= 3
                self.rect.y -= 1
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = -1 * 2
            elif angle == 2:
                self.rect.x -= 3
                self.rect.y -= 2
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = -2 * 2
            elif angle == 3:
                self.rect.x -= 3
                self.rect.y -= 3
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = -3 * 2
            elif angle == 4:
                self.rect.x -= 2
                self.rect.y -= 3
                self.shot_x_speed = -2 * 2
                self.shot_y_speed = -3 * 2
            elif angle == 5:
                self.rect.x -= 1
                self.rect.y -= 3
                self.shot_x_speed = -1 * 2
                self.shot_y_speed = -3 * 2
            elif angle == 6:
                self.rect.y -= 3
                self.shot_x_speed = 0
                self.shot_y_speed = -3 * 2
            elif angle == 7:
                self.rect.x += 1
                self.rect.y -= 3
                self.shot_x_speed = 1 * 2
                self.shot_y_speed = -3 * 2
            elif angle == 8:
                self.rect.x += 2
                self.rect.y -= 3
                self.shot_x_speed = 2 * 2
                self.shot_y_speed = -3 * 2
            elif angle == 9:
                self.rect.x += 3
                self.rect.y -= 3
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = -3 * 2
            elif angle == 10:
                self.rect.x += 3
                self.rect.y -= 2
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = -2 * 2
            elif angle == 11:
                self.rect.x += 3
                self.rect.y -= 1
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = -1 * 2
            elif angle == 12:
                self.rect.x += 3
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = 0
            elif angle == 13:
                self.rect.x += 3
                self.rect.y += 1
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = 1 * 2
            elif angle == 14:
                self.rect.x += 3
                self.rect.y += 2
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = 2 * 2
            elif angle == 15:
                self.rect.x += 3
                self.rect.y += 3
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = 3 * 2
            elif angle == 16:
                self.rect.x += 2
                self.rect.y += 3
                self.shot_x_speed = 2 * 2
                self.shot_y_speed = 3 * 2
            elif angle == 17:
                self.rect.x += 1
                self.rect.y += 3
                self.shot_x_speed = 1 * 2
                self.shot_y_speed = 3 * 2
            elif angle == 18:
                self.rect.y += 3
                self.shot_x_speed = 0
                self.shot_y_speed = 3 * 2
            elif angle == 19:
                self.rect.y += 3
                self.rect.x -= 1
                self.shot_x_speed = -1 * 2
                self.shot_y_speed = 3 * 2
            elif angle == 20:
                self.rect.y += 3
                self.rect.x -= 2
                self.shot_x_speed = -2 * 2
                self.shot_y_speed = 3 * 2
            elif angle == 21:
                self.rect.y += 3
                self.rect.x -= 3
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = 3 * 2
            elif angle == 22:
                self.rect.y += 2
                self.rect.x -= 3
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = 2 * 2
            elif angle == 23:
                self.rect.y += 1
                self.rect.x -= 3
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = 1 * 2

    def move_down(self, angle):
        self.previous_direction = 'down'
        if self.color == 'green':
            if angle == 0:
                self.rect.x -= 3
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = 0
            elif angle == 1:
                self.rect.x -= 3
                self.rect.y -= 1
                self.shot_y_speed = 1 * 2
                self.shot_x_speed = 3 * 2
            elif angle == 2:
                self.rect.x -= 3
                self.rect.y -= 2
                self.shot_y_speed = 2 * 2
                self.shot_x_speed = 3 * 2
            elif angle == 3:
                self.rect.x -= 3
                self.rect.y -= 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = 3 * 2
            elif angle == 4:
                self.rect.x -= 2
                self.rect.y -= 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = 2 * 2
            elif angle == 5:
                self.rect.x -= 1
                self.rect.y -= 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = 1 * 2
            elif angle == 6:
                self.rect.y -= 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = 0
            elif angle == 7:
                self.rect.x += 1
                self.rect.y -= 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = -1 * 2
            elif angle == 8:
                self.rect.x += 2
                self.rect.y -= 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = -2 * 2
            elif angle == 9:
                self.rect.x += 3
                self.rect.y -= 3
                self.shot_y_speed = 3 * 2
                self.shot_x_speed = -3 * 2
            elif angle == 10:
                self.rect.x += 3
                self.rect.y -= 2
                self.shot_y_speed = 2 * 2
                self.shot_x_speed = -3 * 2
            elif angle == 11:
                self.rect.x += 3
                self.rect.y -= 1
                self.shot_y_speed = 1 * 2
                self.shot_x_speed = -3 * 2
            elif angle == 12:
                self.rect.x += 3
                self.shot_y_speed = 0
                self.shot_x_speed -= 3 * 2
            elif angle == 13:
                self.rect.x += 3
                self.rect.y += 1
                self.shot_y_speed = -1 * 2
                self.shot_x_speed = -3 * 2
            elif angle == 14:
                self.rect.x += 3
                self.rect.y += 2
                self.shot_y_speed = -2 * 2
                self.shot_x_speed = -3 * 2
            elif angle == 15:
                self.rect.x += 3
                self.rect.y += 3
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = -3 * 2
            elif angle == 16:
                self.rect.x += 2
                self.rect.y += 3
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = -2 * 2
            elif angle == 17:
                self.rect.x += 1
                self.rect.y += 3
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = -1 * 2
            elif angle == 18:
                self.rect.y += 3
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = 0
            elif angle == 19:
                self.rect.y += 3
                self.rect.x -= 1
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = 1 * 2
            elif angle == 20:
                self.rect.y += 3
                self.rect.x -= 2
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = 2 * 2
            elif angle == 21:
                self.rect.y += 3
                self.rect.x -= 3
                self.shot_y_speed = -3 * 2
                self.shot_x_speed = 3 * 2
            elif angle == 22:
                self.rect.y += 2
                self.rect.x -= 3
                self.shot_y_speed = -2 * 2
                self.shot_x_speed = 3 * 2
            elif angle == 23:
                self.rect.y += 1
                self.rect.x -= 3
                self.shot_y_speed = -1 * 2
                self.shot_x_speed = 3 * 2
        else:
            if angle == 0:
                self.rect.x += 3
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = 0
            elif angle == 1:
                self.rect.x += 3
                self.rect.y += 1
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = -1 * 2
            elif angle == 2:
                self.rect.x += 3
                self.rect.y += 2
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = -2 * 2
            elif angle == 3:
                self.rect.x += 3
                self.rect.y += 3
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = -3 * 2
            elif angle == 4:
                self.rect.x += 2
                self.rect.y += 3
                self.shot_x_speed = -2 * 2
                self.shot_y_speed = -3 * 2
            elif angle == 5:
                self.rect.x += 1
                self.rect.y += 3
                self.shot_x_speed = -1 * 2
                self.shot_y_speed = -3 * 2
            elif angle == 6:
                self.rect.y += 3
                self.shot_x_speed = 0
                self.shot_y_speed = -3 * 2
            elif angle == 7:
                self.rect.x -= 1
                self.rect.y += 3
                self.shot_x_speed = 1 * 2
                self.shot_y_speed = -3 * 2
            elif angle == 8:
                self.rect.x -= 2
                self.rect.y += 3
                self.shot_x_speed = 2 * 2
                self.shot_y_speed = -3 * 2
            elif angle == 9:
                self.rect.x -= 3
                self.rect.y += 3
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = -3 * 2
            elif angle == 10:
                self.rect.x -= 3
                self.rect.y += 2
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = -2 * 2
            elif angle == 11:
                self.rect.x -= 3
                self.rect.y += 1
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = -1 * 2
            elif angle == 12:
                self.rect.x -= 3
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = 0
            elif angle == 13:
                self.rect.x -= 3
                self.rect.y -= 1
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = 1 * 2
            elif angle == 14:
                self.rect.x -= 3
                self.rect.y -= 2
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = 2 * 2
            elif angle == 15:
                self.rect.x -= 3
                self.rect.y -= 3
                self.shot_x_speed = 3 * 2
                self.shot_y_speed = 3 * 2
            elif angle == 16:
                self.rect.x -= 2
                self.rect.y -= 3
                self.shot_x_speed = 2 * 2
                self.shot_y_speed = 3 * 2
            elif angle == 17:
                self.rect.x -= 1
                self.rect.y -= 3
                self.shot_x_speed = 1 * 2
                self.shot_y_speed = 3 * 2
            elif angle == 18:
                self.rect.y -= 3
                self.shot_x_speed = 0
                self.shot_y_speed = 3 * 2
            elif angle == 19:
                self.rect.y -= 3
                self.rect.x += 1
                self.shot_x_speed = -1 * 2
                self.shot_y_speed = 3 * 2
            elif angle == 20:
                self.rect.y -= 3
                self.rect.x += 2
                self.shot_x_speed = -2 * 2
                self.shot_y_speed = 3 * 2
            elif angle == 21:
                self.rect.y -= 3
                self.rect.x += 3
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = 3 * 2
            elif angle == 22:
                self.rect.y -= 2
                self.rect.x += 3
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = 2 * 2
            elif angle == 23:
                self.rect.y -= 1
                self.rect.x += 3
                self.shot_x_speed = -3 * 2
                self.shot_y_speed = 1 * 2

    def move_right(self, angle):
        self.image = self.sprite_sheet[angle]
        if self.previous_direction == 'up':
            self.move_up(angle)
        else:
            self.move_down(angle)

    def move_left(self, angle):
        self.image = self.sprite_sheet[angle]
        if self.previous_direction == 'up':
            self.move_up(angle)
        else:
            self.move_down(angle)

    def turn_off_speed(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.rect.x += self.x_speed
        if self.x_speed != 0:
            self.shot_x_speed = self.x_speed * 3
        self.rect.y += self.y_speed
        if self.y_speed != 0:
            self.shot_y_speed = self.y_speed * 3
        self.turn_off_speed()
