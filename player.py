import pygame
import sys
import random
import os
import math
import time
import random
from ball import *
from game import *
from const import *


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.shooting = False
        self.timing = 0.25
        self.timer = 0
        self.current_bullet = Const().current_bullet
        self.game = game
        self.image = Const().player_image
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.center = (Const().width / 2, Const().height / 2)
        self.x = Const().width / 2
        self.y = Const().height / 2
        self.angle = 0

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        self.angle = ((180 / math.pi) * -math.atan2(rel_y, rel_x))
        angle = ((180 / math.pi) * -math.atan2(rel_y, rel_x)) + 90
        rotated_image = pygame.transform.rotate(self.image, int(angle))
        self.rect = self.image.get_rect(center=self.rect.center)
        Const().screen.blit(rotated_image, self.rect)

    def update(self):
        if self.shooting:
            tim = self.timing + self.timer - time.time()
            if tim <= 0:
                self.timer = 0
                self.shoot()
            if self.timer == 0:
                self.timer = time.time()
        self.rotate()

    def nextBullet(self, typ):
        #current_bullet = Const().current_bullet
        #global game
        if typ == "normal":
            self.current_bullet = random.choice(Const().balls_images)

        list(self.game.current_bullet_sprite)[0].image = self.current_bullet

    def shoot(self):
        #current_bullet = Const().current_bullet
        bullet = Ball(self.game, self.angle, "bullet", 0, self.current_bullet, "unknown", 0, 0)

        #game = Game(all_sprites, ball_spr, bullet_spr,
        #        skull_spr, balls, current_bullet_sprite,
        #        typ, level, score, time)

        self.game.bullet_spr.add(bullet)
        self.game.all_sprites.add(bullet)