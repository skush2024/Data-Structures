"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[-1 for _ in range(n)] for _ in range(m)] 
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                up = grid[i][j] + dp[i - 1][j] if i > 0 else float('inf')
                left = grid[i][j] + dp[i][j - 1] if j > 0 else float('inf')

                dp[i][j] = min(up, left)

        return dp[m - 1][n - 1]
                

