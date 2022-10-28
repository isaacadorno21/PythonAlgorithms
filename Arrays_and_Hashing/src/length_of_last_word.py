"""Problem Description: - Given a string s consisting of words and spaces, return the length of the last word in the
string. A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


class Solution:
    @staticmethod
    def length_of_last_word_one(s: str) -> int:
        words = s.split()
        return len(words[-1])

    @staticmethod
    def length_of_last_word_two(s: str) -> int:
        i, length = len(s) - 1, 0
        while s[i] == " ":  # Trim any white space at the end
            i -= 1
        while i >= 0 and s[i] != " ":  # Iterate over the last word until we find the spaces before it
            length += 1
            i -= 1
        return length


'''
Notes on the solution: 
- Most straightforward solution to me is using built in Python String split() method. We just return the length of 
the last word after splitting the string into different words. Default is whitespace so I left it like that.
Split is an O(n) operation.

Other solutions: 
- We could also trim the white space off the ends of the string, find the index of the last white space inbetween the
words, and get the length of the word from there until the end.
- Without using built-in functions like trim() or split(), we can use two while loops to go through and find the
location of our spaces.
'''
