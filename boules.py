import pygame
from random import randint


class Boules(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = randint(1, 5)
        self.game = game
        self.image = pygame.image.load("Images/Boules.png")
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, 1000)
        self.rect.y = - 250

    def remove(self):
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, 1000)
        self.rect.y = - 250
        self.velocity = randint(1, 5)

    def collision(self):
        if self.game.check_collision(self, self.game.all_players):
            self.remove()

    def move_down(self):
        self.rect.y += self.velocity
        if self.rect.y > 700:
            self.remove()
