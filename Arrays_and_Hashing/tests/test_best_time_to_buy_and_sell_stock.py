import unittest
from Arrays_and_Hashing.src.best_time_to_buy_and_sell_stock import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        actual = Solution().max_profit(prices)
        self.assertEqual(expected, actual)

    def test_2(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        actual = Solution().max_profit(prices)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
