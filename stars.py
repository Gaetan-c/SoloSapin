import pygame
from random import randint


class Stars(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("Images/Stars.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0 + randint(0, 1000)
        self.rect.y = 0 + randint(10, 575)

    def remove(self):
        self.rect = self.image.get_rect()
        self.rect.x = 0 + randint(0, 1000)
        self.rect.y = 0 + randint(10, 575)

    def collision(self):
        if self.game.check_collision(self, self.game.all_players):
            self.remove()
           # self.game.player.heal_sapin
