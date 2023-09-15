# ###### lesson 6 ####
# from random import randint
# # Problem A
# print("Угадай число!")
# print("Загаданное число находится между 1 и 100.")
# print("У вас есть неограниченное количество попыток")
# print("Игра начинается...\n")

# x = randint(1, 100)

# attemts = 0
# while True:
#     answer = int(input("Введите число: "))
#     attemts += 1
#     if x == answer:
#         print ("Вы угадали!")
#         break
#     else:
#         print("Пробуйте еще!")
#         # if attemts >= 50: 
#         #     print ("Ваше число" + x < 50 )
# print ("Количество попыток: " + str(attemts))
         

 
# Problem B
# print ("Камень - ножницы - бумага !")
# print ("Вы будете играть против компьютера, игра джо трех побед")
# print ("Компьютер уже сделал свой выбор !")
# print ("Ваша очередь...")

# print ("1---Камень\n2---Ножницы\n3---Бумага")

# counter_python = 0
# counter_human = 0

# while True:
#     x = int(input("Сделайте свой выбор: ")) #ваш выбор
#     y = randint(1, 3) #выбор питона
    
#     if x == 1:
#         print ("Ваш выбор: камень")
#     elif x == 2:
#         print ("Ваш выбор: ножницы")
#     else:
#         print ("Ваш выбор: бумага")
#     if y == 1:
#         print ("Выбор питона: камень")
#     elif y == 2:
#         print ("Выбор питона: ножнницы")
#     else:
#         print ("Выбор питона бумага")
    
    
    
#     if x == y:
#         print ("У вас ничья!")
#     elif (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
#         counter_python += 1
#     else:
#         counter_human += 1
#     print ("Счет компьютера: " + str(counter_python) + ", Ваш счет: " + str(counter_human))
#     if counter_python == 3 or counter_human == 3:
#         break
        

# # Problem C
from random import randint

# print ("Шарик с предсказаниями!\nКаждый раз шарик будет выдавать вам случайное предсказание.\nА так же вы можете задать любой вопрос и получить ответ.")
# print ("Доступные режимы: ")
# print ("1) Предсказание.")
# print ("2) Задайте вопрос на который можно ответить либо да, либо нет.")
# proda = "Да"
# end = "Нет"
# z = randint(1, 3)
# y = randint (1, 2)
# while proda == "Да":
    
#     x = int(input("Выберите режим: "))
#     if x == 1:
#         print (z)
#     elif x == 2:
#         print (y)
#     if z == 1:
#         print ("good day")
#     elif z == 2:
#         print ("bad day")
#     else:
#         print ("today as usual")
#     if y == 1:
#         print ("Да")
#     elif y == 2:
#         print ("Нет")
#     proda = input("Введите 'Да', чтобы продолжить. ") 
#     end = input ("Введите 'Нет', чтобы завершить сенанс. ")

    # Problem C






# #  Problem D
# print ("Консольный калькулятор.")
# print ("Здесь вы можете применять простые математические операции.")

# further = "y"
# while further == "y":
#     a = float(input("Введите первое число: "))
#     operation = input("Введите операцию: ")
#     print ("+, -, /, *")
#     b = float(input("Введите второе число: "))
#     if operation == "+":
#         print (a+b)
#     elif operation == "/" and b == 0:
#         print ("На ноль делить нельзя! ")
#     elif operation == "-":
#         print (a-b)
#     elif operation == "*":
#         print (a*b)
#     elif operation == "/":
#         print (a/b)
#     further = input("Введите 'y', чтобы продолжить: ")


# Problem C

print ("Шарик с предсказаниями!\nКаждый раз шарик будет выдавать вам случайное предсказание.\nА так же вы можете задать любой вопрос и получить ответ.")
print ("Доступные режимы: ")
print ("1) Предсказание.")
print ("2) Задайте вопрос на который можно ответить либо да, либо нет.")

while True:
    choice = int(input("Выберите режим: "))

    if choice == 1:
        x = randint (1,3)
        if x == 1:
            print ("хороший день")
        elif x == 2:
            print ("плохой день")
        else: 
            print ("обычный день")
    elif choice == 2:
        input ("Задайте вопрос: ")
        x = randint (1,2)
        if x == 1:
            print ("Да")
        elif x == 2:
            print ("Нет")
        print ()
        ans = input ("Хотите продолжить ? (y/n): ")
        if ans == "n" or ans == "N":
            print ("Good bye")
            break