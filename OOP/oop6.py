class Czlowiek:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw(self):
        print("Nazywam się " + self.imie)

    @classmethod
    def nowy_czlowiek(cls, imie):
        return cls(imie)

    @staticmethod
    def przywitaj(arg):
        print("Cześć " + arg)


cz1 = Czlowiek.nowy_czlowiek('Adam')
cz1.przedstaw()
cz2 = cz1.nowy_czlowiek('Ala')
cz2.przedstaw()

Czlowiek.przywitaj("Chłopie")
cz2.przywitaj("Ziomal")
