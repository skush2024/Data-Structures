"""
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.
"""

def checkPalindrome(s):
    return s == s[::-1]



class Solution:

    def __init__(self):
        pass


    def partition(self, s):
        partitions = []
        
        def backtrack(start_idx=0, path=[]):
            if start_idx == len(s):
                partitions.append(path.copy())
                return


            for substr_idx in range(start_idx, len(s)):
                substr = s[start_idx:substr_idx + 1]
                if checkPalindrome(substr):
                    path.append(substr)
                    backtrack(substr_idx + 1, path)
                    path.pop()
                
                
        backtrack()
        return(partitions)


if __name__ == "__main__" :
    s = "aabaa"
    
    solver = Solution()
    solver.partition(s)

