'''
Given a rectangular matrix and integers a and b, consider the union of the ath row and the bth (both 0-based) column of the matrix (i.e. all cells that belong either to the ath row or to the bth column, or to both). Return sum of all elements of that union.

Example

For

matrix = [[1, 1, 1, 1],
          [2, 2, 2, 2],
          [3, 3, 3, 3]]
a = 1, and b = 3, the output should be
crossingSum(matrix, a, b) = 12.

Here (2 + 2 + 2 + 2) + (1 + 3) = 12.
'''

#matrix = [[1, 1, 1, 1],
#          [2, 2, 2, 2],
#          [3, 3, 3, 3]]

m = [[100]]
def vs(m, a,b):
    s = 0
    for i in range (0, len(m)):
        if i == a:
            for k in range(0, len(m[i])):
                s += m[i][k]
            continue
        for j in range(0, len(m[i])):
            if j == b:
                s += m[i][j]
    return s

print(vs(m, 0,0))
