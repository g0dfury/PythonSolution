# x = "Привет всем"
# print (type(x))

# функция type для определения типа информации


#### УСЛОВНЫЕ ОПЕРАТОРЫ:
#  == [РАВНО]
#  ! [НЕРАВНО]
#  > [БОЛЬШЕ]
#  < [МЕНЬШЕ]
#  >= [БОЛЬШЕ ИЛИ РАВНО]
#  <= [МЕНЬШЕ ИЛИ РАВНО]


######### ВСЕ 6 ОПЕРАТОРОГВ ДАЮТ ОТВЕТ ЧЕРЕЗ TRUE OR FALSE

# result = 5 > 5
# print (result)
# result = 10 != 5
# print (result)

# final = 10!= 10
# print (final)

# result = "Decode" > "almaty"
# print (result)

# result = "D" == "d"
# print (result)

############## ord ()    and      chr ()

# print (ord("Q")) # символ -> код
# print (chr(122)) # код -> символ

#### логический оператор
## not   -  для перевода True в False или наооборот
## in -  чтобы узнать есть ли целое слово или буква в каком-то слове
## and       - чтобы узнать оба ли значения верны (true) или неверны (false)
## or     - чтобы узнать верно ли одно из решений (true) или ни одного верного (false)


#  elif = else + if      (альтернативное условие, если не сработает главное условие сработает elif)
# print (not 0 == 0)


# print ("c" in "Cat") #False 
# print ("c" not in "Cat")    #True

# num = 1
# print (num > 0 and num > 0.5) - #true 
# num = 420
# print (num == 420 or "N" in "Chess") - true


# age = int(input("Введите свой возраст: "))
# if age >= 21 :
#     print ("You are welcome")
# elif age >= 18:
#     print ("You may come in, but do not drink")
# else: 
#     print ("Go home")


# if > elif and else

#Part A

# name = (input("Insert your name: "))
# if name == "Bond" :
#     print ("You are Welcome, Mr Bond")
# else :
#     print ("You are Welcome to the bort")

# # Part B


# number = int(input("Insert any number: "))
# if number % 2 == 0:
#  print ("it is an even number")
# else:
#     print ("It is an odd number")


#     # PROBLEM C
# # input 0 -5    output 0
# num1 = float(input("Выведите первое число"))
# num2 = float(input("Выведите второе число: "))
# if num2 > num1:
#     print (num2)
# else:
#     print (num1)



## MEDIUM A ###

num = float(input("Insert any nubmer: "))
if num >= 100 and num <= 999 :
    print ("good")
else:
    print ("not bad") 
    