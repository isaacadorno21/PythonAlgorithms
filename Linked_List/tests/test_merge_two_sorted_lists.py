import unittest
from Linked_List.src.merge_two_sorted_lists import *


class TestSolution(unittest.TestCase):
    def test_1(self):
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        expected = ListNode(1, ListNode(1, ListNode(
            2, ListNode(3, ListNode(4, ListNode(4))))))
        actual = Solution().merge_two_lists_iterative(list1, list2)
        self.assertEqual(expected.val, actual.val)

    def test_2(self):
        list1 = None
        list2 = None
        expected = None
        actual = Solution().merge_two_lists_iterative(list1, list2)
        self.assertEqual(expected, actual)

    def test_3(self):
        list1 = None
        list2 = ListNode(0)
        expected = ListNode(0)
        actual = Solution().merge_two_lists_iterative(list1, list2)
        self.assertEqual(expected.val, actual.val)
        self.assertEqual(expected.next, actual.next)

    '''
    # Small testing error with 'self' keyword
    def test_4(self):
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
        actual = Solution().merge_two_lists_recursive(list1, list2)
        self.assertEqual(expected.val, actual.val)
    '''

    def test_5(self):
        list1 = None
        list2 = None
        expected = None
        actual = Solution().merge_two_lists_recursive(self, list1, list2)
        self.assertEqual(expected, actual)

    def test_6(self):
        list1 = None
        list2 = ListNode(0)
        expected = ListNode(0)
        actual = Solution().merge_two_lists_recursive(self, list1, list2)
        self.assertEqual(expected.val, actual.val)
        self.assertEqual(expected.next, actual.next)


if __name__ == '__main__':
    unittest.main()
