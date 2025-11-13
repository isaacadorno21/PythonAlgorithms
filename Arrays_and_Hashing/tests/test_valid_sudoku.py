import unittest
from Arrays_and_Hashing.src.valid_sudoku import Solution


class TestSolution(unittest.TestCase):
    def test_valid_example_from_doc(self):
        board = [
            ["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","8",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"],
        ]
        expected = True
        actual = Solution().isValidSudoku(board)
        self.assertEqual(expected, actual)

    def test_invalid_subbox_from_doc(self):
        board = [
            ["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","1",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"],
        ]
        expected = False
        actual = Solution().isValidSudoku(board)
        self.assertEqual(expected, actual)

    def test_invalid_row_duplicate(self):
        board = [["."] * 9 for _ in range(9)]
        board[0] = ["5","3",".",".","7",".",".",".","5"]  # two 5s in row 0
        expected = False
        actual = Solution().isValidSudoku(board)
        self.assertEqual(expected, actual)

    def test_invalid_column_duplicate(self):
        board = [["."] * 9 for _ in range(9)]
        board[0][1] = "7"
        board[8][1] = "7"  # two 7s in column 1
        expected = False
        actual = Solution().isValidSudoku(board)
        self.assertEqual(expected, actual)

    def test_empty_board_valid(self):
        board = [["."] * 9 for _ in range(9)]
        expected = True
        actual = Solution().isValidSudoku(board)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()