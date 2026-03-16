"""
Given the arrival and departure times of all trains reaching a particular railway station, determine the minimum number of platforms required so that no train is kept waiting. Consider all trains arrive and depart on the same day.

In any particular instance, the same platform cannot be used for both the departure of one train and the arrival of another train, necessitating the use of different platforms in such cases.

Note: Time intervals are in the 24-hour format (HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this will be <= 59 and >= 0). Leading zeros for hours less than 10 are optional (e.g., 0900 is the same as 900).
"""

class Solution:

    def __init__(self):
        pass

    
    def findPlatform(self, Arrival, Departure):
        
        last_departed = -1
        platforms = 0 
        count = 0


        for i in range(len(Arrival)):
            if int(Arrival[i]) <= last_departed:
                count += 1
                
            else :
                print("New Slot !!!")
                platforms = max(count, platforms)
                count = 1
            
            last_departed = max(last_departed, int(Departure[i]))


        return max(platforms, count)


if __name__ == "__main__" :
    Arrival = ["0900", "0940", "0950", "1100", "1500", "1800"]
    Departed = ["0910", "1200", "1120", "1130", "1900", "2000"]

    solver = Solution()
    print(solver.findPlatform(Arrival, Departed))