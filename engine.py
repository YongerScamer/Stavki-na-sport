import pygame_widgets

from events_generation import *
from setttings import *
import pygame as pg
import time
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

images = {}


def load_images():
    global images
    images = {}
    for file in os.listdir("images"):
        images[file] = pg.image.load(f"images/{file}").convert_alpha()
    return images


class Player:
    def __init__(self) -> None:
        self.money = 100000
        self.name = "Вышковец"


def generate_tab(match, f):
    sc = pg.Surface((750, 100))
    sc.fill((227, 253, 253))
    sc.blit(pg.font.SysFont("arial", 25).render(f"{match.team1} vs {match.team2}", 1, (0, 0, 0)), (2, 2))
    sc.blit(pg.font.SysFont("arial", 12).render(match.sport, 1, (100, 100, 100)), (5, 35))
    sc.blit(pg.font.SysFont("arial", 14).render(f"Победа 1: {match.coef_win1} Ничья: {match.coef_draw} Победа 2: {match.coef_win2}", 1, (0, 0, 0)), (5, 55))
    button = Button([300, 0, 700, 100], sc, f)
    return button

def bet_on(matchBet):
    matchBet[0].bet = matchBet[1]

class MatchList:
    def __init__(self, f, player) -> None:
        self.maths = MathHandler(self, player)
        self.maths.generate()
        self.tabs = []
        self.y = 0
        self.f = f
        for i in self.maths.maths:
            self.tabs.append(generate_tab(i, f))


    def update(self):
        for i in range(len(self.tabs)):
            self.tabs[i].coord[1] = i * 110 + 10 - self.y
            self.tabs[i].update(self.maths.maths[i])
        for event in pg.event.get():
            if event.type == pg.MOUSEWHEEL:
                self.y -= event.y * 40
                self.y = min(1550, max(0, self.y))
            if event.type == pg.QUIT:
                pg.quit()
                exit()
    def refresh(self):
        self.maths.check_old_bet()

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
        self.buttons = [
            Button((320, 300, 210, 90), images["team1_button.png"], bet_on),
            Button((580, 300, 210, 90), images["draw_button.png"], bet_on),
            Button((840, 300, 210, 90), images["team2_button.png"], bet_on)
        ]
        self.slider = Slider(self.sc, 340, 510, 690, 20, min=1000, max=100000, step=1000)
        self.output = TextBox(self.sc, 630, 450, 100, 50, fontSize=30)
        self.activ = True
    def update(self):
        pg.draw.rect(self.sc, (240, 240, 240), (300, 30, 770, 660))
        self.sc.blit(pg.font.SysFont("arial", 30).render(self.match.team1 + " VS " + self.match.team2, 1, (0, 0, 0)), (320, 50))
        self.sc.blit(pg.font.SysFont("arial", 20).render(self.match.sport, 1, (30, 30, 30)), (320, 90))
        self.sc.blit(images["locate_ico.png"], (310, 640))
        self.sc.blit(pg.font.SysFont("arial", 26).render(self.match.place, 1, (30, 30, 30)), (340, 646))
        self.sc.blit(pg.font.SysFont("arial", 17).render(f"Победа 1: {self.match.coef_win1} Ничья: {self.match.coef_draw} Победа 2: {self.match.coef_win2}", 1, (0, 0, 0)), (550, 120))
        self.sc.blit(pg.font.SysFont("arial", 10).render("Закончится: " + time.ctime(self.match.date), 1, (150, 150, 150)), (890, 40))
        self.slider.draw()
        self.output.setText(self.slider.getValue())
        self.output.draw()
        if self.match.bet != 0 and self.activ:
            for i in self.buttons:
                i.activ = False
            self.activ = False
        self.buttons[0].update([self.match, (0, self.slider.getValue())])
        self.buttons[1].update([self.match, (2, self.slider.getValue())])
        self.buttons[2].update([self.match, (1, self.slider.getValue())])
        print(self.match.result)


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

    def on_match_list(self):
        self.current_mod = 2

    def on_bet_list(self):
        self.current_mod = 3

    def on_statistic(self):
        self.current_mod = 4


class Button:
    def __init__(self, coord, image, function) -> None:
        self.coord = coord
        self.image = image
        self.f = function
        self.sc = pg.display.get_surface()
        self.onButton = False
        self.activ = True
    def update(self, arg = None):
        self.sc.blit(self.image, (self.coord[0], self.coord[1]))
        if self.activ:
            x, y = pg.mouse.get_pos()
            if self.coord[0] < x < self.coord[0] + self.coord[2] and self.coord[1] < y < self.coord[1] + self.coord[3]:
                if pg.mouse.get_pressed(3)[0]:
                    self.onButton = True
                else:
                    if self.onButton:
                        if arg == None:
                            self.f()
                        else:
                            self.f(arg)
                        self.onButton = False


class MathHandler:
    def __init__(self, matchlist, player, maths=None, autofill=False, maxMatch=15) -> None:
        if maths is None:
            maths = []
        self.maths = maths
        self.autofill = autofill
        self.maxMatch = maxMatch
        self.player = player
        self.matchlist = matchlist
    def check_old_bet(self):
        money = 0
        t = time.time()
        gen = MatchGen()
        for i in self.maths:
            if i.bet != 0 and t > i.date:
                if i.bet[0] == i.result:
                    if i.bet == 0:
                        money += i.bet[1] * i.coef_win1
                    elif i.bet == 1:
                        money += i.bet[1] * i.coef_win2
                    else:
                        money += i.bet[1] * i.coef_draw
                    self.matchlist.tabs.pop(self.maths.index(i))
                    self.maths.pop(self.maths.index(i))
        if self.autofill:
            for i in range(self.maxMatch - len(self.maths)):
                self.maths.append(gen.generate())
        self.player.money += money

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
