"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

"""


class Solution:

    def __init__(self, m,n):
        self.m = m
        self.n = n
        self.grid = [[0] * self.n] * self.m
        self.dest = [self. m  - 1, self.n - 1]


    def canMoveRight(self,pos):
        if (pos[1] < self.n - 1):
            return True
        
        return False
    
    def canMoveDown(self,pos):
        if (pos[0] < self.m - 1):
            return True
        return False
    
    def factorial(self, n):
        if n == 1 or n == 0 :
            return 1
        
        else :
            return n * self.factorial(n - 1)
    
    def uniquePaths(self):
        unique_paths = int(self.factorial(self.m + self.n - 2) / (self.factorial(self.m - 1) * self.factorial(self.n - 1)))
        return unique_paths


    
                
    def generateAllTrajectories(self):
        result = []
        
        def dfs(row, col, path):
            # global result
            if row >= self.m  or col >= self.n: 
                return

            path.append([row,col])

            if row == self.dest[0] and col == self.dest[1]:
                result.append(path.copy())
                return 
            else :            
                dfs(row, col + 1, path)
                dfs(row + 1, col, path)

            path.pop()       

        dfs(0,0,[])
        return result
    

    
        
if __name__ == "__main__":
    solver = Solution(3,2)
    print(solver.generateAllTrajectories())
        

        