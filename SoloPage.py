import pygame
from game import Game
pygame.font.init()
pygame.init()

pygame.display.set_caption("SapinSapine")
big_window = pygame.display.set_mode((1080, 720))

background = pygame.image.load('Images/Snow bg.png')

# importer notre bouton pour lancer le jeu
play_button = pygame.image.load('Images/jouer logo.png')
play_button_rect = play_button.get_rect()

game = Game()

running = True

while running:

    big_window.blit(background, (-200, -400))

    # vérifier si le jeu à commencé ou non
    if game.is_playing:
        # déclencher les instruction de la partie
        game.update(big_window)
    # vérifier si notre jeu n'a pas commencé
    else:
        # ajouter écran de bienvenue
        big_window.blit(play_button, (220, 150))

    myfont = pygame.font.SysFont("Arial", 20)
    score_display = myfont.render(game.player.score.__str__(), 1, (255, 255, 107))
    big_window.blit(score_display, (15, 15))

    # mettre à jour l'écran
    pygame.display.flip()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and game.player.rect.x < 1000:
        # quelle touche a été utilisée
        game.player.move_right()
    if keys[pygame.K_LEFT] and game.player.rect.x > -10:
        game.player.move_left()
    if keys[pygame.K_UP] and game.player.rect.y > 10:
        # quelle touche a été utilisée
        game.player.move_up()
    if keys[pygame.K_DOWN] and game.player.rect.y < 575:
        game.player.move_down()

    pause = False

# si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # que l'event est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            print(game.player.score, " points !")
            pygame.quit()


            # mettre le jeu en pause, en gardant 'p' appuyer
        elif keys[pygame.K_p]:
            pause = True
            if pause:
                pygame.KEYDOWN = True
                pygame.event.wait()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérification si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                game.start()
