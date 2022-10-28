import unittest
from Arrays_and_Hashing.src.replace_elements_with_greatest_element_on_right_side import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        arr = [17, 18, 5, 4, 6, 1]
        expected = [18, 6, 6, 6, 1, -1]
        actual = Solution().replace_elements(arr)
        self.assertEqual(expected, actual)

    def test_2(self):
        arr = [400]
        expected = [-1]
        actual = Solution().replace_elements(arr)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
