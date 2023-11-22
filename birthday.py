class BirthDayBoy:
    pass


def drink(value):
    value.pop()


glasses = []


class Katamori(BirthDayBoy):
    def __init__(self, name='Zoli', age=""):
        self.name = name
        self.age = age
        self.lelkesedes = 100

    def level_up(self):
        self.age += 1
        beers = [beer for beer in glasses]
        while beers:
            beers.pop()
        self.drunk = True
        return f"{self.name} be van baszva."
