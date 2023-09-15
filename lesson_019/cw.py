# Regular Expressions (Регулярные выражения)
import re # подключение библиотеки ReGex

# print(bool(re.search('q', 'emir'))) #False
# print(bool(re.search('e', 'emir'))) #True

# ^     -    начало строки
# print(bool(re.search(r'^e', 'emir'))) #True
# print(bool(re.search(r'^m', 'emir'))) #False


# $     -   конец строки
# print(bool(re.search(r'e$', 'emir'))) #False
# print(bool(re.search(r'r$', 'emir'))) #True

# print(bool(re.search(r'^emir$', 'emir'))) #True ( от начала до конца )

# \     -   экранирование / изоляция    ( для использования специального символа в качестве текста )
# price = input()
# print(bool(re.search(r'\$$', price))) #True ( первый $ для поиска, второй $ для обозначения конца строки )


# []    -   набор символов  ( создает из набора символов один символ, и проверяет их )
# text = input()
# print(bool(re.search(r'^[abcdef]', text)))

# text = input()
# print(bool(re.search(r'^[a-zA-Z0-9]', text)))

# [^ ]  -   набор КРОМЕ
# text = input()
# print(bool(re.search(r'[^0-9]$', text)))  # В конце что угодно кроме чисел

# .     -       Любой произвольный символ
# text = input()
# print(bool(re.search(r'^a.....b$', text)))  #в начале 'а', в конце 'б', а между ними ЧТО УГОДНО (5 символов)


# +     -       1 или более
# text = input()
# print(bool(re.search(r'^[a-z0-9_.]+@', text)))

# *     -       0 или более
# text = input()
# print(bool(re.search(r'[a-z_.0-9]*@', text)))  # патерна может и не быть


# ?     - будет или не будет (0 или 1)
# text = input()
# print(bool(re.search(r'^\+?7', text)))      #   для проверки телефона ( плюс в начале может быть и не быть )


# {}    -   конкретное количество
# text = input()
# print(bool(re.search(r'^[0-9]{2,4}[a-z]', text)))   # от двух чисел до четырех и в конце любой текст
# print(bool(re.search(r'^[0-9a-zA-Z._]{8,}')))   # от 8 символов и более ( аналог пароля )    



# |    -    логическое ИЛИ

# text = input()
# print(bool(re.search(r'^7|8', text)))   # в начале или 7 или 8


# ()    -   группировка

# text = 'telegram.me'
# result = (re.search(r'([a-z])+\.([a-z]+)', text))
# print(result.group())







# match -   ищет только в начале
# search -  ищет везде
# compile - комплияция ReGex`ов
# findall - находит все что подходит под наш pattern
# split -   разделяет под наш pattern в список
# sub   -   заменяет символы по pattern


# easy a
# string = input()
# print(bool(re.search(r'\d', string)))

# easy b
# text = input()
# pattern = re.search(r'[a-zA-Z0-9]', text)
# if pattern:
#     print('there is coincidence')
# else:
#     print('ho coincidence')

# easy c
# text = input()
# pattern = re.search(r'[A-Z][a-z]+', text)   # start from A_Z, next any a-z more than one time
# if pattern:
#     print('yeah')
# else:
#     print('nah')


# medium a
# text = input()
# pattern = re.search(r'cool$', text)
# print(bool(pattern))


# # medium b
# text = input()
# pattern = re.search(r'^a.+b$', text)
# if pattern:
#     print('Нашел')
# else:
#     print('Не нашел')


