from math import pi, sqrt
from abc import ABC, abstractmethod


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Figure(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Figure):
    def __init__(self, point_center, radius_length):
        self.point_center = point_center
        self.radius_length = radius_length

    def perimeter(self):
        return round(2 * pi * self.radius_length, 2)

    def area(self):
        return round(pi * self.radius_length ** 2, 2)


class Triangle(Figure):
    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def perimeter(self):
        ab = sqrt((self.point_b.x - self.point_a.x) ** 2 + (self.point_b.y - self.point_a.y) ** 2)
        bc = sqrt((self.point_c.x - self.point_b.x) ** 2 + (self.point_c.y - self.point_b.y) ** 2)
        ac = sqrt((self.point_c.x - self.point_a.x) ** 2 + (self.point_c.y - self.point_a.y) ** 2)
        return round(ab + bc + ac, 2)

    def area(self):
        return round(abs(self.point_a.x * (self.point_b.y - self.point_c.y) + self.point_b.x * (
                self.point_c.y - self.point_a.y) + self.point_c.x * (self.point_a.y - self.point_b.y)) / 2, 2)


class Square(Figure):
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def perimeter(self):
        return round(sqrt((self.point_b.x - self.point_a.x) ** 2 + (self.point_b.y - self.point_a.y) ** 2) * 4, 2)

    def area(self):
        return round(sqrt((self.point_b.x - self.point_a.x) ** 2 + (self.point_b.y - self.point_a.y) ** 2) ** 2, 2)
