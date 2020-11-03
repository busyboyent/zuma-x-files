import pygame
import sys
import random
import os
import math
import time
import random
from constant import *

class Skull(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = skull_image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = 15

    def update(self):
        screen.blit(self.image, self.rect)

