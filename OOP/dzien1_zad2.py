import math


class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f'Figrura koloru {self.color} o środku w punkcie ({self.x}, {self.y}).'

    def describe(self):
        print(f"x = {self.x}, y = {self.y}, color = {self.color}")

    def distance(self, cl):
        x_dist = self.x - cl.x
        y_dist = self.y - cl.y
        print(math.sqrt(x_dist ** 2 + y_dist ** 2))


triangle = Shape(3, 4, 'white')
square = Shape(7, 12, 'black')
circle = Shape(-10, 5, 'pink')
print(triangle)
print(square)
print(circle)
circle.distance(square)

