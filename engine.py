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
    def save(self):
        with open("player_data", "w") as f:
            f.write(str(self.money))
    def load(self):
        with open("player_data", "r") as f:
            self.money = float(f.read())

def generate_tab(match, f):
    sc = pg.Surface((750, 100))
    sc.fill((227, 253, 253))
    sc.blit(pg.font.SysFont("arial", 25).render(f"{match.team1} vs {match.team2}", 1, (0, 0, 0)), (2, 2))
    sc.blit(pg.font.SysFont("arial", 12).render(match.sport, 1, (100, 100, 100)), (5, 35))
    sc.blit(pg.font.SysFont("arial", 14).render(
        f"Победа 1: {match.coef_win1} Ничья: {match.coef_draw} Победа 2: {match.coef_win2}", 1, (0, 0, 0)), (5, 55))
    button = Button([300, 0, 700, 100], sc, f)
    return button


def bet_on(matchBet):
    matchBet[0].bet = matchBet[1]
    matchBet[2].money -= matchBet[1][1]


# ------------------------MENU------------------------------------------
class Menu:
    def __init__(self, player) -> None:
        images = load_images()
        self.player = player
        self.player.load()
        self.current_mod = 0
        self.sc = pg.display.get_surface()
        self.buttons = [Button((0, 50, 270, 90), images["profile_button.png"], self.on_profile),
                        Button((0, 150, 270, 90), images["match_list_button.png"], self.on_match_list),
                        Button((0, 250, 270, 90), images["bet_list_button.png"], self.on_bet_list),
                        Button((0, 350, 270, 90), images["statistic_button.png"], self.on_statistic)]
        self.loadwin = LoadWin(self)
        self.playerprofil = PlayerProfil(self)
        self.matchlist = MatchList(self)
        self.betlist = BetList(self)
        self.statistic = Statistic(self)
        self.matchmenu = MatchMenu(self)
        self.current_mod = self.loadwin
        self.matchlist.maths.load()

    def update(self):
        if self.current_mod != 0:
            pg.draw.rect(self.sc, (227, 253, 253), (0, 0, 290, 720))
            for button in self.buttons:
                button.update()
            self.current_mod.update()
            self.matchlist.refresh()

    def on_profile(self):
        self.current_mod = self.playerprofil

    def on_match_list(self):
        self.current_mod = self.matchlist

    def on_bet_list(self):
        self.current_mod = self.betlist

    def on_statistic(self):
        self.current_mod = self.statistic

    def on_match_menu(self, match):
        self.current_mod = self.matchmenu
        self.matchmenu.match = match

    def save(self):
        self.player.save()
        self.matchlist.maths.save()


# ---------------------------MATCH_LIST--------------------------------------------
class MatchList:
    def __init__(self, menu: Menu) -> None:
        self.maths = MathcHandler(menu)
        self.tabs = []
        self.y = 0
        self.menu = menu

    def update(self):
        for i in range(len(self.tabs)):
            self.tabs[i].coord[1] = i * 110 + 10 - self.y
            self.tabs[i].update(self.maths.maths[i])
        for event in pg.event.get():
            if event.type == pg.MOUSEWHEEL:
                self.y -= event.y * 40
                self.y = min(1550, max(0, self.y))
            if event.type == pg.QUIT:
                self.menu.save()
                pg.quit()
                exit()

    def refresh(self):
        self.maths.check_old_bet()

    def new_tab(self, match):
        self.tabs.append(generate_tab(match, self.menu.on_match_menu))
        self.maths.maths.append(match)


# ------------------------------PLAYER_PROFILE---------------------------------------------
class PlayerProfil:
    def __init__(self, menu) -> None:
        self.menu = menu
        self.sc = pg.display.get_surface()
        self.name = pg.font.SysFont("arial", 60).render(self.menu.player.name, 1, (0, 0, 0))
        self.balance_font = pg.font.SysFont("arial", 25)
        self.ava = pg.transform.scale(images["HSE_icon.png"], (400, 400))

    def update(self):
        self.sc.blit(self.name, (300, 20))
        self.sc.blit(self.balance_font.render(f"Баланс: {self.menu.player.money}", 1, (0, 0, 0)), (300, 80))
        self.sc.blit(self.ava, (300, 130))


# -----------------------------BET_LIST---------------------------------------
class BetList:
    def __init__(self, menu):
        self.menu = menu
        self.sc = pg.display.get_surface()
        self.i = 0

    def update(self):
        l = 0
        for match in self.menu.matchlist.maths.maths:
            if match.bet != 0:
                pg.draw.rect(self.sc, (227, 253, 253), (300, l * 110 + 10 - self.i, 750, 100))
                self.sc.blit(pg.font.SysFont("arial", 25).render(f"{match.team1} vs {match.team2}", 1, (0, 0, 0)),
                             (302, 2 + l * 110 + 10 - self.i))
                self.sc.blit(pg.font.SysFont("arial", 12).render(match.sport, 1, (100, 100, 100)),
                             (305, 35 + l * 110 + 10 - self.i))
                self.sc.blit(pg.font.SysFont("arial", 14).render(
                    f"Победа 1: {match.coef_win1} Ничья: {match.coef_draw} Победа 2: {match.coef_win2}", 1, (0, 0, 0)),
                    (305, 55 + l * 110 + 10 - self.i))
                text = ""
                if match.bet[0] == 0:
                    text = " на команду 1"
                elif match.bet[0] == 1:
                    text = " на команду 2"
                elif match.bet[0] == 2:
                    text = " на ничью"
                self.sc.blit(pg.font.SysFont("arial", 20).render(f"{match.bet[1]} {text}", 1, (0, 255, 0)),
                             (305, 70 + l * 110 + 10 - self.i))
                l += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.menu.save()
                pg.quit()
                exit()
            if event.type == pg.MOUSEWHEEL:
                self.i -= event.y * 40
                self.i = min(l * 120 + 600, max(0, self.i))


# -----------------------STATISTIC----------------------------------------------------
class Statistic:
    def __init__(self, menu):
        pass

    def update(self):
        pass


# --------------------------------MATCH_MENU-----------------------------------------------------
class MatchMenu:
    def __init__(self, menu: Menu):
        self.menu = menu
        self.match = None
        self.sc = pg.display.get_surface()
        self.buttons = [
            Button((320, 300, 210, 90), images["team1_button.png"], bet_on),
            Button((580, 300, 210, 90), images["draw_button.png"], bet_on),
            Button((840, 300, 210, 90), images["team2_button.png"], bet_on)
        ]
        self.slider = Slider(self.sc, 340, 510, 690, 20, min=500, max=min(100000, self.menu.player.money), step=1000)
        self.output = TextBox(self.sc, 630, 450, 100, 50, fontSize=30)

    def update(self):
        if not self.match in self.menu.matchlist.maths.maths:
            self.menu.on_match_list()
        pg.draw.rect(self.sc, (240, 240, 240), (300, 30, 770, 660))
        self.sc.blit(pg.font.SysFont("arial", 30).render(self.match.team1 + " VS " + self.match.team2, 1, (0, 0, 0)),
                     (320, 50))
        self.sc.blit(pg.font.SysFont("arial", 20).render(self.match.sport, 1, (30, 30, 30)), (320, 90))
        self.sc.blit(images["locate_ico.png"], (310, 640))
        self.sc.blit(pg.font.SysFont("arial", 26).render(self.match.place, 1, (30, 30, 30)), (340, 646))
        self.sc.blit(pg.font.SysFont("arial", 17).render(
            f"Победа 1: {self.match.coef_win1} Ничья: {self.match.coef_draw} Победа 2: {self.match.coef_win2}", 1,
            (0, 0, 0)), (550, 120))
        self.sc.blit(
            pg.font.SysFont("arial", 10).render("Закончится: " + time.ctime(self.match.date), 1, (150, 150, 150)),
            (890, 40))
        self.slider.draw()
        self.output.setText(self.slider.getValue())
        self.output.draw()
        self.slider.max = max(1000, min(100000, self.menu.player.money))
        self.slider.value = min(self.slider.max, self.slider.value)
        if self.match.bet == 0 and self.menu.player.money >= 1000:
            for i in self.buttons:
                i.activ = True
        self.buttons[0].update([self.match, (0, self.slider.getValue()), self.menu.player])
        self.buttons[1].update([self.match, (2, self.slider.getValue()), self.menu.player])
        self.buttons[2].update([self.match, (1, self.slider.getValue()), self.menu.player])
        for i in self.buttons:
            i.activ = False
        print(self.match.result)


# ------------BUTTON--------------------------------------
class Button:
    def __init__(self, coord, image, function) -> None:
        self.coord = coord
        self.image = image
        self.f = function
        self.sc = pg.display.get_surface()
        self.onButton = False
        self.activ = True

    def update(self, arg=None):
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


# ---------------MATCH_HANDLER_______________________
class MathcHandler:
    def __init__(self, menu: Menu, maths=None, max_match=15) -> None:
        if maths is None:
            maths = []
        self.maths = maths
        self.max_match = max_match
        self.menu = menu

    def check_old_bet(self):
        money = 0
        t = time.time()
        gen = MatchGen()
        for i in self.maths:
            if t > i.date:
                if i.bet != 0:
                    if i.bet[0] == i.result:
                        if i.bet == 0:
                            money += i.bet[1] * i.coef_win1
                        elif i.bet == 1:
                            money += i.bet[1] * i.coef_win2
                        else:
                            money += i.bet[1] * i.coef_draw
                self.menu.matchlist.tabs.pop(self.maths.index(i))
                self.maths.pop(self.maths.index(i))
        for i in range(self.max_match - len(self.maths)):
            self.menu.matchlist.new_tab(gen.generate())
        self.menu.player.money += money
        self.menu.player.money = round(self.menu.player.money, 2)
    def save(self):
        for i in range(len(self.maths)):
            with open(f"saved_matchs/match{i}.mt", "w") as f:
                f.write(self.maths[i].place)
                f.writelines("\n")
                f.write(str(self.maths[i].date))
                f.writelines("\n")
                f.write(self.maths[i].team1)
                f.writelines("\n")
                f.write(self.maths[i].team2)
                f.writelines("\n")
                f.write(self.maths[i].sport)
                f.writelines("\n")
                f.write(str(self.maths[i].result))
                f.writelines("\n")
                f.write(str(self.maths[i].coef_win1))
                f.writelines("\n")
                f.write(str(self.maths[i].coef_win2))
                f.writelines("\n")
                f.write(str(self.maths[i].coef_draw))
                f.writelines("\n")
                if self.maths[i].bet != 0:
                    f.write(str(self.maths[i].bet[0]))
                    f.writelines("\n")
                    f.write(str(self.maths[i].bet[1]))
                else:
                    f.write("999")
    def load(self):
        for i in range(15):
            try:
                with open(f"saved_matchs/match{i}.mt", "r") as f:
                    m = f.read().split("\n")
                    math = Match()
                    math.place = m[0]
                    math.date = float(m[1])
                    math.team1 = m[2]
                    math.team2 = m[3]
                    math.sport = m[4]
                    math.result = int(m[5])
                    math.coef_win1 = float(m[6])
                    math.coef_win2 = float(m[7])
                    math.coef_draw = float(m[8])
                    if m[9] == "999":
                        math.bet = 0
                    else:
                        math.bet = (int(m[9]), int(m[10]))
                    self.menu.matchlist.new_tab(math)
            except:
                pass
# ---------LOAD_WINDOW__________________
class LoadWin:
    def __init__(self, menu: Menu) -> None:
        self.rtext = None
        self.menu = menu
        self.l = 0
        self.d = 1000
        self.texts = ["Савина настраивает микрофон", "Малышев высчитывает вероятность выигрыша",
                      "Беспалов собирает листочки со ставками"]
        self.index = 0
        self.sc = pg.display.get_surface()
        self.font = pg.font.SysFont("Arial", 21)

    def update(self):
        if self.index >= len(self.texts):
            self.menu.on_profile()
            return 0
        self.sc.blit(images["1XHSE.jpg"], (0, 0))
        self.rtext = self.font.render("." * (self.l // 5 % 5) + self.texts[self.index] + "." * (self.l // 5 % 5), 1,
                                      (0, 0, 0))
        self.sc.blit(self.rtext, (540 - self.rtext.get_size()[0] / 2, 670))
        self.l += 1
        if self.l >= self.d:
            self.l = 0
            self.index += 1
