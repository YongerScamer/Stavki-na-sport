from random import *
import time


class Match():
    def __init__(self):
        self.place = ""
        self.date = 0
        self.team1 = ""
        self.team2 = ""
        self.sport = ""
        self.result = randint(0, 2)
        self.coef_win1 = 0
        self.coef_win2 = 0
        self.coef_draw = 0
        self.solve_coef()
        self.bet = 0

    def solve_coef(self):
        if self.result == 0:
            self.coef_win1 = round(uniform(1.5, 3), 2)
            self.coef_win2 = round(1.4 * self.coef_win1, 2)
            self.coef_draw = round(uniform(1.5, 2), 2)
        if self.result == 1:
            self.coef_win2 = round(uniform(1.5, 3), 2)
            self.coef_win1 = round(1.4 * self.coef_win2, 2)
            self.coef_draw = round(uniform(1.5, 2), 2)
        if self.result == 2:
            self.coef_draw = round(uniform(1.5, 3), 2)
            self.coef_win2 = round(1.4 * self.coef_draw, 2)
            self.coef_win1 = round(uniform(1.5, 2), 2)


class PlaceGen:
    def __init__(self):
        self.places = ["Стадион Труд", "Стадион Северный", "Стадион Нижний Новгород", "Поселок", "Реактор", "ФОК",
                       "Полигон", "Парк", "Сантьяго Бернабеу", "Камп Ноу", "Лес", "Пляж", "Музей", "Зоопарк", "Магазин",
                       "Вокзал", "Бар", "Рынок", "Мост", "Банк", "Храм", "Заповедник", "Фонтан", "Аквапарк", "Офис",
                       "Монастырь", "Театр", "Корт", "Бассейн", "Молл"]
        self.adjectives1 = ["Забытый", "Великий", "Переоцененный", "Мертвый", "Старый", "Огромный", "Новый", "Страшный",
                            "Уютный", "Туманный", "Загрязненный", "Религиозный", "Древний", "Умиротворенный",
                            "Холмистый", "Южный", "Северный", "Восточный", "Западный", "Волшебный", "Солнечный",
                            "Ветреный", "Жаркий", "Морской", "Горный", "Речной", "Каменистый", "Пустынный", "Обжитый",
                            "Восточноевропейский", "Траурный", "Орлиный", "Долинный", "Железнодорожный", "Элитный",
                            "Космический"]


    def generate(self):
        random_place = choice(self.places)
        random_adjective1 = choice(self.adjectives1)
        return f"{random_adjective1} {random_place}"


class NameGen:
    def __init__(self):
        self.names = ["Мажоры", "Упыри", "Бедолаги", "Борцухи", "Легкие курильщика", "Жуки", "Смурфы", "Гении",
                      "Лудоманы", "Профессионалы", "Парни", "Линуксоводы", "Приспособленцы", "Нефоры", "Спортики",
                      "Лодыри", "Либерахи", "Питонисты", "Рабочие", "Бродяги", "Жулики", "Табуретки", "Вши",
                      "Пассатижи", "Молотки", "Персики", "Буйволы", "Садовники", "Модельеры", "Воители", "Капитаны",
                      "Начальники", "Философы", "Наставники", "Моряки", "Инспекторы", "Механики", "Дворники", "Соседи",
                      "Мужчины", "Артисты", "Трактористы", "Писатели", "Хакеры", "Программисты", "Плотники", "Коллеги",
                      "Подростки", "Атлеты"]
        self.adjectives2 = ["Взорванные", "Заряженные", "Неуверенные", "Летучие", "Странные", "Напуганные", "Липкие",
                            "Убитые", "Красивые", "Щедрые", "Энергичные", "Вежливые", "Общительные", "Порядочные",
                            "Мудрые", "Доступные", "Безмятежные", "Активные", "Опытные", "Позитивные", "Гармоничные",
                            "Спонтанные", "Заботливые", "Амбициозные", "Терпеливые", "Невинные", "Преданные",
                            "Успешные", "Изысканные", "Разносторонние", "Первоклассные", "Честные"]

    def generate(self):
        random_name = choice(self.names)
        random_adjective2 = choice(self.adjectives2)
        return f"{random_adjective2} {random_name}"


class SportGen:
    def __init__(self):
        self.adjectives = ["Пьяный", "Польский", "Юношеский", "Подводный", "Арабский"]
        self.sports = ["футбол", "хоккей", "хоббихорсинг", "баскетбол ногой", "CS"]

    def generate(self):
        random_adjective = choice(self.adjectives)
        random_sport = choice(self.sports)
        return f"{random_adjective} {random_sport}"


class MatchGen:
    def __init__(self) -> None:
        self.sportGen = SportGen()
        self.nameGen = NameGen()
        self.placeGen = PlaceGen()

    def generate(self):
        m = Match()
        m.date = time.time() + randint(200, 700)
        m.sport = self.sportGen.generate()
        m.place = self.placeGen.generate()
        m.team1 = self.nameGen.generate()
        m.team2 = self.nameGen.generate()
        return m
