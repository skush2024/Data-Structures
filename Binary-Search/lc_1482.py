"""
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
"""

class Solution:

    def __init__(self):
        pass

    def nBouqets(self, bloomDay, k, waiting):
        bouqets = 0
        adjacent_flowers = 0

        for i in range(len(bloomDay)):
            if bloomDay[i] <= waiting:
                adjacent_flowers += 1
                if adjacent_flowers == k :
                    bouqets += 1
                    adjacent_flowers = 0
            else :
                adjacent_flowers = 0
        
        return bouqets

    
    
    
    def minDays(self, bloomDay, m,k):
        if (m * k) > len(bloomDay):
            return -1
        
        low = 1
        high = max(bloomDay)
        
        ans = -1 

        while(low <= high):
            waiting = int((low + high) / 2)
            bouqets = self.nBouqets(bloomDay, k, waiting)

            if bouqets >= m :
                ans = waiting
                high = waiting - 1
            
            else :
                low = waiting + 1

        return ans

if __name__ == "__main__":
    solver = Solution()

    bloomDay = [7,7,7,7,12,7,7]
    m = 2
    k = 3

    print(solver.minDays(bloomDay,m,k))