def validate_pesel(pesel):
    weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    pesel = [int(a) for a in str(pesel)]
    control = []
    for i in range(10):
        control.append(weight[i] * pesel[i])
    control = sum(control)
    if 10 - (control % 10) == pesel[-1]:
        return True
    return False


print(validate_pesel((84102900875)))

