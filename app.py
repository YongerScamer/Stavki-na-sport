import pygame as pg
from setttings import *
from engine import *

class App():
    def __init__(self) -> None:
        pg.init()
        self.sc = pg.display.set_mode((W, H))
        pg.display.set_caption("1XВШЭ")
        pg.display.set_icon(pg.image.load("images/HSE_icon.png").convert())
        self.clock = pg.time.Clock()
        self.player = Player()
        self.menu = Menu()
        self.mods = [LoadWin(self.menu), MathList(), PlayerProfil()]
    def run(self):
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            self.sc.fill((255, 255, 255))
            self.menu.update()
            self.mods[self.menu.current_mod].update()
            pg.display.flip()
            self.clock.tick(60)