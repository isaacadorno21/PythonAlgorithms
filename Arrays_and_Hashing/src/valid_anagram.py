"""Problem Description: - Given two strings s and t, return true if t is an anagram of s, and false otherwise. An
Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""

from collections import Counter


class Solution:
    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


'''
Notes on the solution:
- I used Counters here to compare the values and occurrences of each string

Other solutions: 
- Sort each string and see if they're equivalent
- Create a dictionary manually and fill it in to compare values
'''
