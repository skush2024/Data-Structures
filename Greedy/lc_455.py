"""
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], 
which is the minimum size of a cookie that the child will be content with; 

and each cookie j has a size s[j]. 
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 

Your goal is to maximize the number of your content children and output the maximum number.
"""


class Solution:

    def __init__(self):
        pass


    def findContentChildren(self, g, s):
        kid = 0
        cookie = 0 

        kids_satisfied = 0
        
        while (kid < len(g) and cookie < len(s)):
            grid = g[kid]
            size = s[cookie]

            if grid <= size :
                kids_satisfied += 1
                cookie += 1
                kid += 1
            
            else :
                cookie += 1

        
        return kids_satisfied
    

if __name__ == "__main__" :
    solver = Solution()

    grid = [1,2]
    size = [1,2,3]

    print(solver.findContentChildren(grid, size))




