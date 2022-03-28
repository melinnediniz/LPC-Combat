import pygame

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)


class Sound:
    def __init__(self):
        self.shot = pygame.mixer.Sound('sound/shot.ogg')
        self.move = pygame.mixer.Sound("sound/move.ogg")
        self.flip = pygame.mixer.Sound("sound/flip.wav")
        self.kill = pygame.mixer.Sound("sound/kill.ogg")

    def channel(self, num):
        name = pygame.mixer.Channel(num)
        return name

    def play_move(self):
        self.channel(0).set_volume(0.7), self.channel(1).set_volume(0.7)
        key = pygame.key.get_pressed()

        if not self.channel(0).get_busy():
            if key[pygame.K_d] or key[pygame.K_s] or key[pygame.K_a]:
                self.channel(0).play(self.move)
        elif self.channel(0).get_busy():
            if not key[pygame.K_d] and (not key[pygame.K_s]) and (not key[pygame.K_a]):
                self.channel(0).stop()

        if not self.channel(1).get_busy():
            if key[pygame.K_LEFT] or key[pygame.K_RIGHT] or key[pygame.K_DOWN] or key[pygame.K_UP]:
                self.channel(1).play(self.move)
        elif self.channel(1).get_busy():
            if not key[pygame.K_LEFT] and (not key[pygame.K_RIGHT]) and (not key[pygame.K_UP]) \
                    and (not key[pygame.K_DOWN]):
                self.channel(1).stop()

    def play_shot(self):
        key = pygame.key.get_pressed()
        if not self.channel(2).get_busy():
            if key[pygame.K_g] or key[pygame.K_l]:
                self.channel(2).play(self.shot)

    def play_kill(self):
        if self.channel(3).get_busy():
            self.channel(3).stop()
        self.channel(3).play(self.kill)
        self.channel(3).set_volume(0.2)

    def play_flip(self):
        self.channel(4).set_volume(0.1)
        key = pygame.key.get_pressed()
        if not self.channel(4).get_busy():
            if key[pygame.K_w] or key[pygame.K_s] or key[pygame.K_UP] or key[pygame.K_DOWN]:
                self.channel(4).play(self.flip)

    def call_sound(self):
        self.play_shot()
        self.play_move()
        self.play_flip()
