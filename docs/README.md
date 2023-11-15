# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (ah)/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Общее описание решения
Эта программа может быть использована для нахождения площади и/или периметра некоторых фигур, а именно круга, прямоугольника, квадрата и треугольника.

# Описание каждой функции с примерами вызова

### circle.py
```python
import math

def area(r):
    '''Принимает число r (радиус круга), возвращает площадь круга'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r (радиус круга), возвращает периметр круга'''
    return 2 * math.pi * r
```

### Пример вызова функций из файла circle.py
```python
area(5)
return: 78.53981633974483

perimeter(10)
return: 62.83185307179586
```

### square.py
```python
def area(a):
    '''Принимает число a (сторона квадрата), возвращает площадь квадрата'''
    return a * a


def perimeter(a):
    '''Принимает число a (сторона квадрата), возвращает периметр квадрата'''
    return 4 * a
```

### Пример вызова функций из файла square.py
```python
area(4)
return: 16

perimeter(9)
return: 36
```

### rectangle.py
```python
def area(a, b):
    '''Принимает два числа a и b (стороны прямоугольника), возвращает площадь прямоугольника'''
    return a * b


def perimeter(a, b):
    '''Принимает два числа a и b (стороны прямоугольника), возвращает периметр прямоугольника'''
    return 2 * (a + b)
```

### Пример вызова функций из файла rectangle.py
```python
area(2, 3)
return: 6

perimeter(7, 8)
return: 30
```

### triangle.py
```python
def area(a, h):
    '''Принимает два числа a и h (сторона треугольника и высота, проведённая к ней, соответственно), возвращает площадь треугольника'''
    return a * h / 2 


def perimeter(a, b, c):
    '''Принимает три числа a, b и c (стороны треугольника), возвращает периметр треугольника'''
    return a + b + c
```

### Пример вызова функций из файла triangle.py
```python
area(11, 12)
return: 66.0

perimeter(13, 14, 15)
return: 42
```

# История изменения проекта с хешами коммитов
- `8ba9aeb` - circle.py and square.py added
- `d078c8d` - docs added
- `0b55037` - new files added
- `8c1b852` - file edited 

# Unittest
К данной программе прилагается набор unit-тестов для проверки корректности работы всех описанных функций. Подробное описание тестирования функций находится в отчете по проекту.
