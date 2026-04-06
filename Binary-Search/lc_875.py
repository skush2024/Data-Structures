"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

class Solution:

    def __init__(self):
        pass

    
    def timeTaken(self, piles, speed):
        time = 0
        for bananas in piles :
            if bananas % speed == 0 :
                time += bananas // speed
            
            else :
                time += (bananas // speed) + 1

        return time
    
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)+ 1

        ans = -1

        while low <= high :
            speed = int((low + high)/2)
            time = self.timeTaken(piles, speed)

            if time <= h :
                ans = speed
                high = speed - 1
            
            else :
                low = speed + 1

        
        print(ans)

if __name__ == "__main__":
    piles = [30,11,23,4,20]
    h = 6

    solver = Solution()
    solver.minEatingSpeed(piles, h)