import unittest
from rectangle import area
from rectangle import perimeter


class RectangleTestCaseArea(unittest.TestCase):
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        res = area(0, 10)
        self.assertEqual(res, 0)
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
        res = area(1, 1)
        self.assertEqual(res, 1)
        res = area(5, 5)
        self.assertEqual(res, 25)

    def test_area_normal_data(self):
        res = area(2, 3)
        self.assertEqual(res, 6)
        res = area(12, 4)
        self.assertEqual(res, 48)
        res = area(1, 11)
        self.assertEqual(res, 11)
        res = area(33, 1)
        self.assertEqual(res, 33)
        res = area(27, 6)
        self.assertEqual(res, 162)

    def test_area_big_data(self):
        res = area(1000, 1000)
        self.assertEqual(res, 1000000)
        res = area(100000, 100000)
        self.assertEqual(res, 10000000000)
        res = area(10000000, 10000000)
        self.assertEqual(res, 100000000000000)

    def test_area_wrong_value_of_data(self):
        self.assertRaises(ValueError, area, -10, 9)
        self.assertRaises(ValueError, area, 1, -20)
        self.assertRaises(ValueError, area, -21, -19)
        self.assertRaises(ValueError, area, -100, 99)
        
    def test_area_wrong_type_of_data(self):
        self.assertRaises(TypeError, area, "a", [2701])
        self.assertRaises(TypeError, area, [27], False)
        self.assertRaises(TypeError, area, True, "abc")
        self.assertRaises(TypeError, area, "ab", "cde")


class RectangleTestCasePerimeter(unittest.TestCase):
    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
        res = perimeter(1, 1)
        self.assertEqual(res, 4)
        res = perimeter(5, 5)
        self.assertEqual(res, 20)
        
    def test_perimeter_normal_data(self):
        res = perimeter(2, 3)
        self.assertEqual(res, 10)
        res = perimeter(12, 4)
        self.assertEqual(res, 32)
        res = perimeter(1, 11)
        self.assertEqual(res, 24)
        
    def test_perimeter_big_data(self):
        res = perimeter(100, 1000)
        self.assertEqual(res, 2200)
        res = perimeter(1000, 10000)
        self.assertEqual(res, 22000)
        res = perimeter(10000, 100000)
        self.assertEqual(res, 220000)

    def test_area_wrong_value_of_data(self):
        self.assertRaises(ValueError, perimeter, -10, 9)
        self.assertRaises(ValueError, perimeter, 1, -20)
        self.assertRaises(ValueError, perimeter, -21, -19)
        self.assertRaises(ValueError, perimeter, -100, 11)
        
    def test_area_wrong_type_of_data(self):
        self.assertRaises(TypeError, perimeter, "a", [2701])
        self.assertRaises(TypeError, perimeter, [27], False)
        self.assertRaises(TypeError, perimeter, True, "abc")
        self.assertRaises(TypeError, perimeter, "ab", "cde")


if __name__ == '__main__':
    unittest.main()
