import unittest
from func import addition, subtraction, multiplication, division


class TestFunc(unittest.TestCase):
    def setUp(self):
        self.first = 16
        self.second = 4

    def test_addition(self):
        self.assertEqual(addition(self.first, self.second), 20)

    def test_subtraction(self):
        self.assertEqual(subtraction(self.first, self.second), 12)

    def test_multiplication(self):
        self.assertEqual(multiplication(self.first, self.second), 64)

    def test_division(self):
        self.assertEqual(division(self.first, self.second), 4)


if __name__ == '__main__':
    unittest.main()
