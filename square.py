def area(a):
    if type(a) == int or type(a) == float:
        if a >= 0:
            return a * a
        raise ValueError
    raise TypeError


def perimeter(a):
    if type(a) == int or type(a) == float:
        if a > 0:
            return 4 * a
        raise ValueError
    raise TypeError
