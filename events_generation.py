from random import *
import time
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
        self.solve_coef()
        self.bet = 0

    def solve_coef(self):
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

class PlaceGen:
    def __init__(self):
        self.places = ["Стадион Труд", "Стадион Северный", "Стадион Нижний Новгород", "Поселок", "Реактор", "ФОК", "Полигон", "Парк", "Сантьяго Бернабеу", "Камп Ноу"]
        self.adjectives1 = ["Забытый", "Великий", "Переоцененный", "Мертвый", "Старый", "Огромный", "Новый", "Страшный"]
    
    def generate(self):
        random_place = random.choice (self.places)
        random_adjective1 = random.choice (self.adjectives1)
        return f"{random_adjective1} {random_place}"
    
class NameGen:
    def __init__(self):
        self.names = ["Мажоры", "Упыри", "Бедолаги", "Борцухи", "Легкие курильщика", "Жуки", "Смурфы", "Гении", "Лудоманы", "Профессионалы", "Парни", "Линуксоводы", "Приспособленцы", "Нефоры", "Спортики", "Лодыри", "Либерахи", "Питонисты", "Рабочие"]
        self.adjectives2 = ["Взорванные", "Заряженные", "Неуверенные", "Летучие", "Странные", "Напуганные", "Липкие", "Убитые"]

    def generate(self):
        random_name = random.choice (self.names)
        random_adjective2 = random.choice (self.adjectives2)
        return f"{random_adjective2} {random_name}"

class SportGen:
    def __init__(self):
        self.adjectives = ["Пьяный", "Польский", "Юношеский", "Подводный", "Арабский"]
        self.sports = ["футбол", "хоккей", "хоббихорсинг", "баскетбол ногой", "CS"]

    def generate(self):
        random_adjective = random.choice(self.adjectives)
        random_sport = random.choice(self.sports)
        return f"{random_adjective} {random_sport}"
    
class MatchGen():
    def __init__(self) -> None:
        self.sportGen = SportGen()
        self.nameGen = NameGen()
        self.placeGen = PlaceGen()
    def generate(self):
        m = Match()
        m.date = time.time()
        m.sport = self.sportGen.generate()
        m.place = self.placeGen.generate()
        m.team1 = self.nameGen.generate()
        m.team2 = self.nameGen.generate()
        return m
