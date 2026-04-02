"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""

class Solution :

    def __init__(self):
        pass

    
    def check_in_grid(self,board, row, col, num):
        grid_row = (row // 3) * 3
        grid_col = (col // 3) * 3

        for r in range(grid_row, grid_row + 3):
            for c in range(grid_col, grid_col + 3):
                if board[r][c] == str(num):
                    return True
                
        
        return False    
    
    def check_in_row(self, board, row, num):
        return str(num) in board[row]
    
    def check_in_col(self, board, col, num):
        for row in range(9):
            if board[row][col] == str(num):
                return True
        
        return False


    def is_safe(self,board, row, col, num):
        in_grid_valid = not self.check_in_grid(board, row, col, num)
        in_row_valid = not self.check_in_row(board, row, num)
        in_col_valid = not self.check_in_col(board, col, num)
        
        return in_grid_valid and in_row_valid and in_col_valid
    
    
    
    
    def solveSudoku(self, board):
        solution = []
        
        def backtrack(row, col):
            if row == 9 :
                return True
        
            if col == 9:
                return backtrack(row + 1, 0)
            
            if board[row][col] != ".":
                return backtrack(row, col + 1)
                
            for number in range(1,10):
                if self.is_safe(board, row, col, number):
                    board[row][col] = str(number)
                    
                    if backtrack(row, col + 1):
                        return True
                    
                    board[row][col] = "."
                
            return False
        
        backtrack(0,0)
        print(board)

    
    def solveSudoku2(self, board):

        rows = [[False]*10 for _ in range(9)]
        cols = [[False]*10 for _ in range(9)]
        boxes = [[False]*10 for _ in range(9)]

        # Step 1: initialize state
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = int(board[r][c])
                    b = (r//3)*3 + (c//3)
                    rows[r][num] = True
                    cols[c][num] = True
                    boxes[b][num] = True

        def backtrack(r, c):

            if r == 9:
                return True

            if c == 9:
                return backtrack(r+1, 0)

            if board[r][c] != ".":
                return backtrack(r, c+1)

            b = (r//3)*3 + (c//3)

            for num in range(1, 10):
                if not rows[r][num] and not cols[c][num] and not boxes[b][num]:

                    board[r][c] = str(num)
                    rows[r][num] = cols[c][num] = boxes[b][num] = True

                    if backtrack(r, c+1):
                        return True

                    board[r][c] = "."
                    rows[r][num] = cols[c][num] = boxes[b][num] = False

            return False

        backtrack(0, 0)
        print(board)




if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]


    solver = Solution()
    solver.solveSudoku2(board)