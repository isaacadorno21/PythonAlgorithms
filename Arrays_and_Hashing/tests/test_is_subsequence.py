import unittest
from Arrays_and_Hashing.src.is_subsequence import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "abc"
        t = "ahbgdc"
        expected = True
        actual_one = Solution().is_subsequence_one(s, t)
        self.assertEqual(expected, actual_one)

    def test_2(self):
        s = "axc"
        t = "ahbgdc"
        expected = False
        actual_one = Solution().is_subsequence_one(s, t)
        self.assertEqual(expected, actual_one)

    def test_3(self):
        s = "abc"
        t = "ahbgdc"
        expected = True
        actual_two = Solution().is_subsequence_two(s, t)
        self.assertEqual(expected, actual_two)

    def test_4(self):
        s = "axc"
        t = "ahbgdc"
        expected = False
        actual_two = Solution().is_subsequence_two(s, t)
        self.assertEqual(expected, actual_two)


if __name__ == '__main__':
    unittest.main()
