import unittest
from classes import Math


class TestClasses(unittest.TestCase):
    def setUp(self):
        self.first = 20
        self.second = 4
        self.math = Math(self.first, self.second)

    def test_addition(self):
        self.assertEqual(self.math.addition(), 24)

    def test_subtraction(self):
        self.assertEqual(self.math.subtraction(), 16)

    def test_multiplication(self):
        self.assertEqual(self.math.multiplication(), 80)

    def test_division(self):
        self.assertEqual(self.math.division(), 5)


if __name__ == '__main__':
    unittest.main()
