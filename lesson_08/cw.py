# ######## Вложенные циклы #####
# for i in range (3):
#     for j in range (5):
#         print ("i:",i, " j:", j)

# Problem A
# num = 100
# for i in range (1,num):
#     print (i, 100-i, sep="---")

# # Problem A
# for i in range(1, 100):
#     print (i, j, sep="---")
#     j -= 1

# # Problem B
# num = 1
# n = int(input())
# for i in range (1, n+1):
#     num *= i
# print (num)


n = int(input("N лестниц: "))
for i in range (n+1):
    print ("*"*i)
    