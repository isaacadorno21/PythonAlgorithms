"""Problem Description: - Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def invert_tree(self, root: [TreeNode]) -> [TreeNode]:
        if root is None:
            return None
        temp = self.invert_tree(root.right)
        root.right = self.invert_tree(root.left)
        root.left = temp
        return root


'''
Notes on the solution:
- To do it recursively, we want to focus on switching left and right whilst being concious of using the original
values for each. We could also do this as:
    - root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
'''