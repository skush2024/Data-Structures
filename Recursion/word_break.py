"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words otherwise return false.

Note : The same word in dictionary can be used multiple times in segmentation.
"""

class Solution:

    def __init__(self):
        pass

    def wordBreak(self, s, wordDict):
        
        def backtrack(remaining):
            if remaining == "":
                return True
            
            for word in wordDict:
                if remaining.startswith(word) :
                    if backtrack(remaining[len(word):]) :
                        return True

            return False

        print(backtrack(s))

if __name__ == "__main__":
    wordDict = ["apple"]
    s = "applepineapple"

    solver = Solution()
    solver.wordBreak(s, wordDict)