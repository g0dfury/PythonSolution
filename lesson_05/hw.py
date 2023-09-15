# # #Problem A easy#
# n = int(input("Введите число у которого вы хотите найти наименьший делитель: "))
# i = 2
# while n % i != 0:
#     i+=1
# print (i)

# Problem B easy#
# count = 0
# c = int(input())
# count += c
# while c != 0:
#     c = int(input())
#     count += c

# print(count)

# Problem B medium
c = int(input(" "))
count = 0
while c != 0:
    c = int(input(" "))
    if c % 2 == 0:
        count += 1

print(count)



# Medium A
# x = int(input("x="))
# y = int(input("y="))
# # day = 1
# while x < y:
#     x *= 1.2
#     day += 1
# print(day)
