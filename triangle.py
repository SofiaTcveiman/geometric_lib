def area(a, h): 
    if ((type(a) == int or type(a) == float) and
        (type(h) == int or type(h) == float)):
        if a >= 0 and h >= 0:
            return a * h / 2
        raise ValueError
    raise TypeError


def perimeter(a, b, c):
    if ((type(a) == int or type(a) == float) and
        (type(b) == int or type(b) == float) and
        (type(c) == int or type(c) == float)):
        if a >= 0 and b >= 0 and c >= 0:
            return a + b + c
        raise ValueError
    raise TypeError
