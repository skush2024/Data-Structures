"""
You are given an integer array nums. 
The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

class Solution:

    def previousSmallest(self, arr):
        stack = []
        result = []

        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]] :
                stack.pop()

            result.append(stack[-1] if stack else -1)
            stack.append(i)

        return result
    
    def nextSmallest(self, arr):
        stack = []
        result = []

        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]] :
                stack.pop()

            result.append(stack[-1] if stack else len(arr))
            stack.append(i)

        return result[::-1]

    def sumOfMinimums(self, arr):
        pse = self.previousSmallest(arr)
        nse = self.nextSmallest(arr)
        result = 0

        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i 
            contribution = arr[i] * (left * right) 
            result += contribution

        return result

    def previousLargest(self, arr):
        stack = []
        result = []

        for i in range(len(arr)):
            while stack and arr[i] > arr[stack[-1]] :
                stack.pop()

            result.append(stack[-1] if stack else -1)
            stack.append(i)
        
        return result

    def nextLargest(self, arr):
        stack = []
        result = []

        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            
            result.append(stack[-1] if stack else len(arr))
            stack.append(i)

        return result[::-1]

    def sumOfMaximums(self, arr):
        pse = self.previousLargest(arr)
        nse = self.nextLargest(arr)
        result = 0

        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i 
            contribution = arr[i] * (left * right)
            result += contribution

        return result


    def subArrayRanges(self, nums) :
        sumMax = self.sumOfMaximums(nums)
        sumMin = self.sumOfMinimums(nums)
        return sumMax - sumMin