"""
Given an array of integers heights representing the histogram's bar height 
where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.
"""

class Solution:

    def nearestSmallest(self, arr):
        stack = []
        result = []
        
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()

            result.append(stack[-1] if stack else -1)
            stack.append(i)

        return result
    
    def nextSmallest(self, arr):
        stack = []
        result = []

        for i in range(len(arr) - 1, -1,-1):
            while stack and arr[i] <= arr[stack[-1]] :
                stack.pop()
            
            result.append(stack[-1] if stack else len(arr))
            stack.append(i)
    
        return result[::-1]


    def largestRectangleArea(self, heights):
        pse = self.nearestSmallest(heights)
        nse = self.nextSmallest(heights)

        result = 0
        for i in range(len(heights)):
            
            left = i - pse[i]
            right = nse[i] - i - 1
            width = left + right
            area = heights[i] * width
            result = max(result, area)

        return result
    
    def largestRectangleArea2(self, heights):
        stack = []
        result = 0

        for idx in range(len(heights)):
            while stack and heights[idx] < heights[stack[-1]]:
                popped = stack.pop()
                
                # Next Smallest Element of popped is heights[idx] 
                # Previous Smallest Element of Popped is stack[-1]
                nse_popped = idx
                pse_popped = stack[-1] if stack else -1
                area = heights[popped] * (nse_popped - pse_popped - 1)
                result = max(area, result)            
            
            stack.append(idx)

        for idx in range(len(stack)) :
            nse = len(heights)
            pse = stack[idx - 1] if idx > 0 else -1
            area = heights[stack[idx]] * (nse - pse - 1)
            result = max(area, result)

        return result



if __name__ == "__main__":
    solver = Solution()
    nums = [2,1,5,6,2,3]

    print(solver.largestRectangleArea2(nums))