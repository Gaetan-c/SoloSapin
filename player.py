import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 5
        self.max_health = 5
        self.velocity = 4
        self.score = 0
        self.image = pygame.image.load('Images/SapinSapine.png')
        self.image = pygame.transform.scale(self.image, (75, 110))
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 575

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def image_sapin(self):
        if 4 <= self.health < 5:
            self.image = pygame.image.load('Images/SapinSapine1.png')
            self.image = pygame.transform.scale(self.image, (75, 110))
        elif 3 <= self.health < 4:
            self.image = pygame.image.load('Images/SapinSapine2.png')
            self.image = pygame.transform.scale(self.image, (75, 110))
        elif 2 <= self.health < 3:
            self.image = pygame.image.load('Images/SapinSapine3.png')
            self.image = pygame.transform.scale(self.image, (75, 110))
        elif 1 <= self.health < 2:
            self.image = pygame.image.load('Images/SapinSapine4.png')
            self.image = pygame.transform.scale(self.image, (75, 110))
        elif 0 <= self.health < 1:
            self.image = pygame.image.load('Images/SapinSapinered.png')
            self.image = pygame.transform.scale(self.image, (75, 110))
        else:
            self.image = pygame.image.load('Images/SapinSapine.png')
            self.image = pygame.transform.scale(self.image, (75, 110))

    def damage(self, amount):
        # infliger les dégats
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()

    def collision_stars(self):
        if self.game.check_collision(self, self.game.all_stars):
            self.game.player.score += 3

    def collision_boules(self):
        if self.game.check_collision(self, self.game.all_boules):
            self.game.player.score += 1

    def heal_sapin(self):
        if self.health < self.max_health and self.game.check_collision(self, self.game.all_stars):
            self.health += 0.1
