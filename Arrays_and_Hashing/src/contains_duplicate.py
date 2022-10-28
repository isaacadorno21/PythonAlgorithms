"""Problem Description: - Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from collections import Counter


class Solution:
    @staticmethod
    def contains_duplicate(nums: list[int]) -> bool:
        nums_counter = Counter(nums)
        if any(value > 1 for value in nums_counter.values()):
            return True
        return False


'''
Notes on the solution:
- I used a Counter here to keep track of the values of the array, and the number of times they occurred

Other solutions: 
- We could convert this to a set and check if it's the same length 
    - If it is the same length, we know there's no duplicates 
    - If it isn't, we know there's a problem. The set could be smaller because elements 
      might have been rejected if they already existed in the set
- We could use a regular Python dictionary and store the counts ourselves
- We could also sort and see if any values if any consecutive elements are equal
'''
