"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.

Time Complexity O(m*n)
"""

def zeroMatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    row, col = set(), set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)

    for i in range(m):
        for j in range(n):
            if i in row or j in col:
                matrix[i][j] = 0
    return matrix

