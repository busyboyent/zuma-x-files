import pygame
import sys
import random
import os
import math
import time
import random
from ball import *
from game import *
from player import *
from skull import *
from constant import *


def make_Sprites(first, last, amount, typ, level, score, time):
    global game
    all_sprites = pygame.sprite.Group()
    ball_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()
    skull_spites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    if level == "Первый":
        skull = Skull(135, 185)
        all_sprites.add(skull)
        skull_spites.add(skull)
    counter = 0
    for i in range(first, last):
        angle = 0.25*i
        image = random.choice(balls_images)
        number = amount - counter
        x = 180 + (angle * 120)
        y = 100
        ball = Ball(angle, typ, number, image, level, x, y)
        counter += 1
        ball_sprites.add(ball)
        all_sprites.add(ball)

    angle = 0
    balls = list(ball_sprites)
    game = Game(player, all_sprites, ball_sprites, bullet_sprites,
                skull_spites, balls,
                typ, level, score, time)


make_Sprites(0, 10, 10, "common", "Нулевой", 0, 45)

while True:
    #global current_bullet

    clock.tick(FPS)
    game.bring_balls_together()
    game.get_events()
    game.check_hits()
    game.count_duplicates()

    screen.blit(back_image, [0, 0])
    current_bullet_sprite.update()
    current_bullet_sprite.draw(screen)
    game.all_sprites.update()
    game.ball_sprites.update()
    game.bullet_sprites.update()
    if game.player.is_shoot:
        bullet = Ball(game.player.angle, "bullet", 0, game.player.current_bullet, "unknown", 0, 0)
        game.bullet_sprites.add(bullet)
        game.all_sprites.add(bullet)
        game.player.is_shoot = False
    game.ball_sprites.draw(screen)
    game.bullet_sprites.draw(screen)
    game.show_score_and_level()
    pygame.display.flip()

    if game.time_left == 0:
        game.game_over()
    if len(game.ball_sprites) == 0 and game.level == "Нулевой":
        make_Sprites(0, 10, 10, "common", "Первый", game.score, 90)
        game.level = 'Первый'
    if len(game.ball_sprites) == 0 and game.level == "Первый":
        game.game_over()

pygame.quit()
