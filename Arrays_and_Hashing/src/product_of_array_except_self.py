"""
Problem Description: -

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Product Sum
        # All elements = elements to the left and to the right

        n = len(nums)
        left_array = [1] * n
        right_array = [1] * n
        final_array = [1] * n

        # All to the left (prefix)
        for i in range(1, n):
            left_array[i] = nums[i-1] * left_array[i-1]

        # All to the right (postfix)
        for i in range(n - 2, -1, -1):
            right_array[i] = nums[i+1] * right_array[i+1]

        # Put them together
        for i in range(n):
            final_array[i] = left_array[i] * right_array[i]

        return final_array