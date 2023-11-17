import unittest
from fifth_lab.src.minimal_beer_sort.minimal_beer_sort_count import minimal_beer_sort_count
PARAM_FILE = "param_file"
PARAM_FILE2 = "param_file2"
PARAM_FILE3 = "param_file3"
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2, minimal_beer_sort_count(PARAM_FILE))

    def test_two(self):
        self.assertEqual(2, minimal_beer_sort_count(PARAM_FILE2))

    def test_three(self):
        self.assertEqual(2, minimal_beer_sort_count(PARAM_FILE3))
if __name__ == '__main__':
    unittest.main()
