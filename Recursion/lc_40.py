"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

class Solution:

    def __init__(self):
        pass

    def combinationSum2(self, candidates,target):
        candidates.sort()
        result = []

        def backtrack(idx, subset=[], remain=target):
            if remain == 0 :
                result.append(subset.copy())
                return
            
            if remain < 0 :
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                subset.append(candidates[i])
                backtrack(i + 1, subset, remain - candidates[i])
                subset.pop()

        backtrack(0)
        return result


if __name__ == "__main__" :
    candidates = [10,1,2,7,6,1,5]
    target = 8

    solver = Solution()
    print(solver.combinationSum2(candidates,target))