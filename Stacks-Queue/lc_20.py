"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 :
            return False
        

        rules = {')' : '(',
                '}' : '{',
                ']' : '['}
        
        stack = []
        top = -1

        for char in s :
            if char in rules :
                if top >= 0 and stack[top] == rules[char]:
                    stack.pop()
                    top -= 1
                else :
                    return False
            else :
                stack.insert(top + 1, char)
                top += 1
        
        return not stack and True


if __name__ == "__main__":
    solver = Solution()
    s = '((([]))()'
    print(solver.isValid(s))