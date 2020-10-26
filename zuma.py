import pygame
import sys
import random
import os
import math
import time
import random
from game import *
from ball import *
from skull import *
from player import *
from const import *
from events import *
from ballcheck import *


pygame.init()
pygame.mixer.init()


def make_sprite(first, last, amount, typ, level, score, time):
    global game
    global player
    all_sprites = pygame.sprite.Group()
    ball_spr = pygame.sprite.Group()
    balls = list(ball_spr)
    bullet_spr = pygame.sprite.Group()
    skull_spr = pygame.sprite.Group()
    current_bullet_sprite = pygame.sprite.Group()
    #player = Player(game)
    game = Game(all_sprites, ball_spr, bullet_spr, skull_spr, balls, current_bullet_sprite, typ, level, score, time)
    #all_sprites.add(player)
    if level == "Первый":
        skull = Skull(135, 185)
        all_sprites.add(skull)
        skull_spr.add(skull)
    counter = 0
    for i in range(first, last):
        angle = 0.25*i
        image = random.choice(Const().balls_images)
        number = amount - counter
        x = 180 + (angle * 120)
        y = 100
        ball = Ball(game, angle, typ, number, image, level, x, y)
        counter += 1
        ball_spr.add(ball)
        all_sprites.add(ball)

    current_ball = Ball(game, 0, "current_bullet", 0, Const().current_bullet, level, 0, 0)
    current_bullet_sprite.add(current_ball)
    angle = 0
    #balls = list(ball_spr)
    #game = Game(all_sprites, ball_spr, bullet_spr, skull_spr, balls, current_bullet_sprite, typ, level, score, time)
    player = Player(game)
    all_sprites.add(player)

make_sprite(0, 10, 10, "common", "Тренировка", 0, 45)

while True:
    
    Const().clock.tick(Const().FPS)
    game.bring_balls_together()
    events = Events(player)
    events.get_events()
    ball_check = BallCheck(game)
    ball_check.check_hits()
    game.count_duplicates()

    Const().screen.blit(Const().back_image, [0, 0])
    game.current_bullet_sprite.update()
    game.current_bullet_sprite.draw(Const().screen)

    game.all_sprites.update()
    game.ball_spr.update()
    game.bullet_spr.update()
    game.ball_spr.draw(Const().screen)
    game.bullet_spr.draw(Const().screen)
    game.show_score_and_level()
    pygame.display.flip()

    if game.time_left == 0:
        game.game_over()
    if len(game.ball_spr) == 0 and game.level == "Тренировка":
        make_sprite(0, 10, 10, "common", "Первый", game.score, 90)
        game.level = 'Первый'
    if len(game.ball_spr) == 0 and game.level == "Первый":
        game.game_over()

    #game = Game(all_sprites, ball_spr, bullet_spr, skull_spr, balls, current_bullet_sprite, typ, level, score, time)
    #player = Player(game)

pygame.quit()
