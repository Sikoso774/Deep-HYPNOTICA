# scripts/game_elements/player.py

import pygame
from scripts.game_elements.constants import PLAYER_SIZE, PLAYER_SPEED, LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU
from scripts.game_elements.resources import load_player_sprite


class Player(pygame.sprite.Sprite):  # Hérite de pygame.sprite.Sprite
    def __init__(self):
        super().__init__()  # Appel au constructeur de la classe parente (Sprite)
        self.size = PLAYER_SIZE
        self.speed = PLAYER_SPEED
        self.image = load_player_sprite(self.size)  # Charge le sprite (ou placeholder)

        # Position initiale (centrée horizontalement, un peu au-dessus du bas)
        self.rect = self.image.get_rect(
            centerx=LARGEUR_ECRAN_JEU // 2,
            bottom=HAUTEUR_ECRAN_JEU - 20
        )

    def move(self, direction, screen_width):
        """
        Déplace le joueur horizontalement et le contraint à l'écran.
        direction: -1 pour gauche, 1 pour droite
        """
        self.rect.x += direction * self.speed

        # Contraintes de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

    def draw(self, surface):
        """
        Dessine le joueur sur la surface donnée.
        """
        surface.blit(self.image, self.rect)


# --- Bloc de test pour l'exécution indépendante (optionnel) ---
if __name__ == "__main__":
    pygame.init()
    screen_test = pygame.display.set_mode((LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU))
    pygame.display.set_caption("Test Player")

    player_test = Player()
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_test.move(-1, LARGEUR_ECRAN_JEU)
                if event.key == pygame.K_RIGHT:
                    player_test.move(1, LARGEUR_ECRAN_JEU)

        # Le joueur bouge en continu si la touche est maintenue
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_test.move(-1, LARGEUR_ECRAN_JEU)
        if keys[pygame.K_RIGHT]:
            player_test.move(1, LARGEUR_ECRAN_JEU)

        screen_test.fill((0, 0, 0))  # Fond noir
        player_test.draw(screen_test)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()