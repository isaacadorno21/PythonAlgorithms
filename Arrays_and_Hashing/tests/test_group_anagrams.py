import unittest
from Arrays_and_Hashing.src.group_anagrams import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        actual = Solution().group_anagrams(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = [""]
        expected = [[""]]
        actual = Solution().group_anagrams(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = ["a"]
        expected = [["a"]]
        actual = Solution().group_anagrams(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
