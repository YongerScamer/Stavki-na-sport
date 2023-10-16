import pygame as pg
from setttings import *

class App():
    def __init__(self) -> None:
        pg.init()
        self.sc = pg.display.set_mode((W, H))
        pg.display.set_caption("1XВШЭ")
        pg.display.set_icon(pg.image.load("images/HSE_icon.png").convert())
        self.clock = pg.time.Clock()
        self.intro = pg.image.load("images/1XHSE.jpg").convert()
    def run(self):
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            self.sc.blit(self.intro, (0, 0))
            pg.display.flip()
            self.clock.tick(60)