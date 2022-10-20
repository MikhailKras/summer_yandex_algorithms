import unittest
from repeating_number import check_repeating as check


class TestCheckRepeating(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(check(2, [1, 2, 3, 1]), 'NO')

    def test_case2(self):
        self.assertEqual(check(1, [1, 0, 1, 1]), 'YES')

    def test_case3(self):
        self.assertEqual(check(2, [1, 2, 3, 1, 2, 3]), 'NO')

    def test_one_item(self):
        self.assertEqual(check(1, [0]), 'NO')

    def test_one_item2(self):
        self.assertEqual(check(0, [-10]), 'NO')

    def test_first_item(self):
        self.assertEqual(check(1, [-5, -5, -4, -9, 10, 11, 15, 104, 115, 15, 10, 15]), 'YES')

    def test_two_items(self):
        self.assertEqual(check(1, [-100, -100]), 'YES')


if __name__ == '__main__':
    unittest.main()
