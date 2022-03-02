
class StatyGry:
    def __init__(self,gra):
        self.ustawienia=gra.ustawienia
        self.zresetuj_staty()
        self.czy_zyjesz=False
        self.best_score=0
        self.level=1

    def zresetuj_staty(self):
        self.statki_pozostale = self.ustawienia.limitstatkow
        self.wynik=0