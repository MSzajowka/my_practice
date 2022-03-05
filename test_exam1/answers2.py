def name_sorter(name_list):
    female = []
    male = []
    for item in name_list:
        if item[-1] == 'a':
            female.append(item)
        else:
            male.append(item)

    name_dict = {'female': female,'male': male}
    return name_dict


names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]

print(name_sorter(names))
