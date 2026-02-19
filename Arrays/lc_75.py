"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f" Time Taken by {func.__name__}: {end - start}")
        return result 

    return wrapper



class Solution:

    nums = None 

    def __init__(self, nums):
        self.nums = nums

    
    def swap(self, posA, posB):
        temp = self.nums[posA]
        self.nums[posA] = self.nums[posB]
        self.nums[posB] = temp

    
    @timeit
    def bruteForce(self):
        """
        Time Taken is O(n^2)
        """
        for i in range(0, len(self.nums) - 1):
            for j in range(i + 1,len(self.nums)):
                if self.nums[i] > self.nums[j]:
                    self.swap(i,j)

    
    
    @timeit
    def solve(self):
        if len(self.nums) <= 1 :
            pass

        low = 0 
        mid = 0
        high = len(self.nums) - 1

        while(mid <= high) :
            elem = self.nums[mid]

            if elem == 0:
                self.swap(low, mid)
                mid += 1
                low += 1
            
            elif elem == 1:
                mid += 1
            
            else :
                self.swap(mid, high)
                high -= 1
        
    
if __name__ == "__main__":
    nums = [1,2,2]
    solver1 = Solution(nums)
    solver2 = Solution(nums.copy())
   

    print("====== Optimized Approach ======")
    print()
    print(solver1.nums)
    solver1.solve()
    print(solver1.nums)
    print()
    
    print("====== Brute Force ======")
    print()
    print(solver2.nums)
    solver2.bruteForce()
    print()
    print(solver2.nums)



    