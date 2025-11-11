"""

Problem Description: - Given an array of strings strs, group the anagrams together. You can return the answer in
any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        # mapping = { key - sorted string: value - values that fit this}
        sorted_string_mapping = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in sorted_string_mapping:
                sorted_string_mapping[sorted_str].append(str)
            else:
                sorted_string_mapping[sorted_str] = [str]
        return list(sorted_string_mapping.values())