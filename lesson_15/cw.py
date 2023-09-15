#####    function ()    .
# 1 придумывать оригинальное понятное название:
# 2 принимается столько информации сколько запрашивается в 4 строке, ни больше не меньше

# def greeting_user(name, surname):
#     print(f"Hello {name, surname}!")
# username = input('Print your name: ')
# usersurname = input('Print your surname: ')
# greeting_user(username, usersurname)


### return 
# 1 Данные возвращаются туда, где функция была вызвана
# 2 Завершает функцию

# def sqrt(number: int|float) -> float:
#     result = number ** 0.5
#     return result  #заваершается (аналог break.)
    
        
# x = int(input('Squared number: '))
# squared_number = sqrt(x) #от сюда мы возвращаем значение переменной, и принимаем его снова же
# print(squared_number)


# def is_adult(age):
#     if age < 0:
#         return   # завершил функцию


# def my_max(*numbers):
#     max_el = numbers[0]
#     for el in numbers:
#         if el > max_el:
#             max_el = el
    
#     return max_el

# print(my_max(1,2,3,4,5,6,7,8,9,10))



# age = 10
# def my_function():
#     global age # дает право полностью менять переменную
#     age += 1 # error функция не может менять глобальные перемены, нужно прописать global
#     x = 5   # эта переменная локальна только для моей функции


# #   Аннтоация типов

# def sum_of_digits(num: int) -> int:   #def sum_of_digits(num: int|float):
#     res = 0
#     while num > 0:
#         res += num % 10
#         num //= 10

#     return res

# print(sum_of_digits(456))


# def is_prime(number:int) -> bool:     # функция проверябщая простое ли число
#     if number < 2:
#         return False
#     counter = 0
#     for i in range(1, number + 1):
#         if  number // i == 0:
#             counter += 1
#     if counter > 2:
#         return False

#     return True

# ls = [10, 32, 24, 99, 51, 65, 2, 44]
# for i in ls:
#     if is_prime(i) == True:
#         print(i, end=" ")


# ls_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(sorted(ls_1))
# print(sorted(ls_1, key=sum_of_digits))




# # easy a
# def Whatsapp():
#     print('Hi there, Im using WhatsApp')  
# Whatsapp()

# #easy b
# def show_age(age: int) -> int:
#     print(f'I am {age} years old.')
# age = int(input('Enter your age here: '))
# show_age(age)

# #easy c
# def check(number: int) -> int:
#     if number % 2 == 0:
#         print('even')
#     else:
#         print('odd')

# n = int(input('any number: '))
# check(n)

# # # easy d
# def sum_of_integers(numbers:int) -> int:
#     result = 0
#     for i in range(1, n+1):
#         result += i
#     print(f'Sum from 1 to {n} is eqaul to {result}')
#     return result

# n=int(input())
# summa = sum_of_integers(n)
# sum_of_integers(summa)

# # medium a
def have_digit(word: str) -> bool:
    for symbols in word:
        if symbols.isdigit():
            return True
    return False


word = 'decode'
if have_digit(word):
    print('cool')
else:
    print('hot')

# # medium b'
# def is_prime(number:int) -> bool:     # функция проверябщая простое ли число
#     if number < 2:
#         return False
#     counter = 0
#     for i in range(1, number + 1):
#         if  number // i == 0:
#             counter += 1
#     if counter > 2:
#         return False

#     return True

# # medium c
# def sum_of_digits(num: int) -> int|float:
#     counter = 0
#     while num > 0:
#         counter += num % 10
#         num //=10
#     return counter

# print(sum_of_digits(123))


# # hard a
# def sort_even_odd(numbers: int):
#     even = []
#     odd = []
#     for i in numbers:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return sorted(even) + sorted(odd)

# my_list = list(map(int, input().split()))
# print(*sort_even_odd(my_list))

# hard c
def onlydigit(text: str) -> bool:
        if text.isnumeric() == True:  # если все цифры
            return('very good')
        if text.isalpha() == True:  # если и цифры и числа
            return('so bad')
        if text.isalnum() == True:
            return ('not bad')


text = input()
print(onlydigit(text))



