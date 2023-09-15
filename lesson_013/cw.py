# ## max()        min()
# names = ["Emir", "Eugene", "Beksultan", "Nariman"]
# print(max(names))
# print(max(names, key=len))
# print()
# print(min(names))
# print(min(names, key=len))  

# # таблица ASCII смотрит только на первую букву


# d = { 
#     "math": 75, 
#     "physics": 90, 
#     "ict": 64, 
#     "ads": 70 
# }

# # print(min(d, key=d.get))
# kkk = min(d, key=d.get)
# print(kkk, d[kkk])


# ###### .sorted()    .sort()
# # сортируется только list
# # .sorted ()   -  автоматически конвертирует в list, но не меняет оригинальный список

# st = {"ads", "phys", "ict", "math", "oop"}
# list_st = list(st)
# list_st.sort()
# print(list_st)

# list_st = sorted(st)
# print(list_st)


# names = ["Emir", "Zhenya", "Beksultan", "Nariman"]
# names.sort(key=len, reverse=True)  # по длине от большего до меньше (от "Beksultan" до "Emir")
# print(names)

#       .reverse()    по дефолту False, при True переворачивает list


# Easy A
# nums = list(map(int, input().split()))
# summa = sum(nums)
# if summa > 10:
#     print("More")
# elif summa < 10:
#     print("Less")
# else:
#     print("Equal")

# # easy b
# a = input()
# b = input()
# print (f"http://www.{a}.{b}/")

# easy c
# word = input()
# st = set(word)
# print(len(st))

# # easy d
# text = input().split()
# for letter in text:
#     l = len(letter)
#     print(letter, l)

# meidum a
# ls = list(map(str, input().split()))
# print(*ls[1::2])

# medium b
# is_alphabet = True
# text = input()
# for i in range(len(text)):
#     if ord(text[i]) - i != 97:
#         is_alphabet = False
#         break 
# if is_alphabet:
#     print("good")
# else:
#     print("cringe")


# # medium c
# n = int(input())
# results = {}
# # Считываем имена и оценки
# for i in range(n):
#     name, grade = input().split()
#     grade = int(grade)
#     # Если имя уже есть в словаре, выбираем лучшую оценку
#     if name in results:
#         results[name] = max(results[name], grade)
#     else:
#         results[name] = grade
# # Сортируем имена по алфавиту
# names = sorted(results.keys())
# # Выводим лучшие результаты
# for name in names:
#     print(name, results[name])
