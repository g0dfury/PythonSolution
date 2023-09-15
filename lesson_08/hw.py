# ##### Easy A ####
# a = int(input("1 число: "))
# b = int(input("2 число: "))
# for i in range (a, b+1):
#     if i == i ** 0.5 * i ** 0.5 or i // i**0.5 == i**0.5 or i % i**0.5 == 0:
#         print (i, end=" ")



# #### Easy B ###
# num = int(input())
# for i in range (1, num+1):
#     if num % i == 0:
#         print (i, end=" ")


# ## Medium A
# N = int(input("Введите количество чисел: "))
# found_zero = False
# for i in range(N):
#     num = int(input("Введите число: "))
#     if num == 0:
#         found_zero = True
#         break
# if found_zero:
#     print("YES")
# else:
#     print("NO")

# ### Medium B
# N = int(input("Количество повторений: "))
# zeros = 0
# positives = 0
# negatives = 0
# for i in range (N):
#     num = int(input("Введите числа: ")) 
#     if num == 0:
#         zeros +=1
#     elif num >= 0:
#         positives +=1
#     else:
#         negatives +=1
# print ("Нулей: ", zeros)
# print ("Положительных: ", positives)
# print ("Негативных: ", negatives)




# ###  Hard A
# x = int(input("Введите число от 1 до 9: "))
# # for i in range(1, x+1):
# #     for j in range(1, i+1):
# #         print(j, end='')
# #     print()

# n = int(input())
# text = ""

# for i in range (1, n+1):
#     text += str(1)
#     print (text)


# ### Hard B
# n = int(input("Кол-во карт: "))
# sumn_cards = 0
# for i in raneg (1, n+1):
#     sumn_cards += 1

# for i in range(n-1):
#     card = int(input())
#     sum_cards -= card

# print("Ответ:", sum_cards)