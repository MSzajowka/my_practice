def shorten(string):
    string = string.split()
    shortened = ''
    for i in range(len(string)):
        shortened += string[i][0].upper()
    return shortened

print(shorten("Don't reapeat yourself"))
