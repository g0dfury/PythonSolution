# easy a 
# num = list(map(int, input().split()))
# for i in range(1, len(num)):
#     if num[i] > num[i-1]:
#         print(num[i], end=", ")

# easy b
# num = list(map(int, input().split()))
# max_even = -1 # чтоб узнать является ли число положи
# for i in num:
#     if i % 2 == 0 and i > max_even:
#         max_even = i
# if max_even == -1:
#     print("Error")
# else:
#     print(max_even)

# medium a
# d = {
#     "OOP":[81, 88, 72, 97],
#     "ICT":[78, 69, 86, 98],
#     "MATH":[65, 69, 78, 98],
#     "PHYSICS":[87, 99, 66, 70]
# }

# for subjects, grades in d.items():
#     average = sum(grades) / len(grades)
#     print(subjects + ":", average)


# # hard a
# num = list(map(int, input().split()))
# max_odd = -1
# for i in num:
#     if i % 2 != 0 and i > max_odd:
#         max_odd = i
        
# res = 0
# while i > 0:
#     digit = i % 10 #последняя цифра
#     res += digit #0 + первая цифра + последняя цифра
#     i //= 10  #первая цифра

# if max_odd == -1:
#     print("error")
# else:
#     print("Число: ", max_odd, "Сумма: ", res)


# hard b
spp_students = ["Almira", "Erlan", "Alan"]
python_students = ["Aidana", "Almira"]

python_set = set(python_students)
cpp_set = set(spp_students)

only_python = python_set - cpp_set
only_cpp = cpp_set - python_set

print(len(only_python) + len(only_cpp))

# symmetric_difference чтоб узнать разницу сразу двух сетов
