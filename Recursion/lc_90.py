"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution:

    def __init__(self):
        pass


    def subsetsWithDupl(self, nums, idx, output,ans):
        if len(nums) == idx :
            output.append(ans.copy())
            return
    
        
        ans.append(nums[idx])
        self.subsetsWithDupl(nums, idx + 1, output, ans)
        
        ans.pop()
        i = idx + 1
        
        while(i < len(nums) and nums[i] == nums[i - 1]) : 
            i+= 1
        
        self.subsetsWithDupl(nums, i, output, ans)
        
    def subsets(self, nums):
        nums.sort()
        output = []
        self.subsetsWithDupl(nums, 0, output, [])
        print(output)
        

if __name__ == "__main__":
    solver = Solution()

    nums = [1,2,2]
    solver.subsets(nums)