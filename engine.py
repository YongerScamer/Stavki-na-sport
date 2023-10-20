from events_generation import *
from setttings import *
import pygame as pg
import time

images = {}


def load_images():
    global images
    images = {}
    for file in os.listdir("images"):
        images[file] = pg.image.load(f"images/{file}").convert()
    return images


class Player:
    def __init__(self) -> None:
        self.money = 100000
        self.name = "Вышковец"

def f():
    print("opa")


def generate_tab(math, f):
    sc = pg.Surface((750, 100))
    sc.fill((227, 253, 253))
    sc.blit(pg.font.SysFont("arial", 25).render(f"{math.team1} vs {math.team2}", 1, (0, 0, 0)), (2, 2))
    sc.blit(pg.font.SysFont("arial", 12).render(math.sport, 1, (100, 100, 100)), (5, 35))
    sc.blit(pg.font.SysFont("arial", 14).render(f"Победа 1: {math.coef_win1} Ничья: {math.coef_draw} Победа 2: {math.coef_win2}", 1, (0, 0, 0)), (5, 55))
    button = Button([300, 0, 700, 100], sc, f, arg = math)
    return button


class MatchList:
    def __init__(self, f) -> None:
        self.maths = MathHandler()
        self.maths.generate()
        self.tabs = []
        self.y = 0
        self.f = f
        for i in self.maths.maths:
            self.tabs.append(generate_tab(i, f))


    def update(self):
        for i in range(len(self.tabs)):
            self.tabs[i].coord[1] = i * 110 + 10 - self.y
            self.tabs[i].update()
        for event in pg.event.get():
            if event.type == pg.MOUSEWHEEL:
                self.y -= event.y * 40
                self.y = min(1550, max(0, self.y))
            if event.type == pg.QUIT:
                pg.quit()
                exit()

class PlayerProfil:
    def __init__(self, player) -> None:
        self.player = player
        self.sc = pg.display.get_surface()
        self.name = pg.font.SysFont("arial", 60).render(self.player.name, 1, (0, 0, 0))
        self.balance_font = pg.font.SysFont("arial", 25)
        self.ava = pg.transform.scale(images["HSE_icon.png"], (400, 400))

    def update(self):
        self.sc.blit(self.name, (300, 20))
        self.sc.blit(self.balance_font.render(f"Баланс: {self.player.money}", 1, (0, 0, 0)), (300, 80))
        self.sc.blit(self.ava, (300, 130))


class BetList:
    def __int__(self):
        pass

    def update(self):
        pass


class Statistic:
    def __int__(self):
        pass

    def update(self):
        pass

class MatchMenu:
    def __init__(self):
        self.match = None
        self.sc = pg.display.get_surface()
    def update(self):
        pg.draw.rect(self.sc, (200, 200, 200), (300, 30, 770, 660))

class Menu:
    def __init__(self) -> None:
        images = load_images()
        self.current_mod = 0
        self.sc = pg.display.get_surface()
        self.buttons = [Button((0, 50, 270, 90), images["profile_button.png"], self.on_profile),
                        Button((0, 150, 270, 90), images["match_list_button.png"], self.on_match_list),
                        Button((0, 250, 270, 90), images["bet_list_button.png"], self.on_bet_list),
                        Button((0, 350, 270, 90), images["statistic_button.png"], self.on_statistic)]

    def update(self):
        if self.current_mod != 0:
            pg.draw.rect(self.sc, (227, 253, 253), (0, 0, 290, 720))
            for button in self.buttons:
                button.update()

    def on_profile(self):
        self.current_mod = 1
        print("profile")

    def on_match_list(self):
        self.current_mod = 2

    def on_bet_list(self):
        self.current_mod = 3
        print("bet_list")

    def on_statistic(self):
        self.current_mod = 4
        print("statistic")


class Button:
    def __init__(self, coord, image, function, arg = None) -> None:
        self.coord = coord
        self.image = image
        self.f = function
        self.sc = pg.display.get_surface()
        self.onButton = False
        self.arg = arg

    def update(self):
        self.sc.blit(self.image, (self.coord[0], self.coord[1]))
        x, y = pg.mouse.get_pos()
        if self.coord[0] < x < self.coord[0] + self.coord[2] and self.coord[1] < y < self.coord[1] + self.coord[3]:
            if pg.mouse.get_pressed(3)[0]:
                self.onButton = True
            else:
                if self.onButton:
                    if self.arg == None:
                        self.f()
                    else:
                        self.f(self.arg)
                    self.onButton = False


class MathHandler:
    def __init__(self, maths=[], autofill=False, maxMatch=15) -> None:
        self.maths = maths
        self.autofill = autofill
        self.maxMatch = maxMatch

    def check_old_bet(self):
        money = 0
        t = time.time()
        old_matchs = MathHandler()
        gen = MatchGen()
        for i in self.maths:
            if i.bet != 0:
                if i.bet[0] == i.result:
                    if i.bet == 0:
                        money += i.bet[1] * i.coef_win1
                    elif i.bet == 1:
                        money += i.bet[1] * i.coef_win2
                    else:
                        money += i.bet[1] * i.coef_draw
                    old_matchs.maths.append(i)
                    self.maths.pop(self.maths.index(i))
        if self.autofill:
            for i in range(self.maxMatch - len(self.maths)):
                self.maths.append(gen.generate())
        return old_matchs, money

    def generate(self):
        gen = MatchGen()
        for i in range(self.maxMatch - len(self.maths)):
            self.maths.append(gen.generate())

    def __add__(self, a):
        return MathHandler(maths=self.maths + a.maths)


class LoadWin:
    def __init__(self, menu) -> None:
        self.rtext = None
        self.menu = menu
        self.l = 0
        self.d = 10
        self.texts = ["Савина настраивает микрофон", "Малышев высчитывает вероятность выигрыша",
                      "Беспалов собирает листочки со ставками"]
        self.index = 0
        self.sc = pg.display.get_surface()
        self.font = pg.font.SysFont("Arial", 21)

    def update(self):
        if self.index >= len(self.texts):
            self.menu(1)
            return 0
        self.sc.blit(images["1XHSE.jpg"], (0, 0))
        self.rtext = self.font.render("." * (self.l // 5 % 5) + self.texts[self.index] + "." * (self.l // 5 % 5), 1,
                                      (0, 0, 0))
        self.sc.blit(self.rtext, (540 - self.rtext.get_size()[0] / 2, 670))
        self.l += 1
        if self.l >= self.d:
            self.l = 0
            self.index += 1
