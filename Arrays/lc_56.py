"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time Taken by {func.__name__}: {end - start}")
        return result 

    return wrapper


class Solution:
    def __init__(self, intervals):
        # make an instance copy and sort by start
        self.intervals = sorted(intervals.copy(), key=lambda x: x[0])

    @timeit
    def solve(self):
        merged = []
        for record in self.intervals:
            if not merged or merged[-1][1] < record[0]:
                merged.append(record.copy())
            else:
                merged[-1][1] = max(merged[-1][1], record[1])
        self.output = merged
        return merged
        
if __name__ == "__main__":
    intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    solver = Solution(intervals)
    print(" ===== Optimized Approach =====")
    print(solver.intervals)
    solver.solve()
    print(solver.output)