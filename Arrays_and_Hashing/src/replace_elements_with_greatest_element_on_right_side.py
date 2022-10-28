"""Problem Description: - Given an array arr, replace every element in that array with the greatest element among the
elements to its right, and replace the last element with -1. After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
"""


class Solution:
    @staticmethod
    def replace_elements(arr: list[int]) -> list[int]:
        # Brute force
        # for i in range(len(arr)-1):
        #    arr[i] = max(arr[i+1:])
        # arr[-1] = -1
        # return arr

        right_max = float('-inf')
        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = max(right_max, arr[i+1])
            right_max = max(right_max, temp)
        arr[-1] = -1
        return arr


'''
Notes on the solution: 
- My initial, brute force solution has us going through and checking the max for each 
subarray after the current element. This results in O(n**2) runtime.
- I optimized this by going through the array backwards, to be able to calculate the max in realtime.
This leads us to an O(n) solution.
'''
