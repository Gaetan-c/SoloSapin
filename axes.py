import pygame
from random import randint


class Axes(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.velocity = randint(1, 5)
        self.attack = 1
        self.game = game
        self.image = pygame.image.load("Images//Hache_B_orange.png")
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 1250
        self.rect.y = randint(0, 580)
        self.origin_image = self.image
        self.angle = 0

    def rotate_axes(self):
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.rect = self.image.get_rect()
        self.rect.x = 1250
        self.rect.y = randint(0, 580)
        self.velocity = randint(1, 5)

    def collision(self):
        if self.game.check_collision(self, self.game.all_players):
            self.remove()
            self.game.player.damage(1)

    def move_left(self):
        self.rect.x -= self.velocity
        self.rotate_axes()
        if self.rect.x < -80:
            self.remove()


class ReverseAxes(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = randint(1, 5)
        self.attack = 1
        self.game = game
        self.image = pygame.image.load("Images//Hache_B_rouge.png")
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()
        self.rect.x = -250
        self.rect.y = randint(0, 580)
        self.origin_image = self.image
        self.angle = 0

    def rotate_axes(self):
        self.angle -= 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.rect = self.image.get_rect()
        self.rect.x = - 250
        self.rect.y = randint(0, 580)
        self.velocity = randint(1, 5)

    def collision(self):
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(1)
            self.remove()

    def move_right(self):
        self.rect.x += self.velocity
        self.rotate_axes()
        if self.rect.x > 1100:
            self.remove()


class TopAxes(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = randint(1, 5)
        self.attack = 1
        self.game = game
        self.image = pygame.image.load("Images//Hache_B_bleue.png")
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, 1000)
        self.rect.y = - 250
        self.origin_image = self.image
        self.angle = 0

    def rotate_axes(self):
        self.angle -= 9
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, 1000)
        self.rect.y = - 250
        self.velocity = randint(1, 5)

    def collision(self):
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(1)
            self.remove()

    def move_down(self):
        self.rect.y += self.velocity
        self.rotate_axes()
        if self.rect.y > 700:
            self.remove()
