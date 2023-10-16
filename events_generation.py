import random

class SportGen:
    def __init__(self, adjectives, sports):
        self.adjectives = adjectives
        self.sports = sports

    def generate_random_sport(self):
        random_adjective = random.choice(self.adjectives)
        random_sport = random.choice(self.sports)
        return f"{random_adjective} {random_sport}"

adjectives_list = ["Пьяный", "Польский", "Юношеский", "Подводный", "Арабский"]
sports_list = ["футбол","хоккей", "хоббихорсинг", "баскетбол ногой", "CS"]
sports_generator = SportGen(adjectives_list, sports_list)
random_sport = sports_generator.generate_random_sport()
print("Спорт: " + random_sport)
