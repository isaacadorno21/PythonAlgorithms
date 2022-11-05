import unittest
from Arrays_and_Hashing.src.top_k_most_frequent import Solution


class TestSolution(unittest.TestCase):
    def test_simple_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected_1 = [1, 2]
        expected_2 = [2, 1]
        actual = Solution().top_k_most_frequent_simple(nums, k)
        self.assertTrue(expected_1 == actual or expected_2 == actual)

    def test_simple_2(self):
        nums = [1]
        k = 1
        expected = [1]
        actual = Solution().top_k_most_frequent_simple(nums, k)
        self.assertEqual(expected, actual)

    def test_dictionary_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected_1 = [1, 2]
        expected_2 = [2, 1]
        actual = Solution().top_k_most_frequent_dictionary(nums, k)
        self.assertTrue(expected_1 == actual or expected_2 == actual)

    def test_dictionary_2(self):
        nums = [1]
        k = 1
        expected = [1]
        actual = Solution().top_k_most_frequent_dictionary(nums, k)
        self.assertEqual(expected, actual)

    def test_heap_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected_1 = [1, 2]
        expected_2 = [2, 1]
        actual = Solution().top_k_most_frequent_heap(nums, k)
        self.assertTrue(expected_1 == actual or expected_2 == actual)

    def test_heap_2(self):
        nums = [1]
        k = 1
        expected = [1]
        actual = Solution().top_k_most_frequent_heap(nums, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
