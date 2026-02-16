"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

def solution (numRows:int):
    output = [[1]]
    last_row = 0
    current_row = last_row + 1

    if numRows == 1 :
        return output
    
    else :
        while(current_row < numRows):    
            row = []
            for i in range(current_row + 1):
                if i == 0 or i == current_row :
                    row.append(1)

                else :
                    row.append(output[last_row][i - 1] + output[last_row][i])                    
            
            output.append(row)
            last_row = current_row
            current_row += 1

        return output





if __name__ == "__main__":
    n = 6
    print(solution(n))


