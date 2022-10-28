import unittest
from Arrays_and_Hashing.src.length_of_last_word import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "Hello World"
        expected = 5
        actual = Solution().length_of_last_word_one(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "   fly me   to   the moon  "
        expected = 4
        actual = Solution().length_of_last_word_one(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "luffy is still joyboy"
        expected = 6
        actual = Solution().length_of_last_word_one(s)
        self.assertEqual(expected, actual)

    def test_4(self):
        s = "Hello World"
        expected = 5
        actual = Solution().length_of_last_word_two(s)
        self.assertEqual(expected, actual)

    def test_5(self):
        s = "   fly me   to   the moon  "
        expected = 4
        actual = Solution().length_of_last_word_two(s)
        self.assertEqual(expected, actual)

    def test_6(self):
        s = "luffy is still joyboy"
        expected = 6
        actual = Solution().length_of_last_word_two(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
