""""
Given an array nums of size n, which denotes the positions of stalls, 
and an integer k, which denotes the number of aggressive cows, 

assign stalls to k cows such that the minimum distance between any two cows is the maximum possible. 
Find the maximum possible minimum distance.
"""

class Solution:

    def __init__(self):
        pass

    
    def canPlaceCow(self, stalls, dist, k):
        cows = 1
        last_placed = stalls[0]

        for i in range(1, len(stalls)):
            if cows == k :
                return True

            if stalls[i] - last_placed >= dist :
                cows += 1
                last_placed = stalls[i]

        return cows >= k

    
    
    
    def findMinDistance(self, stalls, k):
        stalls.sort()

        low = 1
        high = stalls[-1] - stalls[0]
        ans = -1

        while low <= high : 
            distance_to_maintain = int((low + high) / 2) 

            if self.canPlaceCow(stalls, distance_to_maintain, k) :
                ans = distance_to_maintain
                low = distance_to_maintain + 1
            
            else :
                high = distance_to_maintain - 1
        
        return ans
    
    def aggresiveCows(self, stalls,k):
        stalls.sort()
        result = []

        def backtrack(cows_placed=0, position=[], start = 0):
            if cows_placed == k :
                result.append(position.copy())
                return

            for i in range(start, len(stalls)):
                position.append(stalls[i])
                backtrack(cows_placed + 1, position, i + 1)
                position.pop()
            
        backtrack()
        return(result)

        




if __name__ == "__main__":
    solver = Solution()

    nums = [1,2,3,4,5,6]
    k = 3

    # print(solver.findMinDistance(nums, k))
    print(solver.aggresiveCows(nums,k))