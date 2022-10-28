import unittest
from Arrays_and_Hashing.src.longest_common_prefix import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        actual = Solution().longest_common_prefix(strs)
        self.assertEqual(expected, actual)

    def test_2(self):
        strs = ["dog", "racecar", "car"]
        expected = ""
        actual = Solution().longest_common_prefix(strs)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
