# # # ###### massiv - spisok

# # # #           0        1        2       3         4
# # # names = ["Emir", "Zhenya", "Beka", "Narik", "Alyana"]
# # # #           -5       -4        -3      -2       -1


# # # print (names)
# # # # print (names[5]) - Error
# # # # print (names[-6]) - Error
# # # ### Index ###

# # # print(names[4])
# # # print (names[1])

# # # number = [123 , -2, 9.6, -1.2, "decode"]
# # # print(number[1], number[3]) #в массиве нужно обращаться к числам по одному


# # # #Функция len() - length (длина)
# # # print(len(names))    #длина начинает отсчет с единицы
# # # print(len(number)) 

# # # empty_list = [] #пустой список
# # # print(len(empty_list))


# # # # Операции над списком
# # # # (+), (*)
# # # students = ["emir", "dawa", "inkgar"]
# # # edvisors = ["aika", "firuza <3", "guldana"]
# # # print(len(students + edvisors))

# # # print(students * 3)   #["emir", "dawa", "inkgar","emir", "dawa", "inkgar", "emir", "dawa", "inkgar"]
# # # print(len(students * 3)) # length = 9


# # # ## Генерация списка ###
# ls = [0] * 10
# print(ls)


# # # #Изменение значения элемента###
# names = ["Emir", "Zhenya", "Beka", "Narik", "Alyana"]
# names[0] = "Slava"
# print (names)


# # # ### swap ###
# name = "Garayev"
# surname = "Emir"
# # # x = name
# # # name = surname
# # # surname = x
# # # print ("name: ", name)
# # # print ("surname", surname)

# name, surname = surname, name
# print (name, surname)

# names = ["Emir", "Zhenya", "Beka", "Narik", "Alyana"]
# names[0], names[-1] = names[-1], names[0]
# print (names)

# ######## Срезы ######
# names = ["Emir", "Zhenya", "Beka", "Narik", "Alyana"]
# print(names[0:3:2])   # начало           конец               шаг
# print(names[0::2])
# print(names[:3])
# print(names[::-1])


# # # ### Итерация/Пробежка

# number = [2, 6, -9, 4, 0, -7, -12, 1]    


# counter = 0   #Var 1
# for elem in number:
#     if elem < 0:
#         counter += 1

# print (counter)


# for i in range (0, len(number)):  # Var 2
#     if number [i] < 0:
#         counter += 1

# print (counter)


# #### Функиця split (методы)
 # разделяет STR по пробелам, создает из них список

# text = "Zhenya Beka Narik"
# print (text.split())


##### Функция map() ####       1 - принимает определенный тип данных         2 - итерирует объект (переменную)
### map без листа выводит какую-то хуйню, поэтому перед map всегда используется list

# numbers = [1, 1.23, 123.456, False, "789"]
# print (list(map(int, numbers)))


# # # # ## Как принять с консоли ###
#   numbers = list(map(int, input().split())) (#(!$*&@&*$@))



# ######## методы списка ##################    очистить

### .clear() #####
# x = [1, 2, 3]
# x.clear()
# print (x)

# # # #### .copy() ####               скопировать данные
# basket = ["IPhone", "Bread", "AirPods"]
# history = basket.copy()
# basket.clear()
# print (history)


# ########### .count() ##########     сосчитать количество чего-то
# # numbers = [3, 0, 3, 2, 1, 0, 6, 5, 4, 0, 3]
# # print (numbers.count(0))

# # ###### .index() #########                   узнать индекс элемента
# nums = ["Emir", "Zhenya", "Beka"]
# print (nums[1])
# print (nums.index("Beka"))


# ############ .append()   ###########             Добавить в конец любой тип данных
# # numbers = [1, 2, 3]
# # numbers.append(9)
# # print (numbers)


# # ############## .insert() #############     добавить в любое место любой тип данных
# # names = ["Emir", "Zhenya", "Beka"]
# # names.insert(2, "Narik")
# # print (names)


# # # ####### .extend() #########        добавить к одному массиву другой массив
# girls = ["alyana", "dawa"]
# boys = ["zhenya", "beka", "narik"]
# boys.extend(girls)
# print (boys)


# # ############ .pop() ################     удаляет и позволяет сохранить удаляемый объект
# names = ["Emir", "Zhenya", "Beka"]
# del_element = names.pop(0)

# print (names)
# print ("Удалилось: ", del_element)


######### .remove() ################
names = ["Emir", "Zhenya", "Beka", "Emir", "Emir"]
# names.remove("Emir")
# print (names) #удалит только первого в списке

# while "Emir" in names:        ### удалит всех 
#     names.remove("Emir")
# print (names)

# ####### .sort()  ##############
# names = ["Nurai", "Gulam", "Zhenya", "Beka", "Narik"]
# names.sort()
# print(names)


# ########## .reverse() ###########
# names = ["Emir", "Beka", "Zhenya", "Alyana"]
# names.reverse()
# print (names)     #изменяет оригинальный массив в отличии от среза
# print(names[::-1])  # не изменяет оригинальный массив в отличии от reverse

# ########## in ##############              узнать если такой в списке через True /// False
# names = ["Emir", "Zhenya", "Beka"]
# print("Emir" in names)
# print("Gusev" in names)



# ###############   Функция min() / max()  sum()    #######################

# numbers = [1, 2, 3, 4, 5]
# print (max(numbers))
# print (min(numbers))
# print(sum(numbers))


# from math import prod
# print(prod(numbers))     ### произведение 



# ############       *            #################             распаковывает массив  (убирает ковычки и запятые)
names = ["Emir", "Zhenya", "Beka"]
print (*names)
