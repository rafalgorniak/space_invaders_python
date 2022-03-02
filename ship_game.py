import pygame
from pygame.sprite import Sprite


class Statek(Sprite):
    def __init__(self,graszka):
        super().__init__()
        self.screen = graszka.screen
        self.screen_rect = graszka.screen.get_rect()

        self.settings = graszka.ustawienia

        self.image = pygame.image.load('ship1.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.w_ruchu_lewo = False
        self.w_ruchu_prawo = False

    def aktualizacja(self):
        if self.w_ruchu_prawo and self.rect.right < self.screen_rect.right:
            self.x += self.settings.szybkosc_statku
        if self.w_ruchu_lewo and self.rect.left > self.screen_rect.left :
            self.x -= self.settings.szybkosc_statku

        self.rect.x=self.x
    def pokaz_mnie(self):
        self.screen.blit(self.image, self.rect)

    def wysrodkuj_statek(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)