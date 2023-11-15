import math


def area(r):
    if type(r) == int or type(r) == float:
        if r >= 0:
            return math.pi * r * r
        raise ValueError
    raise TypeError


def perimeter(r):
    if type(r) == int or type(r) == float:
        if r >= 0:
            return 2 * math.pi * r
        raise ValueError
    raise TypeError
