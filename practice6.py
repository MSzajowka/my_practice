import random


def d6(num):
    throw = 0
    for _ in range(0, num):
        throw += random.randint(1, 6)
    return throw


print(d6(6))
