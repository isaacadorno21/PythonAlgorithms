import unittest
from Arrays_and_Hashing.src.valid_anagram import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "anagram"
        t = "nagaram"
        expected = True
        actual = Solution().is_anagram(s, t)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "rat"
        t = "car"
        expected = False
        actual = Solution().is_anagram(s, t)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
