"""Problem Description: - You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def merge_two_lists(list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        output_list = ListNode()
        temp = output_list
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return output_list.next


'''
Notes on the solution:
- We create a dummy node that serves as the head of our new linked list. we go through and while they both exist,
we compare the heads of each linked list and add whichever head is smaller to our new linked list. We then move 
that head along, and keep going until either or both or finished. If either of them still exist, we can just append 
what's left.
'''
