class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self, powitanie="Cześć"):
        return powitanie + ", tu " + self.imie + ', lat ' + str(self.wiek) + '.'



obiekt = Czlowiek('Michał', 38)
print(obiekt.imie)
print(obiekt.przedstaw_sie("Witam"))
obiekt2 = Czlowiek('Adam', 3)
obiekt2.imie = "Adam"
print(obiekt2.przedstaw_sie())
