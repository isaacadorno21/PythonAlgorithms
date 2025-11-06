import unittest
from Arrays_and_Hashing.src.two_sum import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_1 = [1, 0]
        expected_2 = [0, 1]
        actual = Solution().two_sum(nums, target)
        self.assertTrue(expected_1 == actual or expected_2 == actual)

    def test_2(self):
        nums = [3, 2, 4]
        target = 6
        expected_1 = [2, 1]
        expected_2 = [1, 2]
        actual = Solution().two_sum(nums, target)
        self.assertTrue(expected_1 == actual or expected_2 == actual)

    def test_3(self):
        nums = [3, 3]
        target = 6
        expected_1 = [1, 0]
        expected_2 = [0, 1]
        actual = Solution().two_sum(nums, target)
        self.assertTrue(expected_1 == actual or expected_2 == actual)


if __name__ == '__main__':
    unittest.main()
