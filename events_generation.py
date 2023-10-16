from randon import *
class Match():
    def __init__(self, place, date, team1, team2, sport, result, bet, coef_win1,coef_win2, coef_draw ):
        self.place = place
        self.date = date
        self.team1 = team1
        self.team2 = team2
        self.sport = sport
        """"1 - победа первой, 2 - победа второй, 3 - ничья"""
        self.result = randint(1, 3)
        self.coef_win1 = coef_win1
        self.coef_win2 = coef_win2
        self.coef_draw = coef_draw
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


















