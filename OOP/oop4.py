class Test:
    def __del__(self):
        print("Bye")


obj = Test()
obj2 = obj
lista = [obj2]
print(id(obj), id(obj2), id(lista))
del obj
del obj2
del lista

print("Koniec")


