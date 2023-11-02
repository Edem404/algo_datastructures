import unittest
from first_lab.src.is_arr_monotonous import is_arr_monotonous

monotonous_arr_raise = [item for item in range(1, 9)]
monotonous_arr_raise_twice_of_number = [1, 1, 2, 2, 3, 4, 5]
monotonous_arr_down = [item for item in range(10, 0, -1)]
not_monotonous_arr = [1, 5, 2, 4]
negative_arr = [2, 2, -1]
second_case_arr = [2, 2, 3]
third_case = [1]
fourth_case = []


class RaiseMonotonousTest(unittest.TestCase):
    def test_raise(self):
        self.assertEqual(True, is_arr_monotonous(monotonous_arr_raise))


class DownMonotonousTest(unittest.TestCase):
    def test_down(self):
        self.assertEqual(True, is_arr_monotonous(monotonous_arr_down))


class NotMonotonousTest(unittest.TestCase):
    def test_not_monotonous(self):
        self.assertEqual(False, is_arr_monotonous(not_monotonous_arr))


class RaiseMonotonousTwiceTest(unittest.TestCase):
    def test_raise(self):
        self.assertEqual(True, is_arr_monotonous(monotonous_arr_raise_twice_of_number))


class NegativeArrTest(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(True, is_arr_monotonous(negative_arr))


class SecondCaseTest(unittest.TestCase):
    def test_second(self):
        self.assertEqual(True, is_arr_monotonous(second_case_arr))


class ThirdCaseTest(unittest.TestCase):
    def test_third(self):
        self.assertEqual(True, is_arr_monotonous(third_case))


class FourthCaseTest(unittest.TestCase):
    def test_fourth(self):
        self.assertEqual(False, is_arr_monotonous(fourth_case))


if __name__ == '__main__':
    unittest.main()
