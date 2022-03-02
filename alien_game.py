import pygame
from pygame.sprite import Sprite

class Obcy(Sprite):
    def __init__(self,gra):
        super().__init__()
        self.ekran = gra.screen
        self.opcje = gra.ustawienia

        self.image = pygame.image.load('obcy4.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def sprawdz_krawedzie(self):
        screem_react=self.ekran.get_rect()
        if self.rect.right >= screem_react.right or self.rect.left <=0:
            return True


    def update(self):
        self.x += self.opcje.szybkos_obcego * self.opcje.kierunek_floty

        self.rect.x=self.x



