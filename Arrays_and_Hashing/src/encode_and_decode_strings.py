"""
Problem Description: - 

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
"""


class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += str(len(string)) + "#" + string
        return encoded_str

    def decode(self, s: str) -> list[str]:
        decoded_str_list = []
        i = 0
        while i < len(s):
            # Determine the length of the string - look at all the numbers before #
            j = i
            while s[j] != '#':
                j += 1
            length_of_str = int(s[i:j])

            # Move pointers towards the actual string
            i = j + 1
            j = i + length_of_str

            # Add to list
            decoded_str_list.append(s[i:j])

            i = j
        return decoded_str_list