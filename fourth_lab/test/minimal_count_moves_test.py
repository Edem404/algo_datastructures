import unittest
from fourth_lab.src.min_moves_count import min_moves_count

PARAM_FILE = "files_need_for_test/file_for_test.txt"
RESULT_FILE = "files_need_for_test/result_of_test.txt"


class TestMovesAreFounded(unittest.TestCase):
    def test_founded(self):
        param_lines = ["8\n", "0, 7\n", "7, 0\n"]
        with open(PARAM_FILE, "w", encoding="utf-8") as param_file:
            param_file.writelines(param_lines)

        min_moves_count(PARAM_FILE, RESULT_FILE)
        with open(RESULT_FILE, "r", encoding="utf-8") as result_file:
            read_line = result_file.readlines()

        self.assertEqual(6, int(read_line[0].strip()))


if __name__ == '__main__':
    unittest.main()
