import unittest
from buy_and_sell import get_num_days_fast as get_num_days


class TestBuySell(unittest.TestCase):
    def test_one_price(self):
        self.assertEqual(get_num_days([1]), (0, 0))

    def test_two_price_solution(self):
        self.assertEqual(get_num_days([1, 5]), (1, 2))

    def test_two_price_no_solution(self):
        self.assertEqual(get_num_days([5, 1]), (0, 0))

    def test_all_equal(self):
        self.assertEqual(get_num_days([5, 5, 5, 5]), (0, 0))

    def test_diff_prices(self):
        self.assertEqual(get_num_days([10, 3, 5, 3, 11, 9]), (2, 5))

    def test_diff_prices2(self):
        self.assertEqual(get_num_days([11, 7, 1, 6, 2]), (3, 4))

    def test_first_last_item(self):
        self.assertEqual(get_num_days([1, 3, 2, 8, 2, 11, 15]), (1, 7))

    def test_first_last_equal_item(self):
        self.assertEqual(get_num_days([1, 3, 2, 5, 7, 15, 11, 15, 14, 15]), (1, 6))

    def test_last_two_items(self):
        self.assertEqual(get_num_days([15, 8, 5, 1, 15]), (4, 5))

    def test_first_two_items(self):
        self.assertEqual(get_num_days([1, 100, 5, 6, 11, 99, 98, 97, 96]), (1, 2))

    def test_buy_price_over_1000(self):
        self.assertEqual(get_num_days([1001, 5000, 3000]), (0, 0))


if __name__ == '__main__':
    unittest.main()
