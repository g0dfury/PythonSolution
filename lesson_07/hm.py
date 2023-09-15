### Problem A Easy
# z = int(input("1 число: "))
# x = int(input("2 число: "))
# for i in range (z, x+1):
#     print (i, end=" ")


# z = int(input("1 число: "))
# x = int(input("2 число: "))
# for i in range (z, x-1, -1):
#     print (i, end=" ")

### Problem B Easy ///// with if:
# num1 = int(input("1 число: "))
# num2 = int(input("2 чило: "))
# for i in range (num1, num2-1, -1):
#     if i % 2 != 0:
#         print (i, end=" ")

# #### Medium A
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# check = False
# for i in range (a, b+1):
#     if i % d == c:
#         print (i, end=" ")
#         check = True

# if check == False:
#     print ("Таких чисел нет!")

# # Medium B
# n = int(input())
# summa = 0
# for i in range (n):
#     number = int(input())
#     summa += number
# print (summa)

# Hard B

### Formula: A*x**3 + B*x**2 + C*X+D=0

###     2   -3  -1  2   0
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for x in range (-100, 101):
    if a * (x**3) + b * (x**2) + c * (x) + d == 0:
        print (x, end=" ")
    check = True

if not check:
    print ("x не найден!")