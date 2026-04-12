"""
Given a rows x cols binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.
"""

class Solution:

    def largestAreaRectangle(self, heights):
        ans = 0
        stack = []

        for idx in range(len(heights)):
            while stack and heights[idx] < heights[stack[-1]]:
                popped_element = stack.pop()

                # NSE of popped element is idx
                # Prev Smallest Element is stack[-1]
                nse_popped = idx
                pse_popped = stack[-1] if stack else -1
                area = heights[popped_element] * (nse_popped - pse_popped - 1)
                ans = max(ans, area)

            stack.append(idx)

        for idx in range(len(stack) - 1, -1, -1):
            nse = len(heights)
            pse = stack[idx - 1] if idx > 0 else -1
            area = heights[stack[idx]] * (nse - pse - 1)
            ans = max(area, ans)

        return ans


    
    def maximalRectangle(self, matrix):
        ans = 0
        heights = [0] * len(matrix[0])

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0

            result = self.largestAreaRectangle(heights)
            ans = max(ans, result)
        
        return ans


if __name__ == "__main__":
    solver = Solution()
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
        ]
    
    print(solver.maximalRectangle(matrix))

