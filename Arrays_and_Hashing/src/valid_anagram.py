"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"
Output: true

Example 2:

Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Maps will store { key (letter): value (num of occurences) }
        letters_map = {}

        for i in range(0, len(s)):
            s_letter = s[i]
            t_letter = t[i]

            if s_letter not in letters_map:
                letters_map[s_letter] = 1
            else:
                letters_map[s_letter] += 1

            if t_letter not in letters_map:
                letters_map[t_letter] = -1
            else:
                letters_map[t_letter] += -1

        return all(value == 0 for value in letters_map.values())
