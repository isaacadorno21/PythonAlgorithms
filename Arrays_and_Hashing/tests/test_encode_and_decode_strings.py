import unittest
from Arrays_and_Hashing.src.encode_and_decode_strings import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        data = ["neet", "code", "love", "you"]
        s = Solution()
        encoded = s.encode(data)
        print(encoded)
        decoded = s.decode(encoded)
        print(decoded)
        self.assertEqual(data, decoded)

    def test_example_2(self):
        data = ["we", "say", ":", "yes"]
        s = Solution()
        encoded = s.encode(data)
        decoded = s.decode(encoded)
        self.assertEqual(data, decoded)

    def test_empty_list(self):
        data = []
        s = Solution()
        encoded = s.encode(data)
        decoded = s.decode(encoded)
        self.assertEqual(data, decoded)

    def test_single_empty_string(self):
        data = [""]
        s = Solution()
        encoded = s.encode(data)
        decoded = s.decode(encoded)
        self.assertEqual(data, decoded)

    def test_contains_delimiter(self):
        data = ["a|b", "|", "||", "end|"]
        s = Solution()
        encoded = s.encode(data)
        decoded = s.decode(encoded)
        self.assertEqual(data, decoded)


if __name__ == "__main__":
    unittest.main()