"""
Problem Description: -

You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true
Example 2:

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.

"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        We'll do 3 checks for 9 different values
        - Check the rows of [0,0] - [8,0]
        - Check the columns of [0,0] - [0,8]
        - Check the squares of [0,0], [3,0], [6,0], [3,0], ...
        """

        # Check rows
        for i in range (9):
            cur_row = board[i]
            if self.containsDuplicates(cur_row):
                return False

        # Check columns
        for j in range (9):
            cur_col = [row[j] for row in board]
            if self.containsDuplicates(cur_col):
                return False

        # Check squares
        for i in range(0, 9, 3):
            for j in range (0, 9, 3):
                cur_square = []
                for r in range(i, i+3):
                    for c in range (j, j+3):
                        cur_square.append(board[r][c])
                if self.containsDuplicates(cur_square):
                    return False

        return True

    def containsDuplicates(self, row: list[str]) -> bool:
        valid_set = set()
        valid_items = 0
        for item in row:
            if item == '.':
                continue
            valid_set.add(item)
            valid_items += 1
        return valid_items != len(valid_set)
