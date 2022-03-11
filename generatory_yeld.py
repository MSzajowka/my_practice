def gen():
    i = 0
    while i < 5:
        yield i
        i += 1

"""
funkcja z yeld jest GENERATORem
yelad to taki return ale dla wielu wartości. Tutaj yeld to objekt przechowujący wiele wartości - od 0 do 4 (tyle ile powtórzeń pętli). Trzeba z tego zrobić listę.
"""

print(list(gen()))

"""
funkcję która jest generatorem można użyć jako elementu iterowalnego, np w pętli for
"""

for i in gen():
    print(i)


def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1

print(tuple(parzyste(100)))


