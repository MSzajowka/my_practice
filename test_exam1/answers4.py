def div(a, b):
    my_range = []
    for number in range(a, b + 1):
        if number % 2 == 0 and number % 3 != 0:
            my_range.append(number)
    return my_range


print(div(1, 20))
