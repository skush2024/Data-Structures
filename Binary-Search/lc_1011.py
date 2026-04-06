"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. 
Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
"""

class Solution:

    def __init__(self):
        pass

    def daysToShip(self, weights, capacity):
        days = 1
        ship = 0

        for weight in weights :
            if ship + weight > capacity :
                days += 1
                ship = weight
            
            else :
                ship += weight
        
        return days
            
    
    
    
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)

        while low < high:
            capacity = int((low + high) / 2)
            shipDays = self.daysToShip(weights, capacity)

            if shipDays <= days :
                high = capacity
            
            else :
                low = capacity + 1

        return low
        
        
if __name__ == "__main__":
    solver = Solution()

    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5

    print(solver.shipWithinDays(weights,days))