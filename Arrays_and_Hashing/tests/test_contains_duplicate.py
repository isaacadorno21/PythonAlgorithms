import unittest
from Arrays_and_Hashing.src.contains_duplicate import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3, 3]
        expected = True
        actual = Solution().containsDuplicate(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1, 2, 3, 4]
        expected = False
        actual = Solution().containsDuplicate(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [-1, -1, 0]
        expected = True
        actual = Solution().containsDuplicate(nums)
        self.assertEqual(expected, actual)

    def test_4(self):
        nums = []
        expected = False
        actual = Solution().containsDuplicate(nums)
        self.assertEqual(expected, actual)

    def test_5(self):
        nums = [42]
        expected = False
        actual = Solution().containsDuplicate(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
