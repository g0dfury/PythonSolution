# # ### Dictionary / frozen set / tuple

# # ##### frozenset() #####
# # # st = {1, 2, 3}
# # # st.add(4)
# # # print(st)

# # # st = frozenset({1, 2, 3})
# # # st.add(4)  
# # # print(st)   #error  {frozenset unchangible function}




# # ######## tuple() ##########
# # numbers = (1, 2, 3, 4)
# # # numbers.append(5)     #error  {поддерживает только index, copy}
# # print(numbers[-1])

# # for el in numbers:
# #     print(el)

# # if 2 in numbers:
# #     print("YES")
# # if 5 in numbers:
# #     print("NO")
# # if 7 not in numbers:
# #     print("NOT")

# # print(numbers)


# # # как работает tuple
# # t = ("emir")
# # print(type(t))   #str

# # r = ("emir", )
# # print(type(r))  #tuple

# # z = [1, 2, 3]
# # print(type(z))  #list

# # y = [1, 2, 3, ]
# # print(type(y))   #tuple




# # # ########## dict ()  #######
# # # empty_dict = {} # пустой dict
# # # empty_set = {"python", "java", "js"}  # заполненный set
# # full_dict = {"abc": 1,    # ключ - значения ключа (ключ должен быть уникальным всегда, не повторяться)
# #  5: 2,
# #   0.3: 3}
# # print(type(full_dict))
# # print(len(full_dict))

# # # в роли ключа можно использовать любой тип данных (str, int, float, bool), а в роли значения вообще что угодно


# # # Как использовать ключи (индексы)?

# # print(full_dict["abc"])
# # print(full_dict[5])
# # print(full_dict[0.3])

# # student = {
# #     "name": "Emir",
# # #     "age": 27,
# # #     "height": 175,
# # #     "GPA": 2.8,
# # #     "subjects": ["Statistics", "Financing", "Macroeconomics"],
# # #     "point": [70, 75, 96]

# # # }
# # # print(student["subjects"][-1])
# # # print(sum(student)["point"] / len(student)["point"])


# # x ={
# #     "abc": 100,
# #     "def": "decode"
# # }
# # x["def"] = "python"   #изменяется "def":"decode"  -> "python"
# # x["qwerty"] = "c++"     #изменяется 
# # print(x)


# # ######## методы

# # # .get
# student = {
#     "name": "Emir",
#     "age": 27,
    # "height": 175,
# }
# # print(student["surname"])
# # print(student.get("surname"))  # --> none (не ломает программу)
# # print(student("name"))
# # print(student.get("name"))


## .pop ()
# deleted_value = student.pop("height")
# print(student)
# print(deleted_value)

# # # .poopitem () удаляет парпу ключ значние
# d = student.popitem()
# print(student)
# print(d)

# # # .update()   - добавляет один dict в другой dict
# # a ={
# #     1: 1,
# #     2: 4
# # }
# # b = {
# #     3: 9,
# #     4: 16
# # }
# # a.update(b)
# # # a.update({5: 25})
# # print(a)



# dict.fromkeys() 
letters = ["a", "b", "a", "c", "a", "b", "d", "c"]
d = dict.fromkeys(letters, 0)
for letter in letters:
    d[letter] += 1
print(d)

# ### zip() #####    #объединяет ключи со значениями (лишние ключи или значения )
# x = ["python", "c++", "java"]
# y = [3.10, 14.8, 6, 8]
# d = dict(zip(x, y))
# print(d)

# string = "emirdin"
# z = dict.fromkeys(string, 0)
# for i in string:
#     z[i] += 1
# print(z)


# student = {
#     "name": "Emir",
#     "age": 27,
#     "height": 175,
# }


# ####### .keys () ######         ---- > выводит все ключи
# # print(student.keys())

# # for el in student.keys():
# #     print(el)

# # ###### .values() ###      ----- >    выводит все значения

# # print(student.values())

# # ### .items() ####       -----> выводит пары ключей
# # print(student.items())

# for k, v in student.items():
#     print(k, v)











# # easy a 
# keys = ["Ten", "Twenty", "Thirty"]
# values = [10, 20, 30]
# z = dict(zip(keys, values))
# print(z)


# # easy b
# ## Easy B 
# # вывести значение ключа history
# sample_dict = { 
#     "class": { 
#         "student": { 
#             "name": "Mike", 
#             "marks": { 
#                 "physics": 70, 
#                 "history": 80 
#             } 
#         } 
#     } 
# } 
# print(sample_dict["class"]["student"]["marks"]["history"])


# # Easy C
# d = { 
#     "math": 75, 
#     "physics": 90, 
#     "ict": 64, 
#     "ads": 70 
# }

# min_v = min(d.values())
# for k, v in d.items():
#     if v == min_v:
#         print(k)
#         # break

    
# # Easy D
# info = {
#     "name": "Aidana",
#     "grades": [96, 78, 67, 73, 90]
# }
# # print (sum(info)["grades"] / len(info)["grades"])
# x = info["grades"]
# print(sum(x) / len(x))