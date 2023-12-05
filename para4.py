import math
class Square:
    angle = 90
    def __init__(self, side1):
        self.side1 = side1
    def square(self):
        return self.side1 ** 2
    def perimeter(self):
        return self.side1 ** 4
class Rectangle(Square):
    def __init__(self, side1, side2):
        super().__init__(side1)
        self.side2 = side2
    def square(self):
        super().angle
        return self.side1 * self.side2
    def perimeter(self):
        return (self.side1 * self.side2) * 2
    def area(self):
        return self.side1 * self.side2
class Isosceles_triangle:
    def __init__(self, side1):
        self.side1 = side1
    def perimeter(self):
        return self.side1 ** 3
    def area(self):
        return self.side1 * self.side1
class Right_triangle(Isosceles_triangle):
    def __init__(self, side1, leg2, leg3):
        super().__init__(side1)
        self.leg2 = leg2
        self.leg3 = leg3
    def perimeter(self):
        return self.side1 + self.leg2 + self.leg3
    def area(self):
        return self.side1 * self.leg2 * self.leg3
class Display:
    def __init__(self):
        self.resolution = 1080
class Processor:
    def __init__(self):
        self.speed = 4
class Computer(Processor, Display):
    play = 0

