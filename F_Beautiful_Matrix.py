matrix = []
count =0
for _ in range(5):
    arr = list(map(int, input().split()))
    matrix.append(arr) 
    
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            matrix[i][j], matrix[2][2] = matrix[2][2], matrix[i][j]           
            count += abs(2 - i) + abs(2 - j)

print(count)
