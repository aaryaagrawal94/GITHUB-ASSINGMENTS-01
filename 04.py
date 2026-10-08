#ASSIGMENT_04
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

new = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        new[i][j] = matrix1[i][j] + matrix2[i][j]

print("Addition of two matrices:")
for row in new:
    print(row)
