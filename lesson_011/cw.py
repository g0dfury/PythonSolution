# # text = "qwerty"
# # print(list(text))

# #type       -           чтоб узнать тип данных
# # set       -          unique, {}, не включает в себя повторяющиеся элементы.

# ######## Как создать пустой сет #######

# # st = set ()
# # print (type(st))
# # print (len(st))

# st = {1, 2, 3}
# print(type(st))
# print(len(st))

# ##### Итерация ##
# # st = {"python", "cpp", "js"}
# # for el in st:
# #     print(el, end=" ")

# # print("cpp" in st)
# # print("python" not in st)  

# ################   Методы  #######
# #1 .clear()         .copy()


# #2 .add()  ###
# # st = {"a", "b", "c"}
# # st.add("d")
# # print(st)



#  # 3   .remove() - ломает программу в случае ошибки    
# # st = {"a", "b", "c", "d"}
# # st.remove("b")
# # #  .discard()  - не ломает программу в случае ошибки 
# # print(st)
# # st.discard("b")
# # print(st)
# # #  .pop()   - удаляет рандомные элементы
# # st = {"a", "b", "c", "d"}
# # deleted = st.pop()
# # print(st)
# # print("deleted: ", deleted)


# online = {"emir", "zhenya", "beka", "dawa"}
# offline = {"dawa", "firuza", "aigerim", "emir"}
# #4   .union()      -       создает новый сет где 2 списка объеденены   
# #    .update()   -      создает новый сет создает новый сет меняя оригинал  
# # print(online.union(offline))

# # online.update(offline)
# # print(offlinr)
# # print(online)


# # ##5      .intersection()
# print(online.intersection(offline))


# print(online.intersection_update(offline))



# # # ###6      difference()
# print(online.difference(offline))
# print(offline.difference(online))


# #7 .symmetric_difference ()
# print(online.symmetric_difference(offline))

# #8   .issubset()        .issuperset
languages = {"java", "js", "c++", "python", "c#", "go", "c"}
c_languages = {"c++", "c#", "c"}

print(c_languages.issubset(languages))
print(languages.issuperset(c_languages))



# ### set () ####    -        конвертация массива в сет
# # number = [1, 2, 3, 4, 2, 1, 3]
# # st = set(number)
# # print(st)


# st = {"a", "b", "c"}
# print(list(st))


# ### input () 

# # x = input().split()
# # print(x)


# # numbers = set(map(int, input().split()))
# # print(numbers)




# # cw
# # ae
# # set1 = {10, 20, 30, 40, 50}
# # set2 = {30, 40, 50, 60, 70}
# # print(set1.union(set2))

# # # be
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.intersection(set2))

# # # ce
# # set1 = {10, 20, 30, 40, 50}
# # set2 = {30, 40, 50, 60, 70}
# # print(set1.difference(set2))
# # print(set2.difference(set1))

# # # de
# # text = input().split()
# # print(set(text))

# # a md
# # text = input()
# # lenght = len(set(text))
# # print(lenght, set(text))


# b md

# N = int(input())
# people = set(input().split())
# print(N - len(set(people)))

# c md
# x = [1, 1, 2, 3, 4]
# print(x)
# y = {1, -312, 1, 2, 3, 4, 13, 12, 2, 3}
# print(y)
