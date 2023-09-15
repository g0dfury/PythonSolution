######## рекурсия

# def abc():
#     print('Decode', end=" ")

#     abc()
# abc()

# i - опциональный (необязательный) параметр, должен стоять после дефолтного параметра
# def one_to_number(num: int, i=1) -> None:
#     # print(i, end=' ')
#     print(f"num = {num}, i = {i}")

#     if i == num:  # базовый случай
#         return
#     else:  # рекурсивный случай
#         one_to_number(num, i+1)

# one_to_number(10)



# числа Фибоначи ( сумма последующего и предыдущего элемента начиная с 0 и 1)
# 0 1 1 2 3 5 8 13 21 34 55 89 ...

# n = 10          # не оптимизированная, лучшая версия находится в папке functions
# def fibonacci(n: int) -> int:
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-2) + fibonacci(n-1)

# print(fibonacci(10))




# easy a
# def recursion():
#     print("This is recursion")
#     recursion()

# recursion() # вызов функции


# easy b
# n = int(input())
# for numbers in range(1, n+1):
#     print(numbers, end=' ')


# def print_numbers(n: int) -> int:
#     if n == 0:
#         return 0
#     else:
#         print_numbers(n-1)
#         print(n, end=' ')

# print_numbers(12)


# easy c
# def factorial(n: int):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))


# easy d
def ackerman(m, n):
    if m == 0:
        return n +1
    elif m > 0 and n == 0:
        return ackerman(m-1, 1)
    else:
        return ackerman(m-1, ackerman(m, n -1))

