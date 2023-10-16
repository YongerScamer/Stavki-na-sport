from events_generation import *
import pygame as pg

class Player():
    pass

class MathList():
    def __init__(self) -> None:
        pass
    def update(self):
        pass

class PlayerProfil():
    def __init__(self) -> None:
        pass
    def update(self):
        pass

class Menu():
    def __init__(self) -> None:
        self.current_mod = 0
        self.sc = pg.display.get_surface()
    def update(self):
        pg.draw.rect(self.sc, (227, 253, 253), (0, 0, 290, 720))

class Button():
    def __init__(self, coord, image, function) -> None:
        self.coord = coord
        self.image = image
        self.f = function
        self.sc = pg.display.get_surface()
        self.onButton = False
    def update(self):
        self.sc.blit(self.image, self.coord[:1])
        x, y = pg.mouse.get_pos()
        if self.coord[0] < x < self.coord[2] and self.coord[1] < y < self.coord[3]:
            if pg.mouse.get_pressed(0):
                self.onButton = True
            else:
                if self.onButton:
                    self.f()
