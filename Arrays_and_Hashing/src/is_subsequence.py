"""Problem Description: - Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:
    @staticmethod
    def is_subsequence_one(s: str, t: str) -> bool:
        # Ordering matters - skip on HashMap and Counter
        # Sorting will also not work for us
        # Basic solution: iterate through with a new goal once we've matched letter
        # Goals will be letters in string s
        if len(s) == 0:
            return True
        goal = (0, s[0])
        for letter in t:
            if letter == goal[1]:
                if goal[0] == len(s) - 1:
                    return True
                goal = (goal[0]+1, s[goal[0]+1])
        return False

    @staticmethod
    def is_subsequence_two(s: str, t: str) -> bool:
        # Two Pointers approach
        if len(s) == 0:
            return True
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


'''
Notes on the solution:
- I created a tuple to store goal information (index and current letter we're searching for)
- Iterating through and updating the goal information, making sure to return True early so we 
don't get out of bounds errors

Other solutions: 
- Use two pointers - one to keep track of position in s, one to keep track of position in t
'''
