"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""

class Solution:

    def __init__(self):
        pass

    
    def generateBoard(self, n):
        board = [["." for i in range(n)] for j in range(n)]
        return board

    
    def is_safe(self, board, row, col):
        # Any position can be attacked only by the previous row
        for r in range(row):
            if board[r][col] == 'Q':
                return False
            
        # Attacks from left diagnol 
        r,c = row - 1, col - 1
        while r >= 0 and c >=0 :
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -=1

        # Attacks from right diagnol
        r,c = row - 1, col + 1
        while r >= 0 and c < len(board):
            if board[r][c] == 'Q':
                return False
        
            r -= 1
            c += 1

        return True
    
    def solveNQueens(self, n):
        board = self.generateBoard(n)
        result = []

        def backtrack(row):

            if row == n :
                result.append(["".join(r) for r in board])
                return
            

            for col in range(n):
                if self.is_safe(board, row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        backtrack(0)
        print(result)
    
if __name__ == "__main__" :
    solver = Solution()

    n = 1

    solver.solveNQueens(n)