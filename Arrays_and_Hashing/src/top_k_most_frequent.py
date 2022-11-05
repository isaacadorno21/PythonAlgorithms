"""Problem Description: - Given an integer array nums and an integer k, return the k most frequent elements. You may
return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
from collections import Counter
import heapq


class Solution:
    @staticmethod
    def top_k_most_frequent_simple(nums: list[int], k: int) -> list[int]:
        # Easy Python solution
        output = Counter(nums).most_common(k)
        return [key for key, _ in output]

    @staticmethod
    def top_k_most_frequent_dictionary(nums: list[int], k: int) -> list[int]:
        # We could create our dictionary, sort by values, and take the k top value (O(nlogn))
        nums_dict = {}
        for n in nums:
            nums_dict[n] = 1 + nums_dict.get(n, 0)
        sorted_nums_dict = [(key, value) for key, value in sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)]
        return [key for key, _ in sorted_nums_dict[:k]]

    @staticmethod
    def top_k_most_frequent_heap(nums: list[int], k: int) -> list[int]:
        # We could create a heap, heapify, and then pop off k times (O(klogn))
        heap_list = Counter(nums)
        return heapq.nlargest(k, heap_list.keys(), key=heap_list.get)

    @staticmethod
    def top_k_most_frequent_bucket_sort(nums: list[int], k: int) -> list[int]:
        # Linear Time with Bucket Sort
        return []


'''
Notes on the solution:
- Multiple solutions. "Easy" python solution is use Counter's 'most_common' method to return the top k most 
frequent elements.

Other solutions:
- Use a dictionary, store the elements and then store by value
- Use a heap, return the top k most frequent elements
- Use bucket sort 
'''