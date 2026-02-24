"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity

"""
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start}s.")
        return result
    
    return wrapper

class Solution:
    
    matrix = None  

    def __init__(self, matrix):
        self.matrix = matrix



    def getRow(self, target):
        low = 0 
        high = len(self.matrix) - 1
        while(low <= high):
            mid = int((low + high) / 2)
            first_elem = self.matrix[mid][0]
            if first_elem > target :
                high = mid - 1
            else :
                low = mid + 1
        
        return high


    def binarySearch(self, arr, target):
        low = 0 
        high = len(arr) - 1
        while(low <= high):
            mid = int((low + high) / 2)
            if arr[mid] == target :
                return True
            
            elif arr[mid] > target :
                high = mid - 1
            
            elif arr[mid] < target:
                low = mid + 1
        
        return False


    @timeit
    def solve(self, target):
        row_to_search = self.getRow(target)
        result = self.binarySearch(self.matrix[row_to_search], target)
        return result


if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 5

    solver = Solution(matrix)
    print(solver.solve(target))



