liczby = [2, 10, 12, 15, 20, 30, 35]


# Mapa

def funkcja(x):
    return x * 2


"""
map() przyjmuje 2 argumenty: funkcję oraz argument do niej. Tutaj map modyfikuje - pomnoży przez 2 (tak jak w funkcja()) każdy element listy liczby
na koniec trzeba zrobić z niej listę
"""

wynik = map(funkcja, liczby)

print(list(wynik))

wynik2 = map(lambda x: x * 3, liczby)
print(list(wynik2))

"""
filter() zwraca True lub False dla wyrażenia (per element listy). Tutaj sprawdzamy czy elementy listy są parzyste 
"""

wynik3 = filter(lambda x: x % 2 == 0, liczby)
print(list(wynik3))

# wszystkie parzyste z liczby podniesie do kwadratu
print(list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, liczby))))
