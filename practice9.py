def find_boundaries(k):
    tup = ()
    for i in range(len(k)):
        if type(k[i]) == int or type(k[i]) == float:
            tup = tup + (k[i],)

    return min(tup), max(tup)


k = ('h', 'j', 1, 2.0, 3, 4, -5, 'f', 9)

print(find_boundaries(k))
