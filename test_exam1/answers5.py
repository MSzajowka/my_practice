from random import randint


def roll(dices_number, dice_type=6, result_modifier=0):
    allowed_dices = [3, 4, 6, 8, 10, 12, 100]
    result = []
    if dice_type not in allowed_dices:
        raise Exception("No such dice!")

    for number in range(dices_number):
        result.append(randint(1, dice_type))

    return sum(result) + result_modifier


if __name__ == '__main__':
    print(roll(2, 10, 20))


# 2nd method

def roll(dices_number, dice_type=6, result_modifier=0):
    if dice_type not in (3, 4, 6, 8, 10, 12, 100):
        raise Exception("No such dice!")

    return sum(randint(1, dice_type) for _ in range(dices_number)) + result_modifier


if __name__ == '__main__':
    print(roll(2))
    print(roll(4, 10, 7))

