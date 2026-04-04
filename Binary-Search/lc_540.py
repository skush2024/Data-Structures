"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
"""

class Solution:

    def __init__(self):
        pass

    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = int((low + high) / 2)

            if mid % 2 == 1 :
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            
            else :
                high = mid
        
        return nums[low]

if __name__ == "__main__" :
    nums = [1,1,2,2,3,3,4,4,8]

    solver = Solution()
    print(solver.singleNonDuplicate(nums))

