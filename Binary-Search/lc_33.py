"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:

    def __init__(self):
        pass
    

    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        while(low <= high):
            mid = int((low + high) / 2)

            if nums[mid] == target :
                return mid

            # This means left part is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else :
                    low = mid + 1

            # This means right part is sorted
            else :
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else :
                    high = mid - 1

        
        return -1
        

if __name__ == "__main__":
    solver = Solution()

    nums = [4,5,6,7,8,9,2]
    print(solver.search(nums, 8))