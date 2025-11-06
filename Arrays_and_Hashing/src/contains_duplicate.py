"""
Problem Description: - Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]
Output: true

Example 2:

Input: nums = [1, 2, 3, 4]
Output: false
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique_nums = set()
        for num in nums:
            unique_nums.add(num)
        return len(unique_nums) != len(nums)
