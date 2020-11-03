import pygame
import sys
import random
import os
import math
import time
import random
from constant import *

class Ball(pygame.sprite.Sprite):

    def __init__(self, angle, typ, number, image, level, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 1
        self.number = number
        self.type = typ
        self.level = level
        self.image = image
        self.angle = angle
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        if self.level == "Первый":
            self.rect.x = x
            self.rect.y = y
        if self.type == "bullet":
            self.rect.center = (width / 2, height / 2)
        self.shoot_angle = self.angle + 90
        self.radius = 10

    def update(self):
        if self.level == "Нулевой":
            if self.type == "common":
                self.circle(525, 250, 125)
            if self.type == "reverse":
                self.reverse_circle(525, 250, 125)
        if self.level == "Первый":
            if self.type == "common":
                self.maze()
            if self.type == "reverse":
                self.reverse_maze()
        if self.type == "bullet":
            self.bullet()
        if self.type == "current_bullet":
            self.current_bullet()

    def maze(self):
        speed = (1 * self.speed)
        if self.rect.x < 900 and self.rect.y == 100:
            self.rect.x += speed
        elif self.rect.x == 900 and self.rect.y < 400:
            self.rect.y += speed
        elif self.rect.x > 100 and self.rect.y == 400:
            self.rect.x -= speed
        elif self.rect.x == 100 and self.rect.y > 150:
            self.rect.y -= speed
        elif self.rect.x < 850 and self.rect.y == 150:
            self.rect.x += speed
        elif self.rect.x == 850 and self.rect.y < 350:
            self.rect.y += speed
        elif self.rect.x > 150 and self.rect.y == 350:
            self.rect.x -= speed
        elif self.rect.x == 150 and self.rect.y > 200:
            self.rect.y -= speed

    def reverse_maze(self):
        speed = (1 * self.speed)
        if self.rect.x > 100 and self.rect.y == 100:
            self.rect.x -= speed
        elif self.rect.x == 900 and self.rect.y > 100:
            self.rect.y -= speed
        elif self.rect.x < 900 and self.rect.y == 400:
            self.rect.x += speed
        elif self.rect.x == 100 and self.rect.y < 400:
            self.rect.y += speed
        elif self.rect.x > 100 and self.rect.y == 150:
            self.rect.x -= speed
        elif self.rect.x == 850 and self.rect.y > 150:
            self.rect.y -= speed
        elif self.rect.x < 850 and self.rect.y == 350:
            self.rect.x += speed
        elif self.rect.x == 150 and self.rect.y < 350:
            self.rect.y += speed

    def reduce_distance(self):
        if self.level == "Нулевой":
            self.reverse_circle(525, 250, 125)
        if self.level == "Первый":
            self.reverse_maze()

    def current_bullet(self):
        self.rect.x = width/2 + 25
        self.rect.y = height/2 + 25

    def return_new_ball_pos(self):
        if self.level == "Нулевой":
            for i in range(50):
                self.circle(525, 250, 125)
            angle = self.angle
            x = self.rect.x
            y = self.rect.y
            for i in range(50):
                self.reverse_circle(525, 250, 125)
            return angle, x, y
        if self.level == "Первый":
            for i in range(30):
                self.maze()
            angle = self.angle
            x = self.rect.x
            y = self.rect.y
            for i in range(30):
                self.reverse_maze()
            return angle, x, y

    def correct_sprites_trajectory(self):
        if self.level == "Нулевой":
            for i in range(50):
                self.circle(525, 250, 125)
        if self.level == "Первый":
            for i in range(50):
                self.update()

    def circle(self, x, y, radius):
        self.angle += 0.005 * self.speed
        self.rect.x = x + radius * math.cos(self.angle)
        self.rect.y = y + radius * math.sin(self.angle)

    def reverse_circle(self, x, y, radius):
        self.angle -= 0.005 * self.speed
        self.rect.x = x + radius * math.cos(self.angle)
        self.rect.y = y + radius * math.sin(self.angle)

    def bullet(self):
        #global game
        #global bullet_speed
        self.rect.y += (math.cos(math.pi * self.shoot_angle / 180) *
                        bullet_speed)
        self.rect.x += (math.sin(math.pi * self.shoot_angle / 180) *
                        bullet_speed)
        if (self.rect.x < 0 or self.rect.x > width
           or self.rect.y < 0 or self.rect.y > height):
            self.kill()
