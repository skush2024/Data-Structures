"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.
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
    nums = None

    def __init__(self, nums:list):    
        self.nums = nums
    

    @timeit
    def solve(self):
        """
        Since the elements in the list are in range [1,n] and the list has n + 1 elements, 
        we will treat it as a linked list and detect a point which leads to a cycle and we will know its duplicate.
        """

        slow = 0 
        fast = 0 

        while True :
            slow = self.nums[slow]
            fast = self.nums[self.nums[fast]]

            if slow == fast :
                break

        slow = 0
        while slow != fast :
            slow = self.nums[slow]
            fast = self.nums[fast]

        return slow
    
if __name__ == "__main__":
    nums = [1,3,4,2,1]
    solver = Solution(nums)
    print(solver.solve())