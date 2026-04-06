"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

"""
class Solution:

    def __init__(self):
        pass
    

    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        while(low <= high):
            mid = int((low + high) / 2)

            if nums[mid] == target :
                return True

            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            
            else :
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
                

        
        return False
    
if __name__ == "__main__":
    nums = [1,0,1,1,1]
    solver = Solution()
    print(solver.search(nums,0))