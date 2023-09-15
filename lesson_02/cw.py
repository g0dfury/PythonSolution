#  ТИПЫ ДАННЫХ
# str    [string - строка] "Hello" or 'Hello'
# int    [integer - целое число] 231 -22 0 1
# float  [число с дробью]    21.1    -0.2    1.34
# bool   [boolean - логический тип с 2 вариантами]   True False      Yes No     

### КОНВЕРТАЦИЯ 
# print (int('2018') % 4) - НЕ ВИСОКОСНЫЙ ГОД, мы конвертировали строку в целое число
# print (int("2016") % 4) - ВИСОКОСНЫЙ ГОД
# print (int(1.314)) - дает только одни, потому что ИНТ - целое число

# print (int(True)) True - 1
# print (int(False)) False - 0
# print (float("12.4")) - перевод строки "12.4" в дробнрое число

# print (float(True))

# 0 - its False
#  "" - its False
#  все остальное True
# 
#print (bool(0)) FALSE
#print (bool(1)) TRUE
# print (bool(-643643)) TRUE
# print (bool(" ")) - TRUE потому что строка не пусткая
# print (bool("")) - FALSE потому что нет пробела между кавычками 


### ПЕРЕМЕННАЯ 
# name = "Emir"
# print ("My name is" + " " + name) My name is Emir
# age = "19"
# print ("I am " + age + " " + "years old") I am 19 years old

### ПРАВИЛА ДЛЯ ПЕРЕМЕННЫХ 
# 1) называть переменные понятно, чтоб знать что в себе хранится переменная
# 2) использовать латинские буквы(маленькие), цифры и нижний пробле (_)
# 3) нельзя использовать пробел
# 4) нельзя ставить цифру в начало переменной
# 5) переменная действует до момента создания новой переменной
# 6) переменная работает только без ковычек

# name1 = 'Emir'
# name2 = "Zhenya"
# name3 = "Gula"
# name1 = "Эмир" - пример того как работает 5 правило 
# print ("My name is " + name1)
# print ("My friends name is " + name2)
# print ("Although my name is " + name1 + " " + "socium always call me as a " + name3)

# year = 2023
# print ("Happy new " + year + "year") - строки с числами НЕ СОЕДИНЯЮТСЯ (БУДЕТ ЕРРОР)
# print ("Happy new " + str(year) + ' '+ "year") - конвертация происходит только на одну строчку



# любой input является строкой
# name = input () - для приема информации
# print ("Вас зовут: " + name1)

age = input()
print ("Через 5 лет вам будет: ", + int(age)+5)
