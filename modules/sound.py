import pygame

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)


class Sound:
    def __init__(self):
        self.shot = pygame.mixer.Sound('sound/shot.ogg')
        self.move = pygame.mixer.Sound("sound/move.ogg")
        self.flip = pygame.mixer.Sound("sound/flip_tank.wav")
        self.kill = ""  # pygame.mixer.Sound("sound/kill.wav")
        self.green_tank_channel = pygame.mixer.Channel(0)
        self.blue_tank_channel = pygame.mixer.Channel(1)
        self.shot_channel = pygame.mixer.Channel(2)

    def play_move(self):
        self.blue_tank_channel.set_volume(0.5), self.green_tank_channel.set_volume(0.5)
        key = pygame.key.get_pressed()
        if not self.green_tank_channel.get_busy():
            if key[pygame.K_d] or key[pygame.K_s] or key[pygame.K_a] or key[pygame.K_w]:
                self.green_tank_channel.play(self.move)
        elif self.green_tank_channel.get_busy():
            if not key[pygame.K_d] and (not key[pygame.K_s]) and (not key[pygame.K_a]) and (not key[pygame.K_w]):
                self.green_tank_channel.stop()

        if not self.blue_tank_channel.get_busy():
            if key[pygame.K_LEFT] or key[pygame.K_RIGHT] or key[pygame.K_DOWN] or key[pygame.K_UP]:
                self.blue_tank_channel.play(self.move)
        elif self.blue_tank_channel.get_busy():
            if not key[pygame.K_LEFT] and (not key[pygame.K_RIGHT]) and (not key[pygame.K_UP]) \
                    and (not key[pygame.K_DOWN]):
                self.blue_tank_channel.stop()

    def play_shot(self):
        key = pygame.key.get_pressed()
        if not self.shot_channel.get_busy():
            if key[pygame.K_g] or key[pygame.K_l]:
                self.shot_channel.play(self.shot)
                print('shot sound')
