def find_short_words(l):
    words = []
    for word in l:
        if len(word) < 5:
            words.append(word)
    return words


l = ['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie']
print(find_short_words(l))
