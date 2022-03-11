class Employee:
    id = '12345'
    first_name = 'Zenek'
    last_name = 'Dupek'
    _salary = 10

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def set_salary(self, salary):
        self._salary = salary

obj = Employee('123', 'Zbigniew', 'Boniek')
print(obj)