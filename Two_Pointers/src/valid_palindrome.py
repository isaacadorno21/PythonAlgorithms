"""Problem Description: - A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
import re


class Solution:
    @staticmethod
    def is_palindrome_one(s: str) -> bool:
        # could do this with regex...
        # if we don't import re, we can use .isalpha() and iterate over our string,
        # keeping only the alphanumeric characters
        new_str = ''.join([i.lower() for i in s if i.isalnum()])
        return new_str == new_str[::-1]

    @staticmethod
    def is_palindrome_two(s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            left_char = s[left].lower()
            right_char = s[right].lower()
            if left_char != right_char:
                return False
            left += 1
            right -= 1
        return True

    @staticmethod
    def is_palindrome_three(s: str) -> bool:
        new_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return new_s == new_s[::-1]


'''
Notes on the solution:
- Pythonic way without regex would be using a join on a list comprehension of only the lowercase alphanumeric
letters of s, and then checking if it is equivalent to its reverse

Other solutions: 
- Use a two pointer solution - look at left and right, move it if we're not alpha numeric, otherwise check their
equivalency
- Use regex to only include a-z, A-Z, and 0-9
'''
