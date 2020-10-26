import pygame
from ball import *
from game import *


class BallCheck:

    def __init__(self, game):

        self.game = game

    def check_hits(self):
        self.skull_hits = pygame.sprite.groupcollide(self.game.skull_spr,
                                                self.game.ball_spr,
                                                False, True,
                                                pygame.sprite.collide_circle)
        self.hits = pygame.sprite.groupcollide(self.game.bullet_spr,
                                          self.game.ball_spr,
                                          True, False,
                                          pygame.sprite.collide_circle)
        if self.skull_hits:
            if self.game.lives > 1:
                self.game.lives -= 1
            else:
                self.game_over()
        if self.hits:
            self.hit_balls = list(self.hits.values())
            self.bullet_ball = list(self.hits.keys())
            self.hit_ball = self.hit_balls[0][0]
            self.shift_angle, self.x, self.y = self.hit_ball.return_new_ball_pos()
            self.shift_number = self.hit_ball.number
            self.shift_image = self.bullet_ball[0].image

            for ball in list(self.game.ball_spr):
                if ball.number >= self.shift_number:
                    ball.number += 1
                else:
                    ball.correct_sprites_trajectory()
            self.ball = Ball(self.game, self.shift_angle, self.game.type,
                        self.shift_number, self.shift_image, self.game.level, self.x, self.y)
            self.game.ball_spr.add(self.ball)
            self.game.all_sprites.add(self.ball)
            self.game.balls.insert(len(self.game.balls) - self.shift_number + 1, self.ball)
            self.count_duplicates()

    def count_duplicates(self):
        duplic_bal = 1
        for i in range(len(self.game.balls)):
            if i == (len(self.game.balls) - 1):
                if self.check_duplicates(i, duplic_bal):
                    break
                duplic_bal = 1
            elif self.game.balls[i].image == self.game.balls[i+1].image:
                duplic_bal += 1
            else:
                if self.check_duplicates(i, duplic_bal):
                    break
                duplic_bal = 1

    def check_duplicates(self, i, duplic_bal):
        if duplic_bal > 2:
            self.game.score += duplic_bal * 100
            for j in range(duplic_bal, 0, -1):
                current_ball = i - duplic_bal + 1
                super_number = self.game.balls[current_ball].number
                self.game.balls[current_ball].kill()
                self.game.balls.pop(current_ball)
            for j in self.game.balls:
                if j.number > len(self.game.balls) - i + duplic_bal:
                    j.number -= duplic_bal
            self.bring_balls_together()
            return True
        else:
            return False

    def bring_balls_together(self):
        for i in range(len(self.game.balls) - 1):
            x = (self.game.balls[i+1].rect.center[0] -
                 self.game.balls[i].rect.center[0])**2
            y = (self.game.balls[i+1].rect.center[1] -
                 self.game.balls[i].rect.center[1])**2
            sqrt = int(math.sqrt(x+y))
            while sqrt > 33:
                self.game.balls[i+1].reduce_distance()
                x = (self.game.balls[i+1].rect.center[0] -
                     self.game.balls[i].rect.center[0])**2
                y = (self.game.balls[i+1].rect.center[1] -
                     self.game.balls[i].rect.center[1])**2
                sqrt = math.sqrt(x+y)

    def game_over(self):
        pygame.mixer.music.stop()
        font = pygame.font.SysFont('monaco', 80)
        game_over = font.render('Игра окончена', True, WHITE)
        screen.blit(game_over, (500, 200))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
