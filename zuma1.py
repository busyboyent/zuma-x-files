import pygame
import sys
import random
import os
import math
import time
import random
from Game import *
from Ball import *
from Skull import *
from Player import *



class Zuma:

    def __init__():
        self.width = 1050
        self.height = 500
        self.speed = 5
        self.FPS = 50

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        self.pygame.init()
        self.pygame.mixer.init()
        self.screen = pygame.display.set_mode((width, height))
        self.pygame.display.set_caption('Zuma')
        self.clock = pygame.time.Clock()

        self.game_folder = os.path.dirname(__file__)
        self.image_folder = os.path.join(game_folder, 'images')

        self.violet_image = pygame.image.load(os.path.join(image_folder, 'Violet.png'))
        self.yellow_image = pygame.image.load(os.path.join(image_folder, 'Yellow.png'))
        self.skull_image = pygame.image.load(os.path.join(image_folder, 'Skull.png'))

        self.back_image = pygame.image.load(os.path.join(image_folder, 'Back.png'))
        self.player_image = pygame.image.load(os.path.join(image_folder, 'Player.png'))
        self.red_image = pygame.image.load(os.path.join(image_folder, 'Red.png'))
        self.blue_image = pygame.image.load(os.path.join(image_folder, 'Blue.png'))
        self.gray_image = pygame.image.load(os.path.join(image_folder, 'Gray.png'))

        self.balls_images = [red_image, blue_image, gray_image,
                        violet_image, yellow_image]
        self.current_bullet = random.choice(balls_images)


    def make_sprite(self, first, last, amount, typ, level, score, time):
        global game
        self.all_sprites = pygame.sprite.Group()
        self.ball_spr = pygame.sprite.Group()
        self.bullet_spr = pygame.sprite.Group()
        self.skull_spr = pygame.sprite.Group()
        self.current_bullet_sprite = pygame.sprite.Group()
        self.player = Player()

        self.all_sprites.add(player)
        if self.level == "Первый":
            self.skull = Skull(135, 185)
            self.all_sprites.add(self.skull)
            self.skull_spr.add(self.skull)
        self.counter = 0
        for i in range(first, last):
            self.angle = 0.25*i
            self.image = self.random.choice(self.balls_images)
            self.number = self.amount - self.counter
            self.x = 180 + (self.angle * 120)
            self.y = 100
            self.ball = Ball(self.angle, self.typ, self.number, self.image, self.level, self.x, self.y)
            self.counter += 1
            self.ball_spr.add(self.ball)
            self.all_sprites.add(self.ball)

        self.current_ball = Ball(0, "current_bullet", 0, self.current_bullet, self.level, 0, 0)
        self.current_bullet_sprite.add(self.current_ball)
        self.angle = 0
        self.balls = list(self.ball_spr)
        self.game = Game(self.player, self.all_sprites, self.ball_spr, self.bullet_spr,
                    self.skull_spr, self.balls, self.current_bullet_sprite,
                    self.typ, self.level, self.score, self.time)


    make_sprite(0, 10, 10, "common", "Тренировка", 0, 45)

    while True:

        self.clock.tick(FPS)
        self.game.bring_balls_together()
        self.game.get_events()
        self.game.check_hits()
        self.game.count_duplicates()

        self.screen.blit(back_image, [0, 0])
        self.game.current_bullet_sprite.update()
        self.game.current_bullet_sprite.draw(screen)

        self.game.all_sprites.update()
        self.game.ball_spr.update()
        self.game.bullet_spr.update()
        self.game.ball_spr.draw(screen)
        self.game.bullet_spr.draw(screen)
        self.game.show_score_and_level()
        self.pygame.display.flip()

        if self.game.time_left == 0:
            self.game.game_over()
        if len(self.game.ball_spr) == 0 and self.game.level == "Тренировка":
            make_sprite(0, 10, 10, "common", "Первый", self.game.score, 90)
            self.game.level = 'Первый'
        if len(self.game.ball_spr) == 0 and self.game.level == "Первый":
            self.game.game_over()

    self.pygame.quit()
