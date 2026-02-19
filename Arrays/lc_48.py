"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time Taken by {func.__name__}: {end - start}")
        return result 

    return wrapper


class Solution:

    matrix = None

    def __init__(self, matrix):
        self.matrix = matrix.copy()

    
    @timeit
    def solve(self):
        # Steps: 1. Transpose + Reverse Each Row
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                if row < col:
                    self.matrix[row][col], self.matrix[col][row] = self.matrix[col][row],self.matrix[row][col]

        for row in self.matrix:
            i = 0 
            j = len(row) - 1
            while(i <= j):
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1

if __name__ == "__main__":
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solver = Solution(matrix)
    print("======= Optimized Approach =======")
    print(solver.matrix)
    print()
    solver.solve()
    print(solver.matrix)



