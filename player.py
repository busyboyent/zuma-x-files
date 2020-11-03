import pygame
import sys
import random
import os
import math
import time
import random
from constant import *
from ball import *

current_bullet_sprite = pygame.sprite.Group()
current_ball = Ball(0, "current_bullet", 0, current_bullet, "", 0, 0)
current_bullet_sprite.add(current_ball)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.shooting = False
        self.timing = 0.25
        self.timer = 0
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.center = (width / 2, height / 2)
        self.x = width / 2
        self.y = height / 2
        self.angle = 0
        self.is_shoot = False
        self.current_bullet = current_bullet

    def rotate(self, x, y):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        self.angle = ((180 / math.pi) * -math.atan2(rel_y, rel_x))
        angle = ((180 / math.pi) * -math.atan2(rel_y, rel_x)) + 90
        rotated_image = pygame.transform.rotate(self.image, int(angle))
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, self.rect)

    def update(self):
        if self.shooting:
            tim = self.timing + self.timer - time.time()
            if tim <= 0:
                self.timer = 0
                self.shoot()
            if self.timer == 0:
                self.timer = time.time()
        self.rotate(self.x, self.y)

    def nextBullet(self, typ):
        #global game
        #global current_bullet_sprite
        #global balls_images
        if typ == "normal":
            self.current_bullet = random.choice(balls_images)
        if typ == "bomb":
            self.current_bullet = bomb_image
        list(current_bullet_sprite)[0].image = self.current_bullet

    def shoot(self):
        shoot_sound.play()
        self.is_shoot = True
        # bullet = Ball(self.angle, "bullet", 0, current_bullet, "unknown", 0, 0)
        # game.bullet_sprites.add(bullet)
        # game.all_sprites.add(bullet)

