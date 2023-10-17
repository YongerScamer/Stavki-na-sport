import random

class PlaceGen:
    def __init__(self):
        self.places = ["Стадион Труд", "Стадион Северный", "Стадион Нижний Новгород", "Поселок", "Реактор", "ФОК", "Полигон", "Парк", "Сантьяго Бернабеу", "Камп Ноу"]
        self.adjectives1 = ["Забытый", "Великий", "Переоцененный", "Мертвый", "Старый", "Огромный", "Новый", "Страшный"]
    
    def generate_random_place(self):
        random_place = random.choice (self.places)
        random_adjective1 = random.choice (self.adjectives1)
        return f"{random_adjective1} {random_place}"
    
class NameGen:
    def __init__(self):
        self.names = ["Мажоры", "Упыри", "Бедолаги", "Борцухи", "Легкие курильщика", "Жуки", "Смурфы", "Гении", "Лудоманы", "Профессионалы", "Парни", "Линуксоводы", "Приспособленцы", "Нефоры", "Спортики", "Лодыри", "Либерахи", "Питонисты", "Рабочие"]
        self.adjectives2 = ["Взорванные", "Заряженные", "Неуверенные", "Летучие", "Странные", "Напуганные", "Липкие", "Убитые"]

    def generate_random_place(self):
        random_name = random.choice (self.names)
        random_adjective2 = random.choice (self.adjectives2)
        return f"{random_adjective2} {random_name}"