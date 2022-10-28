"""Problem Description: - Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.You may assume that each input would have exactly one solution, and you may not use
the same element twice.You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


class Solution:
    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for index, num in enumerate(nums):
            if target - num in nums_map:
                return [index, nums_map[target - num]]
            nums_map[num] = index


'''
Notes on the solution:
- We can use a HashMap to determine whether or not our goal exists yet, for each element.
We can define our goal as being the number that when added up to our current element, results in the target.
'''