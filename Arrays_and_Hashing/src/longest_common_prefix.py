"""Problem Description: - Write a function to find the longest common prefix string amongst an array of strings. If
there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix amongst the input strings.
"""


class Solution:
    @staticmethod
    def longest_common_prefix(strs: list[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix


'''Notes on the solution: 
- We have to go one character at a time, checking if that individual character at that 
index is the same for all the strings we have. Checks should be made to make sure we're not getting an index out of 
bounds error in case we run into a shorter word than the one we are using to compare. 

Other solutions: 
-
'''
