"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) # Number of Rows
        n = len(obstacleGrid[0]) # Number of Cols

        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def backtrack(i,j):
            if (i == 0 and j == 0):
                return 1
            
            if (i < 0 or j < 0):
                return 0
            
            if (obstacleGrid[i][j] == 1):
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            up = backtrack(i - 1, j)
            left = backtrack(i, j - 1)

            dp[i][j] = up + left
            return dp[i][j]
        
        
        def tabulation():
            dp[0][0] = 1

            for i in range(m):
                for j in range(n):
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    
                    else:
                        if i==0 and j==0:
                            continue
                            
                        up = dp[i - 1][j] if i > 0 else 0
                        left = dp[i][j - 1] if j > 0 else 0
                        
                        dp[i][j] = up + left

            return dp[i][j]

        return tabulation()
        