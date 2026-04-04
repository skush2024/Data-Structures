"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:

    def __init__(self):
        pass

    def lowerBound(self, nums, target):
        lb = len(nums)
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = int((low + high) / 2)

            if nums[mid] >= target:
                lb = mid 
                high = mid - 1
            
            else:
                low = mid + 1

        
        return lb
    

    def upperBound(self, nums, target):
        ub = len(nums)
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = int((low + high) / 2)

            if nums[mid] > target:
                ub = mid 
                high = mid - 1
            
            else:
                low = mid + 1

        
        return ub
    


    
    def search(self, nums, target):
        lb = self.lowerBound(nums, target)
        ub = self.upperBound(nums, target) - 1

        if (lb == len(nums)) or (nums[lb] != target):
            return [-1,-1]
        
        return [lb, ub]

if __name__ == "__main__":
    nums = [1,2,3]
    solver = Solution()
    print(solver.search(nums, 1))
