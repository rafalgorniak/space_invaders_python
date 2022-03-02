import pygame.font

class Przycisk:
    def __init__(self,gra,wiadomosc):
        self.okno=gra.screen
        self.okno_kwadrat=self.okno.get_rect()

        self.width, self.height =300,60
        self.button_color=(45,100,43)
        self.kolor_tekstu=(255,255,255)
        self.czcionka=pygame.font.SysFont(None,48)

        self.prostokat=pygame.Rect(0,0,self.width,self.height)
        self.prostokat.center = self.okno_kwadrat.center

        self._prep_msg(wiadomosc)

    def _prep_msg(self,wiadomosc):
        self.msg_image = self.czcionka.render(wiadomosc,True,self.kolor_tekstu,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.prostokat.center

    def rysuj_przycisk(self):
        self.okno.fill(self.button_color,self.prostokat)
        self.okno.blit(self.msg_image,self.msg_image_rect)