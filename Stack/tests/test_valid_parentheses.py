import unittest
from Stack.src.valid_parentheses import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "()"
        expected = True
        actual = Solution().is_valid(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "()[]{}"
        expected = True
        actual = Solution().is_valid(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "(]"
        expected = False
        actual = Solution().is_valid(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
