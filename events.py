import pygame
from ball import *
from player import *


class Events:

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player

    def get_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shooting = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.shooting = False
                    self.player.nextBullet("normal")
