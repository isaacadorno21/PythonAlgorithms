"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]
Output: true

Example 2:

Input: nums = [1, 2, 3, 4]
Output: false
"""

import unittest


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3, 1]
        expected = True
        actual = Solution().containsDuplicate(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1, 2, 3, 4]
        expected = False
        actual = Solution().containsDuplicate(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        expected = True
        actual = Solution().containsDuplicate(nums)
        self.assertEqual(expected, actual)


# Run the tests
if __name__ == "__main__":
    unittest.main()
