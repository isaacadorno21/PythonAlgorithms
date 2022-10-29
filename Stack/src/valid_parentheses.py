"""Problem Description: - Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine
if the input string is valid. An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
"""


class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for bracket in s:
            if bracket in mapping.values():
                if len(stack) == 0: return False
                stack_top = stack.pop()
                if mapping[stack_top] != bracket:
                    return False
            else:
                stack.append(bracket)
        return len(stack) == 0


'''
Notes on the solution:
- Ordering is important, and we want to compare elements to previous elements in order, so a stack is a good choice.
Going through we add to the stack when it's an open bracket, and pop when it is a closed bracket; this let's us 
determine whether they are matched up correctly or not.
'''
