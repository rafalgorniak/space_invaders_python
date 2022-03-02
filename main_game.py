#importing necessary libraries
import sys
import pygame
from time import sleep
from pygame import mixer

#importing classes from Class Files
from options_game import Ustawienia
from ship_game import Statek
from bullet_game import Pocisk
from alien_game import Obcy
from statistics_game import StatyGry
from button_game import Przycisk
from leaderscoreboard_game import Tablicawynikow


class InwazjaObcych():      #main class implementation
    def __init__(self):     #creating constructior
        pygame.init()       #initializing pygame module, crucial interface
        self.ustawienia = Ustawienia()      #assigning settings to self
        #defining screen size
        self.screen=pygame.display.set_mode((self.ustawienia.screen_szerokosc,self.ustawienia.screen_wysokosc))
        #making image a background
        self.bacg_img=pygame.image.load('tlo.png').convert()
        #naming caption
        pygame.display.set_caption("Invasion landowers!!!")
        #assigning stats to self
        self.staty = StatyGry(self)
        #assigning score board to self
        self.tablicawynikow = Tablicawynikow(self)
        #assigning ship to self
        self.ship = Statek(self)
        #looping main theme sound and loading it from disc
        mixer.music.load('tlo.mp3')
        mixer.music.play(-1)
        #assigning aliens and bullets to self
        self.pociski = pygame.sprite.Group()
        self.alieni = pygame.sprite.Group()
        #starting button

        self.przysick_poczatkowy = Przycisk(self,"Aliens attack!!!")

        self._stworzenie_floty()


    #loop function in charge of updating objects
    def rusz_gre(self):
        while True:
            self.zdarzenia()

            if self.staty.czy_zyjesz:

                self.ship.aktualizacja()
                self.aktualizacja_poxiskow()
                self.aktualizcja_obcyh()

            self.aktualizacja()
    #function checking if event happened
    def zdarzenia(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()
            elif event.type ==pygame.MOUSEBUTTONDOWN:
                pozycjamyszy = pygame.mouse.get_pos()
                self.sprawdz_gre_przycisk(pozycjamyszy)
            elif event.type == pygame.KEYDOWN:
                self.sprawdz_klawisz_dol(event)
            elif event.type == pygame.KEYUP:
                self.sprawdz_klawisz_gora(event)

    #positioning start button, and what happen after clicking  it
    def sprawdz_gre_przycisk(self,pozycja):
        przycisk_klikany = self.przysick_poczatkowy.prostokat.collidepoint(pozycja)
        if przycisk_klikany and not self.staty.czy_zyjesz:
            self.ustawienia.inicjacja_dynamiczna()
            self.staty.zresetuj_staty()
            self.staty.czy_zyjesz=True

            self.tablicawynikow.przygotuj_wynik()
            self.tablicawynikow.przygotuj_lvl()
            self.tablicawynikow.przygotuj_statek()

            self.alieni.empty()
            self.pociski.empty()

            self._stworzenie_floty()
            self.ship.wysrodkuj_statek()
            pygame.mouse.set_visible(False)

    #checking if some button was pushed
    def sprawdz_klawisz_dol(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.w_ruchu_prawo = True
        elif event.key == pygame.K_LEFT:
            self.ship.w_ruchu_lewo = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    # checking if some button was pulled
    def sprawdz_klawisz_gora(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.w_ruchu_prawo = False
        elif event.key == pygame.K_LEFT:
            self.ship.w_ruchu_lewo = False
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    #updating bullets' position and removing it after being out of the window
    def aktualizacja_poxiskow(self):
        self.pociski.update()

        for pocisk in self.pociski.copy():
            if pocisk.rect.bottom <= 0:
                self.pociski.remove(pocisk)

        self.sprawdzenie_kolizji()

    #function which works after loosing one heart, lost round
    def uderzenie_statku(self):
        if self.staty.statki_pozostale>1:


            self.staty.statki_pozostale-=1
            self.tablicawynikow.przygotuj_statek()

            self.alieni.empty()
            self.pociski.empty()

            self._stworzenie_floty()
            self.ship.wysrodkuj_statek()

            sleep(0.4)
        else:
            self.staty.czy_zyjesz=False
            pygame.mouse.set_visible(True)

    #checking colision bullet with alien
    def sprawdzenie_kolizji(self):
        kolizja = pygame.sprite.groupcollide(self.pociski, self.alieni, True,
                                             True)

        dzwiek_kolizji = mixer.Sound('PING.mp3')

        if kolizja:
            dzwiek_kolizji.play()
            for alieni in kolizja.values():
                self.staty.wynik += self.ustawienia.pkt_for_alien * len(alieni)
            self.tablicawynikow.przygotuj_wynik()
            self.tablicawynikow.sprawdz_wynik()


        if not self.alieni:
            self.pociski.empty()
            self._stworzenie_floty()
            self.ustawienia.zwieksz_predkosc()

            self.staty.level+=1
            self.tablicawynikow.przygotuj_lvl()

    #shooting bullets
    def _fire_bullet(self):
        if len(self.pociski) < self.ustawienia.ilosc_pociskow:
            new_pocisk = Pocisk(self)
            self.pociski.add(new_pocisk)

    #creating new aliens army
    def _stworzenie_floty(self):
        obcy = Obcy(self)
        szerokosc_obcego,wysokosc_obcego = obcy.rect.size

        dostepne_miejsce_x = self.ustawienia.screen_szerokosc - (11 * szerokosc_obcego)
        numer_obcych_x = dostepne_miejsce_x // (1 * szerokosc_obcego)

        wysokosc_statku = self.ship.rect.height
        dostepne_miejsce_y = self.ustawienia.screen_wysokosc - wysokosc_statku - (8 * wysokosc_obcego )
        numer_rzedow = dostepne_miejsce_y// (1* wysokosc_obcego)

        for rzedy in range(numer_rzedow):
            for ilosc_obcych in range(numer_obcych_x):
                self.stworzenie_obcego(ilosc_obcych,szerokosc_obcego, wysokosc_obcego ,rzedy)

    #creating single alien
    def stworzenie_obcego(self,ilosc_obcych,szerokosc_obcego, wysokosc_obcego ,rzedy):
        obcy = Obcy(self)
        obcy.x = szerokosc_obcego + 2 * szerokosc_obcego * ilosc_obcych
        obcy.rect.x = obcy.x
        obcy.rect.y = 2.5 *wysokosc_obcego + 1.8 * wysokosc_obcego * rzedy
        self.alieni.add(obcy)

    #updating aliens position
    def aktualizcja_obcyh(self):
        self.sprawedz_krawedzie_floty()
        self.alieni.update()
        if pygame.sprite.spritecollideany(self.ship,self.alieni):
           self.uderzenie_statku()

        self.sprawdz_dol_ekranu_obcy()

    #checking if alien hit screen bottom
    def sprawdz_dol_ekranu_obcy(self):
        ekran_rect=self.screen.get_rect()
        for obcy in self.alieni.sprites():
            if obcy.rect.bottom >= ekran_rect.bottom:
                self.uderzenie_statku()
                break

    #checking alien army edge
    def sprawedz_krawedzie_floty(self):
        for obcy in self.alieni.sprites():
            if obcy.sprawdz_krawedzie():
                self.zmien_kierunek_floty()
                break

    #changing direction of army
    def zmien_kierunek_floty(self):
        for obcy in self.alieni.sprites():
            obcy.rect.y += self.ustawienia.spadek_obcyh
        self.ustawienia.kierunek_floty *= -1

    #main update, where ship, bullets and aliens are shown
    def aktualizacja(self):
        # wpisanie koloru tła
        self.screen.fill(self.ustawienia.kolor_tla)
        self.screen.blit(self.bacg_img,[ 0,0])
        self.ship.pokaz_mnie()
        for pocisk in self.pociski.sprites():
            pocisk.pocisk_rysuj()
        self.alieni.draw(self.screen)

        self.tablicawynikow.pokaz()

        if not self.staty.czy_zyjesz:
            self.przysick_poczatkowy.rysuj_przycisk()
        pygame.display.flip()


#automatical main function execution
if(__name__ == '__main__'):
    inw = InwazjaObcych()
    inw.rusz_gre()