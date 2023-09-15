# # ## Problem A ###

from random import randint

# # print("Угадай число!")
# # print("Загаданное число находится между 1 и 6.")
# # print("У вас есть 3 попытки")
# # print("Игра начинается...\n")

# # x = randint(1, 6)
# # answer = int(input("Попытка #1. Введите число: "))

# # if answer == x:
# #     print("Вы угадали!")
# # else:
# #     print("Вы не угадали, но у вас есть еще 2 попытки\n")
# #     answer = int(input("Попытка #2. Введите число: "))

# #     if answer == x:
# #         print("Вы угадали!")
# #     else:
# #         print("Вы не угадали, у вас есть последений шанс!\n")
# #         answer = int(input("Попытка #3. Введите число: "))

# #         if answer == x:
# #             print("Вы угадали!")
# #         else:
# #             print("Вы проиграли!")
# #             print("Загаданное число:", x)



# ### Problem B ###

# print ("Камень - ножницы - бумага !")
# print ("Вы будете играть против компьютера")
# print ("Компьютер уже сделал свой выбор !")
# print ("Ваша очередь...")

# print ("1---Камень\n2---Ножницы\n3---Бумага")
# x = int(input("Сделайте свой выбор: "))
# y = randint(1, 3)
# if y == 1:
#     print("Выбор компьютера: Камень")
# elif y == 2:
#     print("Выбор компьютера: Ножницы")
# else:
#     print("Выбор компьютера: Бумага")

# if x == 1:
#     print("Ваш выбор: Камень")
# elif x == 2:
#     print("Ваш выбор: Ножницы")
# else:
#     print("Ваш выбор: Бумага")

# if x == y:
#     print ("У вас ничья!")
# elif (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
#     print ("Вы проиграли")
# else:
#     print ("Вы победили!")


## Problem C ####

# print ("Определение абонента номера телефона.")
# print ("Программа определит абонент на территории Казахстана.")

# print ("Введите номер в числовом формате! ")
# x = int(input("Введите здесь свой номер: "))
# print (x)
# num1 = int(727)
# if num1 in x:
#     print ("Ваш абонент: Activ")
# elif 700 in x or 708 in x:
#     print ("Ваш абонент: Altel4g")
# elif 705 in x or 771 in x or 776 in x or 777 in x:
#     print ("Ваш абонент: Beeline")
# elif 701 in x or 702 in x or 775 in x or 778 in x:
#     print ("Ваш абонент: Kcell")
# else:
#     print ("Ваш абонент: Tele2")


#     ### Problem D ###
print ("Консольный калькулятор.")
print ("Здесь вы можете применять простые математические операции.")
print("Для завершения программы пропишите 'stop'.")
print()

while True:
    a = float(input("Введите первое число: "))
    print ("+, -, *, /, **, //, %")
    x = (input("Введите операцию: "))
    b = float(input("Введите второе число: "))
    if a == 'stop' or b == 'stop' or x == 'stop':
        break
    if x == "+":
        print (a+b)
    elif (x == "/" or x == "//" or x == "%") and b == 0: # elif (x in "//%") and x == 0:
        print ("На ноль делить нельзя!") 
    elif x == "-":
        print (a-b)
    elif x == "*":
        print (a*b)
    elif x == "/":
        print (a/b)
    elif x == "**":
        print (a**b)
    elif x == "//":
        print (a//b)
    elif x == "%":
        print (a%b)



