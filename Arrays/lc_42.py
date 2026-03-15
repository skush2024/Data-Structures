"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""

class Solution:

    def __init__(self):
        pass


    def bruteForce(self, height):
        maxi = height[0]
        hmap = {}

        for i in range(1, len(height) - 1):
            hmap[i] = [maxi]
            maxi = max(maxi, height[i])
            
        maxi = height[len(height) - 1]
        for i in range(len(height) - 2, 0, -1):
            hmap[i].append(maxi)
            maxi = max(maxi, height[i])


        water = 0
        for i in range(1, len(height) - 1):
            if min(hmap[i]) > height[i] :
                water += min(hmap[i]) - height[i]

        return water

    def solve(self, height):
        n = len(height)

        left, right = 0, n - 1

        max_left, max_right = 0,0

        total_water = 0

        while left <= right :
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]

                else :
                    total_water += max_left - height[left]
                
                left += 1

            else :
                if height[right] >= max_right:
                    max_right = height[right]

                else :
                    total_water += max_right - height[right]
                
                right -= 1

        print(total_water)
        
if __name__ == "__main__":
    solver = Solution()
    solver.solve([0,1,0,2,1,0,1,3,2,1,2,1])