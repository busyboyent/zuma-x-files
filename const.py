import os
import pygame
import random


class Const:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    width = 1050
    height = 500
    speed = 5
    FPS = 50

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

    violet_image = pygame.image.load(os.path.join(image_folder, 'Violet.png'))
    yellow_image = pygame.image.load(os.path.join(image_folder, 'Yellow.png'))
    skull_image = pygame.image.load(os.path.join(image_folder, 'Skull.png'))

    back_image = pygame.image.load(os.path.join(image_folder, 'Back.png'))
    player_image = pygame.image.load(os.path.join(image_folder, 'Player.png'))
    red_image = pygame.image.load(os.path.join(image_folder, 'Red.png'))
    blue_image = pygame.image.load(os.path.join(image_folder, 'Blue.png'))
    gray_image = pygame.image.load(os.path.join(image_folder, 'Gray.png'))

    balls_images = [red_image, blue_image, gray_image,
                violet_image, yellow_image]
    current_bullet = random.choice(balls_images)

    icon = pygame.image.load(os.path.join(image_folder, 'Player.png'))
    pygame.display.set_icon(icon)

    #player = Player()