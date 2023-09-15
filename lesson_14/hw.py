# easy 

# n, m = map(int, input().split())
# matrix = []
# for i in range (n):
#     x = list(map(int, input().split()))
#     matrix.append(x)

# max_el = matrix[0][0]
# i_max, j_max = 0, 0

# for i in range (len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] < max_el:
#             matrix_el == matrix[i][j]
#             i_max = i
#             j_max = j

# print(i_max, j_max)

#medium 

# n, m = map(int, input().split())
# matrix = []
# for i in range (n):
#     x = list(map(int, input(),split()))
#     matrix.append(x)

# for row in matrix[::-1]:
#     print(*row[::-1])

#hard 
n = int(input("Size: "))
matrix = [["."] * n for i in range(n)]

for i in range(n):
    matrix[i][i] = "*"
    matrix[n//2][i] = "*"
    matrix[i][n//2] = "*"
    matrix[i][n-i-1] = "*"

for row in matrix:
    print(*row)