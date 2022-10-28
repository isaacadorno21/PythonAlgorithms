import unittest
from src.contains_duplicate import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1,2,3,1]
        expected = True
        actual = Solution().containsDuplicate(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1,2,3,4]
        expected = False
        actual = Solution().containsDuplicate(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        expected = True
        actual = Solution().containsDuplicate(nums)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()