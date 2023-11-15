import unittest
from triangle import area
from triangle import perimeter


class TriangleTestCaseArea(unittest.TestCase):
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        res = area(0, 10)
        self.assertEqual(res, 0)
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_normal_data(self):
        res = area(2, 3)
        self.assertEqual(res, 3)
        res = area(12, 4)
        self.assertEqual(res, 24)
        res = area(2, 11)
        self.assertEqual(res, 11)
        res = area(34, 10)
        self.assertEqual(res, 170)
        res = area(27, 6)
        self.assertEqual(res, 81)

    def test_area_big_data(self):
        res = area(10000, 10000)
        self.assertEqual(res, 50000000)
        res = area(1000000, 1000000)
        self.assertEqual(res, 500000000000)
        res = area(100000000, 100000000)
        self.assertEqual(res, 5000000000000000)

    def test_area_wrong_value_of_data(self):
        self.assertRaises(ValueError, area, -10, 9)
        self.assertRaises(ValueError, area, 1, -20)
        self.assertRaises(ValueError, area, -21, -2)

    def test_area_wrong_type_of_data(self):
        self.assertRaises(TypeError, area, "a", "b")
        self.assertRaises(TypeError, area, "a", True)
        self.assertRaises(TypeError, area, "a", [27])
        self.assertRaises(TypeError, area, [33], [27])
        self.assertRaises(TypeError, area, "a", {62})
        self.assertRaises(TypeError, area, "a", 2055)
        self.assertRaises(TypeError, area, False, [84])
        self.assertRaises(TypeError, area, [27], {187})
        self.assertRaises(TypeError, area, False, True)


class TriangleTestCasePerimeter(unittest.TestCase):
    def test_perimeter_normal_data(self):
        res = perimeter(2, 3, 4)
        self.assertEqual(res, 9)
        res = perimeter(12, 8, 7)
        self.assertEqual(res, 27)
        res = perimeter(1, 11, 111)
        self.assertEqual(res, 123)
        
    def test_perimeter_big_data(self):
        res = perimeter(100, 1000, 500)
        self.assertEqual(res, 1600)
        res = perimeter(1000, 10000, 8000000)
        self.assertEqual(res, 8011000)
        res = perimeter(30000, 100000, 22000000)
        self.assertEqual(res, 22130000)

    def test_area_wrong_value_of_data(self):
        self.assertRaises(ValueError, perimeter, -10, 3, 9)
        self.assertRaises(ValueError, perimeter, 1, -8, -20)
        self.assertRaises(ValueError, perimeter, -21, -19, -2)

    def test_perimeter_wrong_type_of_data(self):
        self.assertRaises(TypeError, perimeter, "a", True, [123])
        self.assertRaises(TypeError, perimeter, "a", 234, (1870))
        self.assertRaises(TypeError, perimeter, "a", "b", "c")
        self.assertRaises(TypeError, perimeter, "a", True, False)
        self.assertRaises(TypeError, perimeter, "a", [27], {133})
        self.assertRaises(TypeError, perimeter, [33], [27], "d")
        self.assertRaises(TypeError, perimeter, "a", {62}, True)
        self.assertRaises(TypeError, perimeter, "a", 2055, 76)
        self.assertRaises(TypeError, perimeter, False, True, True)


if __name__ == '__main__':
    unittest.main()
