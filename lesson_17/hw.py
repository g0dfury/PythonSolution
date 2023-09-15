# # easy a
# my_dict = {"a":1, "b":2, "c":3}
# key = input('key: ')
# value = my_dict.get(key)
# if value is not None:
#     print('key: ', value)
# else:
#     print('key does not exist')

# # # easy b
# a, b = map(int, input().split())
# print(a if b > a else b)

# # medium a
# numbers = list(map(int, input().split()))
# found = False
# for i in numbers:
#     if i % 3 == 0 and i % 5 == 0:
#         found = True
# if found:
#     print('Присутствует')
# else:
#     print('Не присутствует')

# # # medium b
# a = int(input('Fist factor: '))
# b = int(input('Second factor: '))
# c = int(input('Result: '))
# # found = False
# # if a * b == c:
# #     found = True
# # if found:
# #     print('Correct')
# # else:
# #     print('Incorrect')
    

#     # Второй способ:
# if a * b != c:
#     raise Exception('Incorrect.')
# else:
#     print('Correct')

# # hard a
# try:
#     a = int(input('First variable: '))
#     print('Доступные операции: +    -   *   **  /   //  %')
#     operation = input()
#     b = int(input('Second variable: '))
#     if operation == '+':
#         print(a+b)
#     if operation == '-':
#         print(a-b)
#     if operation == '*':
#         print(a*b)
#     if operation == '**':
#         print(a**b)
#     if operation == '/':
#         print(a/b)
#     if operation == '//':
#         print(a//b)
#     if operation == '%':
#         print(a%b)
# except:
#     raise ZeroDivisionError('На ноль делить нельзя.')


# hard b
# while True:
#     number = input('4-х значное число, или введите "stop" для завершения программы: ')   # принимаю строкой чтоб посчитать длину
#     if number == 'stop':
#         break
#     try:
#         if len(number) == 4 and int(number) % 3 == 0:  #перевожу в int чтоб получить математическую ценность
#             print('Число кратно 3.')
#         else:
#             print('Число некратно 3.')
#     except:
#         raise Exception('Введите 4-х значное число.')


def is_have_three(num):
    while num > 0:
        if (num % 10) == 3:
            return True
        num //= 10
    return False
 
number = int(input())
print(is_have_three(number))