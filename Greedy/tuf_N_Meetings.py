class Solution:

    def __init__(self):
        pass

    def solve(self, start,end):
        schedule = {i : end[i] - start[i] for i in range(len(end))}
        schedule_sorted = sorted(schedule, key= lambda x: schedule[x])
        calendar_start = min(start)
        calendar= [0 for i in range(max(end) - min(start) + 1)] 
        N = 0
        
        for i in schedule_sorted:
            start_time = start[i]
            idx = start_time - calendar_start
            if 1 not in calendar[idx: idx + schedule[i] + 1]:
                N += 1
                for j in range(idx, idx + schedule[i] + 1):
                    calendar[j] = 1

        print(N)

    
    def maxMeetings(self, start, end):
        meetings = [[end[i], start[i], i + 1] for i in range(len(end))]
        meetings.sort()
        

        last_ended = -1
        N = 0 

        for meeting in meetings :
            if meeting[1] > last_ended :
                N += 1
                last_ended = meeting[0]

        return N



if __name__ == "__main__" :
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]
    
    solver = Solution()
    print(solver.maxMeetings(start,end))