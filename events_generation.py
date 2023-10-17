from random import *
class Match():
    def __init__(self):
        self.place = ""
        self.date = 0
        self.team1 = ""
        self.team2 = ""
        self.sport = ""
        """"1 - победа первой, 2 - победа второй, 3 - ничья"""
        self.result = randint(1, 3)
        self.coef_win1 = 0
        self.coef_win2 = 0
        self.coef_draw = 0
        self.get_coef()
        self.bet = 0

    def get_coef(self):
        if self.result == 1:
            self.coef_win1 = round(random.uniform((1.5, 3), 2))
            self.coef_win2 = 1.4 * self.coef_win1
            self.coef_draw = round(random.inuforn((1.5, 2), 2))
        if self.result == 2:
            self.coef_win2 = round(random.uniform((1.5, 3), 2))
            self.coef_win1 = 1.4 * self.coef_win1
            self.coef_draw = round(random.inuforn((1.5, 2), 2))
        if self.result == 3:
            self.coef_draw = round(random.uniform((1.5, 3), 2))
            self.coef_win2 = 1.4 * self.coef_win1
            self.coef_win1 = round(random.inuforn((1.5, 2), 2))


















