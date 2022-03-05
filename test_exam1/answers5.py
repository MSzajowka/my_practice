from random import randint


def roll(dices_number, dice_type=6, result_modifier=0):
    allowed_dices = [3, 4, 6, 8, 10, 12, 100]
    try:
        if dice_type in allowed_dices:
            result = []

        for number in range(dices_number):
            result.append(randint(1, dice_type))

        return sum(result) + result_modifier

    except:
        return 'No such dice!'


print(roll(2, 100, 20))
