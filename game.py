import pygame
from player import Player
from stars import Stars
from boules import Boules
from axes import Axes, ReverseAxes, TopAxes


# créer une seconde classe : game
class Game:

    def __init__(self):
        # définir si le jeu à commencé
        self.is_playing = False
        # généré notre joueur quand une nouvelle partie est lancée
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_stars = pygame.sprite.Group()
        self.all_axes = pygame.sprite.Group()
        self.all_ReverseAxes = pygame.sprite.Group()
        self.all_TopAxes = pygame.sprite.Group()
        self.all_boules = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_stars()
        self.spawn_axes()
        self.spawn_axes()
        self.spawn_reverse_axes()
        self.spawn_reverse_axes()
        self.spawn_top_axes()
        self.spawn_top_axes()
        self.spawn_boules()

    def game_over(self):
        # remettre le jeu au point de départ
        self.all_axes = pygame.sprite.Group()
        self.all_TopAxes = pygame.sprite.Group()
        self.all_ReverseAxes = pygame.sprite.Group()
        self.all_stars = pygame.sprite.Group()
        self.all_boules = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.score = 0
        self.is_playing = False

    def update(self, big_window):

        big_window.blit(self.player.image, self.player.rect)

        self.all_stars.draw(big_window)
        self.all_axes.draw(big_window)
        self.all_ReverseAxes.draw(big_window)
        self.all_TopAxes.draw(big_window)
        self.all_boules.draw(big_window)

        for player in self.all_players:
            player.image_sapin()
            player.heal_sapin()
            player.collision_stars()
            player.collision_boules()

        for stars in self.all_stars:
            stars.collision()

        for axes in self.all_axes:
            axes.move_left()
            axes.collision()

        for reverseaxes in self.all_ReverseAxes:
            reverseaxes.move_right()
            reverseaxes.collision()

        for topaxes in self.all_TopAxes:
            topaxes.move_down()
            topaxes.collision()

        for boules in self.all_boules:
            boules.move_down()
            boules.collision()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_stars(self):
        stars = Stars(self)
        self.all_stars.add(stars)

    def spawn_axes(self):
        axes = Axes(self)
        self.all_axes.add(axes)

    def spawn_reverse_axes(self):
        reverse_axes = ReverseAxes(self)
        self.all_ReverseAxes.add(reverse_axes)

    def spawn_top_axes(self):
        top_axes = TopAxes(self)
        self.all_TopAxes.add(top_axes)

    def spawn_boules(self):
        boules = Boules(self)
        self.all_boules.add(boules)
