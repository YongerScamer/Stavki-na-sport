import pygame as pg
from setttings import *
from engine import *
import sys

class App:
    def __init__(self) -> None:
        pg.init()
        self.sc = pg.display.set_mode((W, H))
        pg.display.set_caption("1XВШЭ")
        pg.display.set_icon(pg.image.load("images/HSE_icon.png").convert())
        self.clock = pg.time.Clock()
        self.player = Player()
        self.menu = Menu()
        self.mods = [LoadWin(self.change_mod), PlayerProfil(self.player), MatchList(self.match_menu, self.player), BetList(), Statistic(), MatchMenu(self.player, self.menu)]
        self.mods[5].matchlist = self.mods[2]

    def run(self):
        while 1:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.sc.fill((255, 255, 255))
            self.menu.update()
            self.mods[self.menu.current_mod].update()
            self.mods[2].refresh()
            pg.display.flip()
            pygame_widgets.update(events)
            self.clock.tick()

    def change_mod(self, n):
        self.menu.current_mod = n

    def match_menu(self, match):
        self.menu.current_mod = 5
        self.mods[5].match = match