import pygame
from pygame.sprite import Sprite

class Pocisk(Sprite):
    def __init__(self,gra):
        super().__init__()
        self.ekran = gra.screen
        self.ustawienia = gra.ustawienia
        self.kolor = self.ustawienia.pocisk_kolor


        self.rect = pygame.Rect(0,0, self.ustawienia.pocisk_szerokosc,
                                     self.ustawienia.pocisk_dlugosc)
        self.rect.midtop= gra.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.ustawienia.pocisk_szybkosc
        self.rect.y = self.y

    def pocisk_rysuj(self):
        pygame.draw.rect(self.ekran, self.kolor, self.rect)