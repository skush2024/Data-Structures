"""
You are given A painters and an array C of N integers where C[i] denotes the length of the ith board. 
Each painter takes B units of time to paint 1 unit of board. 

You must assign boards to painters such that:
Each painter paints only contiguous segments of boards.
No board can be split between painters.

The goal is to minimize the time to paint all boards.

"""

class Solution:

    def __init__(self):
        pass

    
    def checkWorkersRequired(self, work, m:int, max_time):
        workers_required = 1
        time_taken = 0


        for task in work :
            time_to_complete_task = task * m
            if time_taken + time_to_complete_task > max_time :
                workers_required += 1
                time_taken = time_to_complete_task
            else :
                time_taken += time_to_complete_task

        return workers_required




    
    
    def paint(self, work, k:int, m:int):
        '''
        work -> Tasks to be done, requirement.
        k -> Number of workers
        m -> Time taken by each of the worker 

        Goal:
        Allocate continous tasks to k workers such that the total time to complete the work is mininzd.
        '''
        
        # Since it is the bare minimum time to  complete the entire task
        low = max(work) * m
        
        # Total Time to do all work, therefore the answer would be in this range.
        high = sum(work) * m

        while low < high :

            max_time_allowed = int((low + high) / 2)
            nWorkers = self.checkWorkersRequired(work, m, max_time_allowed)
            if nWorkers > k :
                low = max_time_allowed + 1
            
            else :
                high = max_time_allowed
        
        return low 
    
if __name__ == "__main__":
    solver = Solution()

    tasks = [5,10,30,20]
    nWorkers = 3
    cost = 2

    print(solver.paint(tasks, nWorkers, cost))