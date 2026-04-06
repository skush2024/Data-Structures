"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.
"""

class Solution:

    def __init__(self):
        pass
    

    def findMin(self, nums):
        ans = 5001
        low, high = 0, len(nums) - 1

        while(low <= high):
            mid = int((low + high) / 2)

            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                ans = min(ans, nums[mid])
                low += 1
                high -= 1
                continue

            # This means left part is sorted
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1

            # This means right part is sorted
            else :
                ans = min(ans, nums[mid])
                high = mid - 1

        
        return ans
    
if __name__ == "__main__":
    nums = [1,0,1,1,1]
    solver = Solution()

    print(solver.findMin(nums))