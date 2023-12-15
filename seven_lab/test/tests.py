import unittest
from seven_lab.src.max_line_length.max_line_length import max_wire_length


class MyTestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(5.65, max_wire_length('first_test.txt'))  # add assertion here

    def test_second(self):
        self.assertEqual(300.0, max_wire_length('second_test.txt'))

    def test_third(self):
        self.assertEqual(396.32, max_wire_length('third_test.txt'))

    def test_fourth(self):
        self.assertEqual(2738.17, max_wire_length('fourth_test.txt'))

if __name__ == '__main__':
    unittest.main()
