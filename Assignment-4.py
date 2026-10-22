A = [[1,2,1],
     [0,2,1]]

B = [[1,1,3],
     [0,2,1]]

result = [[0,0,0,],
          [0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

print(' Sum of Matrices:')
for row in result:
    print(row)