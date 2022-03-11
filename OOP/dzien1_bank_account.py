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
