import pygame as pg
from setttings import *
from engine import *
import sys
import pygame_widgets

class App:
    def __init__(self) -> None:
        pg.init()
        self.sc = pg.display.set_mode((W, H))
        pg.display.set_caption("1XВШЭ")
        pg.display.set_icon(pg.image.load("images/HSE_icon.png").convert())
        self.clock = pg.time.Clock()
        self.player = Player()
        self.menu = Menu(self.player)

    def run(self):
        while 1:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.menu.save()
                    pg.quit()
                    sys.exit()
            self.sc.fill((255, 255, 255))
            self.menu.update()
            pg.display.flip()
            pygame_widgets.update(events)
            self.clock.tick()