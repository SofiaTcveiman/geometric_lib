def area(a, b):
    if ((type(a) == int or type(a) == float) and
        (type(b) == int or type(b) == float)):
        if a >= 0 and b >= 0:
            return a * b
        raise ValueError
    raise TypeError


def perimeter(a, b):
    if ((type(a) == int or type(a) == float) and
        (type(b) == int or type(b) == float)):
        if a >= 0 and b >= 0:
            return 2 * (a + b)
        raise ValueError
    raise TypeError
