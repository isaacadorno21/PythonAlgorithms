import unittest
from Arrays_and_Hashing.src.valid_anagram import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "racecar"
        t = "carrace"
        expected = True
        actual = Solution().isAnagram(s, t)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "jar"
        t = "jam"
        expected = False
        actual = Solution().isAnagram(s, t)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "anagram"
        t = "nagaram"
        expected = True
        actual = Solution().isAnagram(s, t)
        self.assertEqual(expected, actual)

    def test_4(self):
        s = "rat"
        t = "car"
        expected = False
        actual = Solution().isAnagram(s, t)
        self.assertEqual(expected, actual)

    def test_5(self):
        s = "a"
        t = "a"
        expected = True
        actual = Solution().isAnagram(s, t)
        self.assertEqual(expected, actual)

    def test_6(self):
        s = "a"
        t = "b"
        expected = False
        actual = Solution().isAnagram(s, t)
        self.assertEqual(expected, actual)

    def test_7(self):
        s = ""
        t = ""
        expected = True
        actual = Solution().isAnagram(s, t)
        self.assertEqual(expected, actual)

    def test_8(self):
        s = "aaabbb"
        t = "bbbaaa"
        expected = True
        actual = Solution().isAnagram(s, t)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()