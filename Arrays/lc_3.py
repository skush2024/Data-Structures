"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

class Solution:
    def __init__(self):
        pass

    def bruteforce(self, s):
        longest = 0

        if len(s) <= 1 :
            return len(s)

        l = 0 
        r = 1
        
        traversed = {s[l]}
        cur_length = 1
        
        while(l < r and r < len(s)):
            
            
            if s[r] in traversed :
                longest = max(longest, cur_length)
                l += 1
                r = l + 1
                traversed = {s[l]}
                cur_length = 1
            
            else :
                traversed.add(s[r])
                cur_length += 1 
                r += 1

        longest = max(longest, cur_length)
        return longest


    def solve(self, s):
        traversed = set()
        left, longest = 0,0

        for right in range(len(s)):
            while s[right] in traversed :
                traversed.remove(s[left])
                left += 1
            
            traversed.add(s[right])
            longest = max(longest, right - left + 1)

        return longest





    

if __name__ == "__main__" :
    s = "dvdf"
    solver = Solution()
    print(solver.solve(s))