from typing import override


class Shape:
    def calc_area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # @override
    def calc_area(self):
        return self.height * self.width


class Square(Rectangle):
    @override
    def get_area(self):
        return self.height**2


rectangle = Rectangle(5, 4)
square = Square(5, 5)
print(rectangle.calc_area())
print(square.calc_area())
