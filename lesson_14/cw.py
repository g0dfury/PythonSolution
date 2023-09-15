# двумерные массивы

    #столбец/колонна
# numbers = [
#     [1, 2, 3, 4],   #линия/дорожка
#     [4, 5, 6, 7],
#     [8, 9, 10, 11]
# ]

# print(len(numbers)) #  3
# print(numbers[-1]) #  4
# print(numbers[1][-1]) #  7

######## итерация

# for el in numbers:
#     print(el)

# [1, 2, 3, 4]
# [4, 5, 6, 7]
# [8, 9, 10, 11]

# variant 1
# for row in numbers:  #обращение к массивам
#     for el in row:  #обращение к элементам массивов
#         print(el)
# variant 2
# for i in range(len(numbers)): # i = 0 --> 2
#     for j in range(len(numbers[i])):  # j = 0 --> 3
#         print(i,j,sep=" ")
############ самый короткий print

# for row in numbers:
#     print(*row)

####### сумма
# print(sum(numbers))           error

# summa = 0
# for row in numbers:
#     summa += sum(row)
# print(summa)




#### генерация

# n = [[0] * 3] * 3
# n = [[0] * 3 for i in range(3)]
# n[1][1] = 9
# for row in n:
#     print(*row)

# ########### input()
# n, m = map(int, input().split())  # 2 числа в одном инпуте
# numbers = []
# for i in range(n):
#     x = list(map(int, input().split()))
#     numbers.append(x)
# print(numbers)


#пример 1   
# n = int(input("Matrix size: "))
# matrix = [["0"] * n for i in range(n)]        # генерация матрицы n x n (3 x 3)

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i == j:
#             matrix[i][j] = 1
#         elif i > j:
#             matrix[i][j] = 2
# for row in matrix:
#     print(*row)

# пример 2
# n = int(input("Matrix size: "))
# matrix = [["x"] * n for i in range(n)]   

# # for i in range(len(matrix)):   # i - от 0 до 4
# #     for j in range(len(matrix[i])):  # j - от 0 до 4
# #             matrix[i][j] = i * j

# for row in matrix:
#     print(*row)


