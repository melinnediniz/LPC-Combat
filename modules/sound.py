import pygame
from config import Sounds
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)


class Sound:
    def __init__(self):
        self.shot = Sounds["shot"]
        self.move = Sounds["move"]
        self.flip = Sounds["flip"]
        self.kill = ""  # pygame.mixer.Sound("sound/kill.wav")
        self.green_tank_channel = pygame.mixer.Channel(0)
        self.blue_tank_channel = pygame.mixer.Channel(1)
        self.shot_channel = pygame.mixer.Channel(2)
        self.flip_channel = pygame.mixer.Channel(3)

    def play_move(self):
        self.blue_tank_channel.set_volume(0.5), self.green_tank_channel.set_volume(0.5)
        key = pygame.key.get_pressed()
        if not self.green_tank_channel.get_busy() and not self.flip_channel.get_busy():
            if key[pygame.K_d] or key[pygame.K_a]:
                self.green_tank_channel.play(self.move)
        elif self.green_tank_channel.get_busy():
            if not key[pygame.K_d] and not key[pygame.K_a]:
                self.green_tank_channel.stop()

        if not self.blue_tank_channel.get_busy() and not self.flip_channel.get_busy():
            if key[pygame.K_j] or key[pygame.K_l]:
                self.blue_tank_channel.play(self.move)
        elif self.blue_tank_channel.get_busy():
            if not key[pygame.K_j] and not key[pygame.K_l]:
                self.blue_tank_channel.stop()

    def play_flip(self):
        self.flip_channel.set_volume(0.1)
        key = pygame.key.get_pressed()
        if not self.flip_channel.get_busy():
            if key[pygame.K_w] or key[pygame.K_s] or key[pygame.K_UP] or key[pygame.K_DOWN]:
                self.flip_channel.play(self.flip)
