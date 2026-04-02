"""
Given a grid of dimensions n x n. A rat is placed at coordinates (0, 0) and wants to reach at coordinates (n-1, n-1).

Find all possible paths that rat can take to travel from (0, 0) to (n-1, n-1). The directions in which rat can move are 'U' (up) , 'D' (down) , 'L' (left) , 'R' (right).

The value 0 in grid denotes that the cell is blocked and rat cannot use that cell for travelling, whereas value 1 represents that rat can travel through the cell. If the cell (0, 0) has 0 value, then mouse cannot move to any other cell.

Note :
In a path no cell can be visited more than once.
If there is no possible path then return empty vector.s
"""


class Solution:

    def __init__(self):
        pass

    def possibleMove(self, row, col, n):
        actions = ["U", "D", "L", "R"]

        if row == n - 1:
            actions.remove("D")

        if row == 0:
            actions.remove("U")

        if col == n - 1 :
            actions.remove("R")

        if col == 0:
            actions.remove("L")

        return actions
    
    
    def validMove(self, grid, row, col,action, visited):
        match action:
            case "U" :
                row -= 1
            
            case "D" :
                row += 1
            
            case "L":
                col -= 1
            
            case "R":
                col += 1
        
        if grid[row][col] != 0 and [row,col] not in visited:
            return True, row, col
        
        return False, row, col
    
    
    
    def findPath(self, grid):
        paths = []

        def backtrack(row, col, path = "", visited = []):
            visited.append([row,col])

            if row == len(grid) - 1 and col == len(grid) - 1 :
                paths.append(path)
                return
            
            valid_actions = self.possibleMove(row, col, len(grid)) 
            
            for action in valid_actions:
                valid, n_row, n_col = self.validMove(grid, row, col, action, visited)
                
                if valid:
                    backtrack(n_row, n_col, path + action,visited)
                    visited.pop()
        

        backtrack(0,0)
    
        return paths if len(paths) >= 1 else -1
    


if __name__ == "__main__" :
    solver = Solution()

    grid = [ [1, 0, 0] , [1, 1, 0], [0, 1, 1] ]
    print(solver.findPath(grid))