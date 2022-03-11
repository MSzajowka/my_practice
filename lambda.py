def funkcja(f, liczba):
    return f(liczba)


print(funkcja(lambda x: x * x, 3))


def kwadrat(x):
    return x * x


print(kwadrat(5))

wynik = lambda x, y, z: (x * y) + z

print(wynik(2, 9, 10))

wynik2 = (lambda x: x + x)(7)

print(wynik2)
