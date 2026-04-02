"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

"""

def factorial(n):
    if n <= 1 :
        return 1
    
    return n * factorial(n - 1)

class Solution:

    def __init__(self):
        pass

    def getPermutation(self, n, k):
        
        numbers = list(range(1, n + 1))
        k -= 1
        result = []  

        for i in range(n,0,-1):
            fact = factorial(i - 1)
            index = k // fact

            result.append(numbers[index])
            numbers.pop(index)

            k %= fact

        print(result)            


        
        

        # def backtrack1(idx, string=[]):
        #     if idx == n:
        #         result.append("".join(string.copy()))
        #         return

        #     for i in range(n):
        #         if str(i + 1) in string:
        #             continue

        #         string.append(str(i + 1))
        #         backtrack(idx + 1, string)
        #         string.pop()

        # backtrack1(0)
        # return result[k - 1]

if __name__ == "__main__":
    solver = Solution()
    # print(solver.getPermutation(3,2))

    n = 3
    k = 2
    solver.getPermutation(n,k)