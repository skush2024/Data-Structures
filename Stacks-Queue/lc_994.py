"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.
"""

class Solution:


    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = []
        front = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        minutes = 0
        
        # Directions -> Down, Up, Right, Left
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while front < len(queue):
            size = len(queue) - front
            infected = False

            for _ in range(size):
                r,c = queue[front]
                front += 1

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr and nr < rows) and (0 <= nc and nc < cols) and (grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh -= 1
                        infected = True
                
            if infected:
                minutes += 1
        
        return minutes if fresh == 0 else -1
    

if __name__ == "__main__":
    solver = Solution()
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]]
    
    print(solver.orangesRotting(grid))
        