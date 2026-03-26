"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

class Solution:

    def __init__(self):
        pass


    def combinationSum(self, candidates, target) :
        result = []
        count_map = {candidate : target // candidate for candidate in candidates}


        def explore(selections, idx):
            if sum(selections) >= target :
                if sum(selections) == target:
                    result.append(selections.copy())
                return

            for i in range(idx, len(candidates)):
                for multiples in range(1, count_map[candidates[i]] + 1):
                    for j in range(multiples):
                        selections.append(candidates[i])
                    
                    explore(selections, idx + 1)
                    
                    for j in range(multiples):
                        selections.pop()
        

        def backtrack(start, remain, selections):
            if remain == 0 :
                result.append(selections.copy())
                return
            
            if remain < 0 :
                return
            
            for i in range(start, len(candidates)):
                selections.append(candidates[i])
                backtrack(i, remain - candidates[i], selections)
                selections.pop()


        # explore([],0)
        backtrack(0,target,[])

        return result




if __name__ == "__main__":
    solver = Solution()
    candidates = [2,3,5]
    target = 8

    print(solver.combinationSum(candidates,target))