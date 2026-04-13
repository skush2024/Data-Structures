"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""

class Solution:
    def bruteForce(self, nums, k):
        result = []

        for i in range(len(nums) - k + 1):
            result.append(max(nums[i: i + k])) 

        return result
    
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        
        dq = [0] * n   # will store indices
        front = 0
        back = -1
        
        res = []

        for i in range(n):

            # 1. Remove out-of-window element
            if front <= back and dq[front] == i - k:
                front += 1

            # 2. Remove smaller elements from back
            while front <= back and nums[i] > nums[dq[back]]:
                back -= 1

            # 3. Insert current index
            back += 1
            dq[back] = i

            # 4. Add result when window is valid
            if i >= k - 1:
                res.append(nums[dq[front]])

        return res
    

if __name__ == "__main__":
    solver = Solution()
    
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    print(solver.maxSlidingWindow(nums, k))

        