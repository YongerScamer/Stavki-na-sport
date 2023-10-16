import random

class SportGen:
    def __init__(self, sports):
        self.sports = sports

    def generate_random_sport(self):
        return random.choice(self.sports)

sports_list = ["Футбол","Хоккей", "Хоббихорсинг", "Дота 2", "CS2"]
sports_generator = SportGen(sports_list)
random_sport = sports_generator.generate_random_sport()
print("Спорт: " + random_sport)
