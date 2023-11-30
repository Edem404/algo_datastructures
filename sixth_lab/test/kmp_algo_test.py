import unittest
from sixth_lab.src.kmp_algorythm.kmp_algorythm import kmp


class MyTestCase(unittest.TestCase):
    def test_one_find(self):
        self.assertEqual([9], kmp("abcabc", "acbacdacdabcabcd"))  # add assertion here

    def test_two_find(self):
        self.assertEqual([3, 9], kmp("abab", "abcababcdabab"))

    def test_all_char_similar(self):
        self.assertEqual([0, 1, 2, 3], kmp("XXX", "XXXXXX"))

    def test_haystack_needle_similar(self):
        self.assertEqual([0], kmp("XXX", "XXX"))

    def test_one_char(self):
        self.assertEqual([0], kmp("X", "X"))

    def test_no_entry(self):
        self.assertEqual([], kmp("X", "CCC"))


if __name__ == '__main__':
    unittest.main()
