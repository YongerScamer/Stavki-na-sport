import pygame as pg
from setttings import *

class App():
    def __init__(self) -> None:
        pg.init()
        self.sc = pg.display.set_mode((H, W))
        self.clock = pg.Time.clock()
    def run(self):
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            self.sc.fill((0, 0, 0))
            pg.display.flip()
            self.clock.tick(60)