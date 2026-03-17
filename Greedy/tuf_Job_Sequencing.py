"""
Given an 2D array Jobs of size Nx3, 
where 
    Jobs[i][0] represents JobID , 
    Jobs[i][1] represents Deadline , 
    Jobs[i][2] represents Profit associated with that job. 

Each Job takes 1 unit of time to complete and only one job can be scheduled at a time.

The profit associated with a job is earned only if it is completed by its deadline. Find the number of jobs and maximum profit.
"""

class Solution:

    def __init__(self):
        pass

    def JobScheduling(self, Jobs):
        jobs = sorted(Jobs, key= lambda x: x[2], reverse=True)
        time = sorted(Jobs, key= lambda x: x[1], reverse=True)
        
        max_waiting_time = time[0][1]
        slots = [0 for i in range(max_waiting_time)]
        
        profit = 0
   
        for job in jobs:
            can_wait = job[1]
            
            if slots[can_wait - 1] == 1 :
                to_be_placed = can_wait - 2
                
                while to_be_placed >= 0 :
                    if slots[to_be_placed] == 0 :
                        slots[to_be_placed] = 1
                        profit += job[2]
                        break
                    
                    else :
                        to_be_placed -= 1

            else :
                profit += job[2]
                slots[can_wait - 1] = 1
            



if __name__ == "__main__" :
    solver = Solution()

    jobs = [ [1,4,20], [2,1,10], [3,1,40], [4,1,30] ]
    solver.JobScheduling(jobs)