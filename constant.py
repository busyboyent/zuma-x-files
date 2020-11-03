import pygame
import sys
import random
import os
import math
import time
import random

width = 1050
height = 500
speed = 5
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Zuma')
clock = pygame.time.Clock()

game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, 'images')
back_image = pygame.image.load(os.path.join(image_folder, 'Back.png'))
player_image = pygame.image.load(os.path.join(image_folder, 'Player.png'))
red_image = pygame.image.load(os.path.join(image_folder, 'Red.png'))
blue_image = pygame.image.load(os.path.join(image_folder, 'DarkBlue.png'))
gray_image = pygame.image.load(os.path.join(image_folder, 'Gray.png'))
violet_image = pygame.image.load(os.path.join(image_folder, 'Violet.png'))
yellow_image = pygame.image.load(os.path.join(image_folder, 'Yellow.png'))
skull_image = pygame.image.load(os.path.join(image_folder, 'Skull.png'))

balls_images = [red_image, blue_image, gray_image,
                violet_image, yellow_image]
current_bullet = random.choice(balls_images)

sounds_folder = os.path.join(game_folder, 'sounds')
shoot_sound = pygame.mixer.Sound(os.path.join(sounds_folder, 'shoot.wav'))
explode_sound = pygame.mixer.Sound(os.path.join(sounds_folder, 'expl.wav'))
game_over_sound = pygame.mixer.Sound(os.path.join(sounds_folder, 'end.wav'))
pygame.mixer.music.load(os.path.join(sounds_folder, 'SweetDreams.mp3'))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

icon = pygame.image.load(os.path.join(image_folder, 'Player.png'))
pygame.display.set_icon(icon)

bullet_speed = 5




