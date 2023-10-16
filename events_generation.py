import random

class SportGen:
    def __init__(self):
        self.adjectives = ["Пьяный", "Польский", "Юношеский", "Подводный", "Арабский"]
        self.sports = ["футбол", "хоккей", "хоббихорсинг", "баскетбол ногой", "CS"]

    def generate_random_sport(self):
        random_adjective = random.choice(self.adjectives)
        random_sport = random.choice(self.sports)
        return f"{random_adjective} {random_sport}"
