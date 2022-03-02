import pygame.font
from pygame.sprite import Group

from ship_game import Statek

class Tablicawynikow:
    def __init__(self,gra):
        self.gra=gra
        self.ekran = gra.screen
        self.ekran_ramka = self.ekran.get_rect()
        self.ustawienia = gra.ustawienia
        self.statystyki = gra.staty

        self.kolor_textu = (30,30,30)
        self.font = pygame.font.SysFont(None,60)

        self.przygotuj_wynik()

        self.przygotuj_najlepszy_wynik()

        self.przygotuj_lvl()

        self.przygotuj_statek()

    def przygotuj_wynik(self):
        zaokroglony_wynik = round(self.statystyki.wynik,-1)


        wynik_string= "{:,}".format(zaokroglony_wynik)
        self.wynik_obraz = self.font.render(wynik_string,True,(45,100,43)
                                            )

        self.wynik_ramka = self.wynik_obraz.get_rect()
        self.wynik_ramka.right = self.ekran_ramka.right - 15
        self.wynik_ramka.top=15

    def pokaz(self):
        self.ekran.blit(self.wynik_obraz, self.wynik_ramka)
        self.ekran.blit(self.najlepszy_wynik_obraz,self.high_score_rect)
        self.ekran.blit(self.level_image,self.poziom_okno)
        self.statki.draw(self.ekran)

    def przygotuj_najlepszy_wynik(self):
        high_score=round(self.statystyki.best_score,-1)
        high_score_str = "{:,}".format(high_score)
        self.najlepszy_wynik_obraz = self.font.render(high_score_str,True,
                                                      (45,100,43))

        self.high_score_rect = self.najlepszy_wynik_obraz.get_rect()
        self.high_score_rect.centerx = self.ekran_ramka.centerx
        self.high_score_rect.top = self.high_score_rect.top+30

    def sprawdz_wynik(self):
        if self.statystyki.wynik>self.statystyki.best_score:
            self.statystyki.best_score=self.statystyki.wynik
            self.przygotuj_najlepszy_wynik()

    def przygotuj_lvl(self):
        poziom_string=str(self.statystyki.level)
        self.level_image = self.font.render(poziom_string,True,(45,100,43))

        self.poziom_okno = self.level_image.get_rect()
        self.poziom_okno.right = self.wynik_ramka.right
        self.poziom_okno.top= self.wynik_ramka.bottom+10

    def przygotuj_statek(self):
        self.statki=Group()
        for numer_statkow in range(self.statystyki.statki_pozostale):
            statek = Statek(self.gra)
            statek.rect.x = 10 + numer_statkow * statek.rect.width
            statek.rect.y = 10
            self.statki.add(statek)