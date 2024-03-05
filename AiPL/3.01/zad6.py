matrix = [[1,2,3],[3,1,5], [2,2,2]]

for i in range(3):
    for j in range(i):
        matrix[i][j] = 0


print(matrix)