import pygame
import sys
import random
import os
import math
import time
import random
from const import *


class Game(pygame.sprite.Sprite):

    def __init__(self, all_sprites, ball_spr, bullet_spr,
                 skull_spr, balls, current_bullet_sprite, typ, level,
                 score, timing):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_speed = 5
        self.score = score
        self.level = level
        self.type = typ
        #self.player = player
        self.lives = 5
        self.time = timing
        self.time_left = timing
        self.all_sprites = all_sprites
        self.ball_spr = ball_spr
        self.bullet_spr = bullet_spr
        self.skull_spr = skull_spr
        self.balls = balls
        self.current_bullet_sprite = current_bullet_sprite
        self.copy_group = pygame.sprite.Group()
        self.begin_time = time.time()


    def count_duplicates(self):
        duplic_bal = 1
        for i in range(len(self.balls)):
            if i == (len(self.balls) - 1):
                if self.check_duplicates(i, duplic_bal):
                    break
                duplic_bal = 1
            elif self.balls[i].image == self.balls[i+1].image:
                duplic_bal += 1
            else:
                if self.check_duplicates(i, duplic_bal):
                    break
                duplic_bal = 1

    def check_duplicates(self, i, duplic_bal):
        if duplic_bal > 2:
            self.score += duplic_bal * 100
            for j in range(duplic_bal, 0, -1):
                current_ball = i - duplic_bal + 1
                super_number = self.balls[current_ball].number
                self.balls[current_ball].kill()
                self.balls.pop(current_ball)
            for j in self.balls:
                if j.number > len(self.balls) - i + duplic_bal:
                    j.number -= duplic_bal
            self.bring_balls_together()
            return True
        else:
            return False

    def bring_balls_together(self):
        for i in range(len(self.balls) - 1):
            x = (self.balls[i+1].rect.center[0] -
                 self.balls[i].rect.center[0])**2
            y = (self.balls[i+1].rect.center[1] -
                 self.balls[i].rect.center[1])**2
            sqrt = int(math.sqrt(x+y))
            while sqrt > 33:
                self.balls[i+1].reduce_distance()
                x = (self.balls[i+1].rect.center[0] -
                     self.balls[i].rect.center[0])**2
                y = (self.balls[i+1].rect.center[1] -
                     self.balls[i].rect.center[1])**2
                sqrt = math.sqrt(x+y)

    def show_score_and_level(self):
        screen = Const().screen
        WHITE = Const().WHITE
        self.time_left = int(self.time + self.begin_time - time.time())
        font = pygame.font.SysFont('monaco', 30)
        score = font.render('Счет: {}'.format(self.score), True, WHITE)
        level = font.render('Уровень: {}'.format(self.level), True, WHITE)
        lives = font.render('Жизни: {}'.format(self.lives), True, WHITE)
        timer = font.render('Время: {}'.format(self.time_left), True, WHITE)

        screen.blit(timer, (50, 300))
        screen.blit(lives, (50, 350))
        screen.blit(score, (50, 400))
        screen.blit(level, (50, 450))

    def game_over(self):
        screen = Const().screen
        pygame.mixer.music.stop()
        font = pygame.font.SysFont('monaco', 80)
        game_over = font.render('Игра окончена', True, Const().WHITE)
        screen.blit(game_over, (500, 200))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()