class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f'added {num1} to {num2} got {result}')
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f'multiplied {num1} with {num2} got {result}')
        return result

    def print_operators(self):
        print(self.history)


# TODO - works
# obj = Calculator()
# print(obj.multiply(5, 2))
# print(obj.multiply(7, 3))
# print(obj.add(5, 2))
# print(obj.add(5, 3))
# obj.print_operators()



