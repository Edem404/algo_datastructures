import unittest
from second_lab.src.can_square_contain import can_square_contain

class FirstCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(9, can_square_contain(10, 2, 3))  # add assertion here


class SecondCase(unittest.TestCase):
    def test_second(self):
        self.assertEqual(1999999998, can_square_contain(2, 1000000000, 999999999))


class ThirdCase(unittest.TestCase):
    def test_third(self):
        self.assertEqual(2, can_square_contain(4, 1, 1))


if __name__ == '__main__':
    unittest.main()
