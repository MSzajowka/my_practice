def censor(str, forbidden):
    words = str.split()
    forbidden = forbidden.split(', ')

    for word in words:
        if word in forbidden:
            str = str.replace(word, "*" * len(word))
    return str


str = "Java is the best, but PHP is the bestest!"
forbidden = "Java, C#, Ruby, PHP"

print(censor(str, forbidden))
