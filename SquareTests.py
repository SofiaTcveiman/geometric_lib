import unittest
from square import area
from square import perimeter


class SquareTestCaseArea(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_normal_data(self):
        res = area(5)
        self.assertEqual(res, 25)
        res = area(10)
        self.assertEqual(res, 100)
        res = area(15)
        self.assertEqual(res, 225)
        res = area(20)
        self.assertEqual(res, 400)

    def test_area_big_data(self):
        res = area(100)
        self.assertEqual(res, 10000)
        res = area(1000)
        self.assertEqual(res, 1000000)
        res = area(10000)
        self.assertEqual(res, 100000000)

    def test_area_wrong_value_of_data(self):
        self.assertRaises(ValueError, area, -1)
        self.assertRaises(ValueError, area, -100)
        
    def test_area_wrong_type_of_data(self):
        self.assertRaises(TypeError, area, "a")
        self.assertRaises(TypeError, area, [27])
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, [27])


class SquareTestCasePerimeter(unittest.TestCase):
    def test_perimeter_normal_data(self):
        res = perimeter(2)
        self.assertEqual(res, 8)
        res = perimeter(12)
        self.assertEqual(res, 48)
        res = perimeter(1)
        self.assertEqual(res, 4)
        
    def test_perimeter_big_data(self):
        res = perimeter(100)
        self.assertEqual(res, 400)
        res = perimeter(1000)
        self.assertEqual(res, 4000)
        res = perimeter(10000)
        self.assertEqual(res, 40000)

    def test_area_wrong_value_of_data(self):
        self.assertRaises(ValueError, perimeter, -1)
        self.assertRaises(ValueError, perimeter, -100)
        
    def test_area_wrong_type_of_data(self):
        self.assertRaises(TypeError, perimeter, "a")
        self.assertRaises(TypeError, perimeter, [27])
        self.assertRaises(TypeError, perimeter, True)
        self.assertRaises(TypeError, perimeter, [27])


if __name__ == '__main__':
    unittest.main()
    
