from events_generation import *
from setttings import *
import pygame as pg

images = {}

def load_images():
    global images
    images = {}
    for file in os.listdir("images"):
        images[file] = pg.image.load(f"images/{file}").convert()
    return images

class Player():
    def __init__(self) -> None:
        self.money = 100000

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
        images = load_images()
        self.current_mod = 0
        self.sc = pg.display.get_surface()
        self.buttons = [Button((0, 50, 270, 140), images["profile_button.png"], self.on_profile), 
                        Button((0, 150, 270, 240), images["match_list_button.png"], self.on_match_list),
                        Button((0, 250, 270, 340), images["bet_list_button.png"], self.on_bet_list), 
                        Button((0, 350, 270, 440), images["statistic_button.png"], self.on_statistic)]
    def update(self):
        pg.draw.rect(self.sc, (227, 253, 253), (0, 0, 290, 720))
        for button in self.buttons:
            button.update()
    def on_profile(self):
        self.current_mod = 0
        print("profile")
    def on_match_list(self):
        self.current_mod = 0
        print("match_list")
    def on_bet_list(self):
        self.current_mod = 0
        print("bet_list")
    def on_statistic(self):
        self.current_mod = 0
        print("statistic")


class Button():
    def __init__(self, coord, image, function) -> None:
        self.coord = coord
        self.image = image
        self.f = function
        self.sc = pg.display.get_surface()
        self.onButton = False
    def update(self):
        self.sc.blit(self.image, (self.coord[0], self.coord[1]))
        x, y = pg.mouse.get_pos()
        if self.coord[0] < x < self.coord[2] and self.coord[1] < y < self.coord[3]:
            if pg.mouse.get_pressed(3)[0]:
                self.onButton = True
            else:
                if self.onButton:
                    self.f()
                    self.onButton = False

class MathHandler():
    def __init__(self) -> None:
        self.maths = []
    def get_info(self, place = False, date = False, team1 = False, team2 = False, sport = False, result = False, cf = False, bet = False):
        pass


