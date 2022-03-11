class RaceCar:
    def __init__(self, brand, model, hp):
        self.brand = brand
        self.model = model
        self.hp = hp

    def __repr__(self):
        return f'RaceCar({self.brand!r}, {self.model!r}, {self.hp})'

    def __lt__(self, other):
        return self.hp > other.hp


car1 = RaceCar('BMW', 'E36', 102)
car2 = RaceCar('Audi', 'A3', 99)
car3 = RaceCar('Mercedes', 'A', 80)
print(car2 < car3)
print(sorted([car1, car2, car3]))
