"""Problem Description: - Given an array of strings strs, group the anagrams together. You can return the answer in
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
    @staticmethod
    def group_anagrams(strs: list[str]) -> list[list[str]]:
        # Consider using Counters or sets to define what should go where
        mapping = {}
        for s in strs:
            s_key = str(sorted(s))
            if s_key in mapping:
                mapping[s_key].append(s)
            else:
                mapping[s_key] = [s]
        return list(mapping.values())


'''
Notes on the solution: 
- Some challenge in figuring out what we can use as a HashMap key to determine possible 
anagram combinations. I initially wanted to use a set(), but this isn't a hashable type in Python due to the fact 
that it is not immutable. I instead am sorted characters and using that output string to be the key for our hashmap.

Other solutions: 
- If we know we have a limited set of characters we are working with (ex. a-z), we can use that instead of a sorted str. 
'''
