class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def voice(self):
        print("Hau Hau")


class Wolf(Dog):
    def get_voice(self):
        print("I am the wolf, ")
        super().voice()


class Cat(Animal):
    def get_voice(self):
        print("Miau Miau")


dog = Dog("Ida", "12")
print(dog.name)
print(dog.age)
dog.voice()

cat = Cat("Maska", "8")
cat.get_voice()

wolf = Wolf("Ger", 55)
wolf.get_voice()
print(wolf.name)