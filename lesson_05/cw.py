######## CICLE WHILE
# a + 1   ----  a+=1
# a * 2 ---- a*=2  

# age = 24
# age += 2
# print (age)

# age = float(input("Введите свой возраст: "))
# while age < 21:
#     print ("Вам сюда нельзя!")
#     age += 1
# print (age)

### Оператор break ###

# i = 1
# while i < 7:
#     print (i, "zxc")
#     if i == 5:
#         break  #досрочная остановка цикла
#     i += 1

### Операторт continue ###


# i = 10
# while i > 0:
#     i -=1
#     if i % 2 !=0: #если чесло не делится без остатка на два (нечетное)
#         continue
#     print (i)


##### Бесконечный цикл #####
# i=5
# while 5 < 10:
#     print ("zxczxczxczxc")

# while True:
#     number = int(input("Введите число: "))
#     if number == 0:
#         break

# from random import randint

# print("Угадай число!")
# print("Загаданное число находится между 1 и 6.")
# print("У вас есть 3 попытки")
# print("Игра начинается...\n")

# x = randint(1, 6)
# i = 0
# while i < 3:
#     answer = int(input("Попытка #" + str(i+1) + ": "))
#     if answer == x:
#         print ("Вы угадали!")
#         break
#     else: 
#         print ("Вы не угадали. Оставшееся количество попыток:", 3 - i - 1)
#     i += 1



# Задача А easy
# n = int(input("Количество повторений: "))
# i = 0
# while i < n:
#     print ("zxc")
#     i += 1

# Задача B
n = int(input("Введите число: "))
summa = 0
i = 1
while i<=n:
    summa +=i
    i += 1
print (summa)

    


