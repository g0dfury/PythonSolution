# # #eval - :>
# # ##### строки - str #######
# text = "ronaldo_7"
# # print (text[3])  # a
# # print (text[-1])   # 7


# # ## длина строки

# # print(len(text))   # 9


# # # text [0] = "D"  ### нельзя менять строку
# # # text [0], text [1] = text [1], text [0]   ### нельзя менять

# # # ##slice - срез
# print(text[2:6]) # nald
# print (text[2:]) #naldo_7
# print (text[:7]) #ronaldo 
# print (text[::-1]) #7_odlanor

# # #итерация в строчке   V1
# for letter in text:
#     print (letter)

# for i in range(len(text)):  #V2 (better)
#     print (i, text[i])



# # # формватирование
# #  вставка данных в строку

###    V1:   {} - holder        variable.forman("data", some nubmer)
# text = "https://www.{}.{:.4f}/"
# print (text.format("google", "com"))

# domen = "your name is {}, and you are {} years old"
# print (domen.format("Emir", 19))

# # # ##### V2:   f - string 
# # # name = "decode"
# # # zone = "kz"
# # # print(f"https://www.{name}.{zone}/")

# name = "Emir"
# age = "19"
# print(f"Your name is {name}, and you are {age} years old!")


# name = "Emir"
# age = 19
# print(f"your name is {name}, and you are {age} years old")



# #### V3         %s    %i
# text = "My name is %s, I am %i years old!"
# text_v2 = "My name is %s, I am %.1f years old!"
# name = "John"
# age = 36
# print(text % (name, age))
# print(text_v2 % (name, age))


# ###### Методы строки      #### выводит текст либо заглавными буквами либо маленькими
# #1             .lower()      and .upper() ####

# text = "Emirdin"
# print (text.lower())
# print (text.upper())


# # # 2          .islower()      .isupper()    isalpha () - #Задает вопрос является все ли символы маленькие или заглавные (Output: True/False)
# print(text.islower())
# print(text[0].islower())

# #3           .isdigit()  ###       ### задает вопрос цифра ли Output: True/False

# text = "1z33h7"
# for symbol in text:
#     print (symbol, symbol.isdigit())

# #4      .count()  ####
# text = "emirdin"
# print (text.count("i"))


# #5       .replace()

# text = "My name is Omar"
# print(text.replace("O", "E").replace("a", "i"))

# #6      .index()        .find  
#         # .rindex()     .rfind()

# text = "python"
# print(text.index("n"))  #5
# print(text.find("n"))   #5     если выдаст -1, означает что строка не найдена (не сломается программа)


# # 7    .strip()   # убирает лишние пробелы
# name = input("asda").strip()
# age = input().strip()
# print (f"Ваше имя: {name}, ваш возраст: {age}")

# 8    .title()      .capitalize()   # фиксит пользовательские инпуты

# text = "deCODE schOOl groUp"
# print(text.capitalize())   #делает только первую букву заглавной
# print(text.title())    #делает первую букву во всех словах заглавной


# #9  .split()  #

text = "1 2 2 3"
print(text.split())

# # data = "06/03/2023"
# # print(data.split("/"))



# # 10     .join()          # создает из массива строку
# # text = ["Decode", "School", "Generation"]
# # print("-".join(text))

# # time = [20, 56, 34]
# # print(":".join(map(str, time)))    #join не читает ничего кроме строки, через map() фиксим эту проблему

# text = "ronaldo"
# print(text[0:8])