import pygame
import sys
import random
import os
import math
import time
import random
from constant import *
from ball import *

class Game():

    def __init__(self, player, all_sprites, ball_sprites, bullet_sprites,
                 skull_spites, balls, typ, level,
                 score, timing):

        self.score = score
        self.level = level
        self.type = typ
        self.player = player
        self.lives = 5

        self.time = timing
        self.time_left = timing
        self.all_sprites = all_sprites
        self.ball_sprites = ball_sprites
        self.bullet_sprites = bullet_sprites
        self.skull_spites = skull_spites
        self.balls = balls
        self.copy_group = pygame.sprite.Group()
        self.begin_time = time.time()
        self.duplicate_delay = time.time()

    def get_events(self):
        #global FPS
        #global bullet_speed
        #global current_bullet
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
        return "gj"

    def check_hits(self):
        skull_hits = pygame.sprite.groupcollide(self.skull_spites,
                                                self.ball_sprites,
                                                False, True,
                                                pygame.sprite.collide_circle)
        hits = pygame.sprite.groupcollide(self.bullet_sprites,
                                          self.ball_sprites,
                                          True, False,
                                          pygame.sprite.collide_circle)
        if skull_hits:
            if self.lives > 1:
                self.lives -= 1
            else:
                self.game_over()
        if hits:
            hit_balls = list(hits.values())
            bullet_ball = list(hits.keys())
            hit_ball = hit_balls[0][0]
            shift_angle, x, y = hit_ball.return_new_ball_pos()
            shift_number = hit_ball.number
            shift_image = bullet_ball[0].image

            for ball in list(self.ball_sprites):
                if ball.number >= shift_number:
                    ball.number += 1
                else:
                    ball.correct_sprites_trajectory()
            ball = Ball(shift_angle, self.type,
                        shift_number, shift_image, self.level, x, y)
            self.ball_sprites.add(ball)
            self.all_sprites.add(ball)
            self.balls.insert(len(self.balls) - shift_number + 1, ball)
            self.count_duplicates()

    def count_duplicates(self):
        duplicate_balls = 1
        if (time.time() - self.duplicate_delay) > 0.3:
            for i in range(len(self.balls)):
                if i == (len(self.balls) - 1):
                    if self.check_duplicates(i, duplicate_balls):
                        break
                    duplicate_balls = 1
                elif self.balls[i].image == self.balls[i+1].image:
                    duplicate_balls += 1
                else:
                    if self.check_duplicates(i, duplicate_balls):
                        break
                    duplicate_balls = 1
            self.duplicate_delay = time.time()

    def check_duplicates(self, i, duplicate_balls):
        if duplicate_balls > 2:
            self.score += duplicate_balls * 100
            for j in range(duplicate_balls, 0, -1):
                current_ball = i - duplicate_balls + 1
                super_number = self.balls[current_ball].number
                self.balls[current_ball].kill()
                self.balls.pop(current_ball)
            for j in self.balls:
                if j.number > len(self.balls) - i + duplicate_balls:
                    j.number -= duplicate_balls
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
        pygame.mixer.music.stop()
        game_over_sound.play()
        font = pygame.font.SysFont('monaco', 80)
        game_over = font.render('Игра окончена', True, WHITE)
        screen.blit(game_over, (500, 200))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
