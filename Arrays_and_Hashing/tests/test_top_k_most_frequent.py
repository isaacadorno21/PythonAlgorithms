import unittest
from Arrays_and_Hashing.src.top_k_most_frequent import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected_1 = [1, 2]
        expected_2 = [2, 1]
        actual = Solution().top_k_most_frequent(nums, k)
        self.assertTrue(expected_1 == actual or expected_2 == actual)

    def test_2(self):
        nums = [1]
        k = 1
        expected = [1]
        actual = Solution().top_k_most_frequent(nums, k)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
