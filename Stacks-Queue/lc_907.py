"""
Given an array of integers arr, find the sum of min(b), where 
b ranges over every (contiguous) subarray of arr. 
Since the answer may be large, return the answer modulo 109 + 7.
"""

class Solution:
    
    def prev_smallest(self, arr):
        stack = []
        pse = []

        for i in range(len(arr)):
            while stack and nums[i] <= arr[stack[-1]]:
                stack.pop()
            
            pse.append(stack[-1] if stack else -1)
            stack.append(i)

        return(pse)
    

    def next_smallest(self, arr):
        stack = []
        nse = []
        

        for i in range(len(arr) - 1, -1,-1):
            while stack and arr[i] < arr[stack[-1]] :
                stack.pop()
            
            nse.append(stack[-1] if stack else len(arr))
            stack.append(i)

        return(nse[::-1])


    
    def sumSubarrayMins(self, arr):
        pse = self.prev_smallest(arr)
        nse = self.next_smallest(arr)
        result = 0
        mod = (10**9) + 7

        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            
            contribution = arr[i] * (left * right) 
            result += contribution % mod

        return result

        
if __name__ == "__main__":
    solver = Solution()
    nums = [3,1,2,4]
    print(solver.sumSubarrayMins(nums))