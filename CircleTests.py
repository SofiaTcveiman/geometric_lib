import unittest
from math import pi
from circle import area
from circle import perimeter


class CircleTestCaseArea(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_normal_data(self):
        res = area(5)
        self.assertEqual(res, pi * 25)
        res = area(10)
        self.assertEqual(res, pi * 100)
        res = area(15)
        self.assertEqual(res, pi * 225)
        res = area(20)
        self.assertEqual(res, pi * 400)

    def test_area_big_data(self):
        res = area(100)
        self.assertEqual(res, pi * 10000)
        res = area(1000)
        self.assertEqual(res, pi * 1000000)
        res = area(1000000)
        self.assertEqual(res, pi * 1000000000000)

    def test_area_wrong_value_of_data(self):
        self.assertRaises(ValueError, area, -1)
        self.assertRaises(ValueError, area, -100)
        
    def test_area_wrong_type_of_data(self):
        self.assertRaises(TypeError, area, "a")
        self.assertRaises(TypeError, area, [27])
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, {84})


class CircleTestCasePerimeter(unittest.TestCase):
    def test_perimeter_normal_data(self):
        res = perimeter(2)
        self.assertEqual(res, pi * 2 * 2)
        res = perimeter(12)
        self.assertEqual(res, pi * 12 * 2)
        res = perimeter(1)
        self.assertEqual(res, pi * 1 * 2)
        
    def test_perimeter_big_data(self):
        res = perimeter(100)
        self.assertEqual(res, pi * 100 * 2)
        res = perimeter(1000)
        self.assertEqual(res, pi * 1000 * 2)
        res = perimeter(10000)
        self.assertEqual(res, pi * 10000 * 2)

    def test_area_wrong_value_of_data(self):
        self.assertRaises(ValueError, perimeter, -1)
        self.assertRaises(ValueError, perimeter, -100)
        
    def test_area_wrong_type_of_data(self):
        self.assertRaises(TypeError, perimeter, "a")
        self.assertRaises(TypeError, perimeter, [84])
        self.assertRaises(TypeError, perimeter, True)
        self.assertRaises(TypeError, perimeter, {72})

if __name__ == '__main__':
    unittest.main()
