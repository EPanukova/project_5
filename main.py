import pygame                                                                   # dedline 27.09.20 23:59:59
from random import random
from math import sqrt


class Vector:
    """Class vector"""

    def __init__(self, x, y):
        """Initialization method"""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Sum of vectors"""
        return self.x + other.x, self.x + other.y

    def __sub__(self, other):
        """Vector difference"""
        return self.x[0] - other.x, self.x[1] - other.y

    def __mul__(self, other):
        """Return multiplication by scalar and scalar product"""
        return self.x * other.x, self.y * other.y

    def len(self):
        """Return vector length"""
        return int(sqrt(self.x[0] * self.x[0] + self.x[1] * self.x[1]))

    def int_pair(self):
        """Return int pair - point"""
        return tuple([self.x, self.y])

#    def __str__(self):
#        """String method"""
#        a = '({},{})'.format(self.x, self.y)
#        return a


#point = Vector(1, 1)
#print(point)


class Line:
    """Class line"""

    def __init__(self):
        """Initialization method """

    def get_joint(self):
        """Adding to a line dot"""

    def set_points(self):
        """Recalculation of point coordinates"""

    def draw_points(self):
        """Drawing a line"""


class Joint(Line):
    """Class Joint"""

    def __init__(self):
        """Initialization method """
        super().__init__()

    # def get_joint(self):

    # удаление кривой, замедление\ускорение кривой


point_1 = Vector(1, 2)
point_2 = Vector(3, 4)
print(point_1 + point_2)
print(Vector.len(point_1))