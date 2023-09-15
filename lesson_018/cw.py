#### module 

# # variant a 
# import math  # импортирует сам модуль
# num = math.sqrt(10)
# num2 = math.pi
# num3 = math.sin(num2)

# # variant b
# from math import sqrt, pi, sin

# num = sqrt(10)
# num2 = pi

# # variant c
# from math import * #импортирует сам модуль (не надо писать math)

# num1 = sin(10)
# num = pi

# number = 5.9
# print(ceil(number)) # окргуляет вверх
# print(floor(number)) # округляет вниз
# print(round(number)) # окрглуяет по правилам


#pip list <module name>    # array of modules
#pip install <module name>   # install module
#pip uninstall <module name>    #uninstall module


# import my_module as qwerty  # импортуировали созданную нами библиотеку
# print(qwerty.factorial(5))
# print(qwerty.student['GPA'])


# import sys
# sys.path('..')
# from lesson_15.cw import have_digit
# print(456)




# easy a
from my_module import var as v, student
print(v[0])

# easy b
print(student['name'], student['age'])

# easy c
from random import randint
print(randint(5, 10))

# medium a
# from my_module import my_reverse
# word = input()
# my_reverse(word)

# medium b
from math import sin, sqrt, cos, exp, e
# x = int(input('x: '))
# y = int(input('y: '))
# numerator = (sqrt(sin(x)+pow(y, 3))+sqrt(x+y))
# denominator = 2*x+y
# print(f'{(numerator / denominator):.2f}')

# medium c
numerator = sin(5) + 1.75**2
denominator = 3 * e**cos(7)
print(f'{numerator / denominator:.4f}')

#hard a 