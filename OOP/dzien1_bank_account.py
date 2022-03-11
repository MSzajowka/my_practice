# class BankAccount:
#     number = '12345678910100001111'
#     cash = 0.0
#
#     def __init__(self, number):
#         self.number = number
#         self.cash = 0.0
#
#     def deposit_cash(self, amount):
#         self.amount = amount
#         if amount > 0.0:
#             self.cash += amount
#
#     def withdraw_cash(self, amount):
#         self.amount = amount
#         if amount > 0:
#             if amount <= self.cash:
#                 self.cash -= amount
#             else:
#                 self.cash = 0.0
#             return amount
#         else:
#             raise ValueError('Kwota wypłacenia musi być większa od 0!')
#
#     def print_info(self):
#         return number, self.cash
#
#
# obj_cash = BankAccount(cash=1000).print_info()
# print(obj_cash)
#


class BankAccount:
    def __init__(self, number, cash=0.0):
        self.number = number
        self.cash = cash

    def deposit_cash(self, amount):
        # self.amount = amount
        if amount > 0:
            self.cash += amount
            return f'Wpłacono: {amount}. Stan konta to: {self.cash}.'
        else:
            raise ValueError("you cannot deposit negative amount of cash!")

    def withdraw_cash(self, amount):
        if amount > 0:
            if amount < self.cash:
                self.cash -= amount
                return amount
            else:
                _temp = self.cash
                self.cash = 0.0
                return _temp

    def print_info(self):
        print(f'Numer konta: {self.number} & stan konta: {self.cash}')


obj = BankAccount(12345)


print(obj.cash)

obj.deposit_cash(520)

print(obj.withdraw_cash(200))
print(obj.withdraw_cash(300))
print(obj.withdraw_cash(300))
print(obj.withdraw_cash(100))
print(obj.deposit_cash(1000))
print(obj.deposit_cash(10))
print(obj.withdraw_cash(900))


print('==========')
obj.print_info()