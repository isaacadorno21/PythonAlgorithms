"""
Problem Description: - Given an integer array nums and an integer k, return the k most frequent elements. You may
return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
"""


from collections import Counter


class Solution:
    def top_k_most_frequent(self, nums: list[int], k: int) -> list[int]:
        # Dictionary of counts, sort values in descending order
        nums_map = Counter(nums)
        dictionary_items = list(nums_map.items())
        sorted_dictionary_items = sorted(dictionary_items, key=lambda x: x[1], reverse=True)
        
        i = 0
        output_values = []
        while i < k:
            output_values.append(sorted_dictionary_items[i][0])
            i += 1
        return output_values
