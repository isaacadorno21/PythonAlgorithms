import unittest
from Two_Pointers.src.valid_palindrome import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "A man, a plan, a canal: Panama"
        expected = True
        actual = Solution().is_palindrome_one(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "race a car"
        expected = False
        actual = Solution().is_palindrome_one(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = " "
        expected = True
        actual = Solution().is_palindrome_one(s)
        self.assertEqual(expected, actual)

    def test_4(self):
        s = "A man, a plan, a canal: Panama"
        expected = True
        actual = Solution().is_palindrome_two(s)
        self.assertEqual(expected, actual)

    def test_5(self):
        s = "race a car"
        expected = False
        actual = Solution().is_palindrome_two(s)
        self.assertEqual(expected, actual)

    def test_6(self):
        s = " "
        expected = True
        actual = Solution().is_palindrome_two(s)
        self.assertEqual(expected, actual)

    def test_7(self):
        s = "A man, a plan, a canal: Panama"
        expected = True
        actual = Solution().is_palindrome_three(s)
        self.assertEqual(expected, actual)

    def test_8(self):
        s = "race a car"
        expected = False
        actual = Solution().is_palindrome_three(s)
        self.assertEqual(expected, actual)

    def test_9(self):
        s = " "
        expected = True
        actual = Solution().is_palindrome_three(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
