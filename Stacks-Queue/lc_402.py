"""
Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for char in num:
            while stack and k > 0 and char < stack[-1]:
                stack.pop()
                k -= 1

            stack.append(char)
        
        stack = stack[:-k] if k > 0 else stack
        result = ''.join(stack).lstrip("0")
        
        return result if result else "0"
        


if __name__ == "__main__":
    solver = Solution()
    
    nums = "9"
    k = 1
    print(solver.removeKdigits(nums, k))