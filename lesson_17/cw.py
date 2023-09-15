# Try - except

# while True:
#     try:
#         age = int(input('Введите свой возраст: '))
#         break
#     except:
#         print('Ошибка, введите еще раз: ')
# print('Добро пожаловать!')


# while True:
#     try: # помещаем код с возможной ошибкой.
#         a = int(input('age: '))
#     except: # что делать если код сломался
#         print('Введите челое число без букв.')
#     else: # что делать если код успешно сработал.
#         print(f'Ваш возраст: {a}')
#         break
#     finally: # сработает в любом случае
#         print('конец')

# def my_reverse(num: int, res = 0) -> int:
#     if type(num) != int:
#         raise TypeError('Функиця принимает только int.')
    
#     if num == 0:
#         return res
#     else:
#         res = res * 10 + num % 10
#         return my_reverse(num // 10, res)

# number = int(input('Число: '))
# print(my_reverse(number))


# Тернарный оператор

# num = int(input('Number: '))

# #v2.0
# print('even' if num % 2 == 0 else 'odd')

# res = 'positive' if num > 0 else 'neutral or negative'
# print(res)



# class work 
# easy a
# number = int(input('Число: '))
# if number < 0:
#     raise ValueError('Число может быть только положительным')
# else:
#     print(f"Ваше число: {number}")


#easy b
# try:
#     number = int(input('Введите целое число: '))
# except: 
#     print('Can be only integer')
# else:
#     print(f'Your number is {number}')


# #easy c
# name = input('Put your name: ')
# if name[0].islower():
#     raise NameError('Введите свое имя с большой буквы.')
# else:
#     print('Welcome')


# tg exercises:
# Поделите каждый элемент списка на следущий элемент

# my_list = list(map(int, input().split()))
# for el in range(len(my_list) - 1):
#     try:
#         res = my_list[el] / my_list[el+1]
#         print(f'{my_list[el]} / {my_list[el+1]} == {res}')
#     except ZeroDivisionError:
#         print(f'Невозможно вычислить {my_list[el]} / {my_list[el+1]}')


# two_numbers = list(map(int, input().split()))
# try:
#     a, b = two_numbers  # Может сломаться
# except:
#     a = two_numbers[0]
#     b = int(input())
# print(f"{a} + {b} = {a+b}")



# def factorial(number: int) -> int:
#     try:
#         number = int(number)
#     except:
#         raise TypeError('Only integers')
#     res = 1
#     for i in range(1, number + 1):
#         res *= i
#     return res

    
# print(factorial(5))
# print(factorial('5'))
# print(factorial('abc'))
