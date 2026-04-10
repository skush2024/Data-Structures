"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge = {}

        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            nge[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        
        return [nge[i] for i in nums1]
    
    def nearestSmallerElement(self, nums):
        stack = []
        nse =  {}

        for i in range(len(nums)):
            while stack and stack[-1] >= nums[i]:
                stack.pop()

            nse[nums[i]] = stack[-1] if stack else -1
            stack.append(nums[i])
        

        return nse
        
        

if __name__ == "__main__":
        solver = Solution()
        nums1 = [1,2,3]
        nums2 = [1,3,2,0,4,5]
        # print(solver.nextGreaterElement(nums1, nums2))
        print(solver.nearestSmallerElement(nums2))
        