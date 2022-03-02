class Ustawienia():
    def __init__(self):
        self.screen_szerokosc = 1200
        self.screen_wysokosc = 800

        self.kolor_tla = (100,120,100)
        self.pocisk_szerokosc = 5
        self.pocisk_dlugosc = 20

        self.ilosc_pociskow = 2
        self.pocisk_kolor = (231, 227, 16)

        self.spadek_obcyh = 15
        self.pkt_for_alien = 20
        self.limitstatkow = 3

        self.zmiana_predkosci_obcych = 1.2

        self.inicjacja_dynamiczna()

    def inicjacja_dynamiczna(self):
        self.szybkos_obcego = 0.5
        self.szybkosc_statku = 1.5
        self.pocisk_szybkosc = 3
        self.kierunek_floty = 1

    def zwieksz_predkosc(self):
        self.szybkos_obcego *= self.zmiana_predkosci_obcych
        self.szybkosc_statku *=self.zmiana_predkosci_obcych
        self.pocisk_szybkosc *=self.zmiana_predkosci_obcych

        self.pkt_for_alien =int(self.pkt_for_alien * self.zmiana_predkosci_obcych)
