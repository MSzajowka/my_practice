class Book:

    def __init__(self, n, p, a):
        print("Tworzę nową książkę")
        self.name = n
        self.price = p
        self.author = a

    def __repr__(self):
        return "Book({}, {}, {})".format(repr(self.name), repr(self.author), repr(self.price))

# obj = Book('nazwa', 100, 'zbychu')
# print(obj)


class EBook(Book):
    def __init__(self, n, p, a, s):
        print('Tworzę nowego ebooka')
        super().__init__(n, p, a)
        self.size_in_mb = s

    def print_book_info(self, n, p, a, s):
        super().__init__(n, p, a)
        self.size_in_mb = s
        print(self.size_in_mb)

obj2 = EBook('nazwa2', 200, 'zenek', 256)
obj2.print_book_info()


