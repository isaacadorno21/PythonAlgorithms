import unittest
from Arrays_and_Hashing.src.product_of_array_except_self import Solution


class TestSolution(unittest.TestCase):
    # Test Case 1: Standard positive integers (from Example 1)
    def test_1_standard_positive(self):
        """Input: [1, 2, 3, 4] -> Output: [24, 12, 8, 6]"""
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        actual = Solution().productExceptSelf(nums)
        self.assertEqual(expected, actual)

    # Test Case 2: Array containing a single zero (from Example 2)
    # This checks the edge case where one zero makes the product of all others zero,
    # except for the element at the zero's index.
    def test_2_single_zero(self):
        """Input: [-1, 1, 0, -3, 3] -> Output: [0, 0, 9, 0, 0]"""
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0] # product(-1, 1, -3, 3) = 9
        actual = Solution().productExceptSelf(nums)
        self.assertEqual(expected, actual)
        
    # Test Case 3: Array containing multiple zeros
    # If there are two or more zeros, every element's product-except-self must be 0.
    def test_3_multiple_zeros(self):
        """Input: [1, 2, 0, 4, 0] -> Output: [0, 0, 0, 0, 0]"""
        nums = [1, 2, 0, 4, 0]
        expected = [0, 0, 0, 0, 0]
        actual = Solution().productExceptSelf(nums)
        self.assertEqual(expected, actual)

    # Test Case 4: Array with negative numbers
    def test_4_negative_numbers(self):
        """Input: [-2, -3, 4, -1] -> Output: [-12, -8, 6, 24]"""
        # Product = 24
        # i=0 (-2): -3 * 4 * -1 = 12. Corrected: Product/nums[0] = 24 / -2 = -12
        # i=1 (-3): -2 * 4 * -1 = 8. Corrected: 24 / -3 = -8
        # i=2 (4): -2 * -3 * -1 = -6. Corrected: 24 / 4 = 6
        # i=3 (-1): -2 * -3 * 4 = 24. Corrected: 24 / -1 = -24 (Wait, the product is (-2)*(-3)*(4)*(-1) = -24)
        
        # Recalculating expected for nums = [-2, -3, 4, -1]
        # Total Product (P) = -2 * -3 * 4 * -1 = -24
        # i=0 (P/-2) = -24 / -2 = 12
        # i=1 (P/-3) = -24 / -3 = 8
        # i=2 (P/4) = -24 / 4 = -6
        # i=3 (P/-1) = -24 / -1 = 24
        nums = [-2, -3, 4, -1]
        expected = [12, 8, -6, 24]
        actual = Solution().productExceptSelf(nums)
        self.assertEqual(expected, actual)

    # Test Case 5: Minimum size array (length 2)
    def test_5_min_length(self):
        """Input: [5, 10] -> Output: [10, 5]"""
        nums = [5, 10]
        expected = [10, 5]
        actual = Solution().productExceptSelf(nums)
        self.assertEqual(expected, actual)

    # Test Case 6: Larger array with mixed numbers
    def test_6_larger_mixed(self):
        """Input: [1, -5, 2, 0, 3] -> Output: [0, 0, 0, -30, 0]"""
        # Product of non-zero elements: 1 * -5 * 2 * 3 = -30
        # The zero is at index 3. Only answer[3] should be non-zero (-30).
        nums = [1, -5, 2, 0, 3]
        expected = [0, 0, 0, -30, 0]
        actual = Solution().productExceptSelf(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()