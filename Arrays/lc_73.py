"""

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

def solution(matrix):
    rows = set()
    cols = set()   

    for row in range(len(matrix)):
        if 0 in matrix[row] :
            rows.add(row)

    for row in rows:
        record = matrix[row]
        for col in range(len(record)):
            if record[col] == 0 :
                cols.add(col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row in rows:
                matrix[row] = [0] * len(matrix[row])
                break
            if col in cols: 
                matrix[row][col] = 0

if __name__ == "__main__":
    input_matrix = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]        
    ]


    solution(input_matrix)

    print(input_matrix)
